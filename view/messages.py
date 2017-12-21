from flask import request,render_template,Flask,redirect,url_for,session
from main.models import User,Post,Like,Comment,Photo

def home(host):
    if session.get('username') == host:
        # get infomation of host
        sql = 'SELECT * FROM users WHERE user_name = %s;'
        parm = (host,)
        hosts = User().get_User(sql, parm)
        # get infomation the posts of host and friend
        sql1 = 'SELECT message.*,users.user_name,users.userpic FROM message,relation,users WHERE relation.user_id = %s AND message.user_id = relation.follow_id AND message.user_id = users.user_id;'
        parm1 = (hosts[0],)
        posts1 = Post().get_AllPost(sql1, parm1)
        sql2 = 'SELECT message.*,users.user_name,users.userpic FROM message,users WHERE message.user_id = %s and message.user_id = users.user_id;'
        parm2 = (hosts[0],)
        posts2 = Post().get_AllPost(sql2, parm2)
        posts = sorted(posts1 + posts2, reverse=True)

        return render_template('homeopage.html', hosts=hosts, posts=posts)

    else:
        return render_template('notlogin.html')

def addPost(host):
    if session.get('username') != host:
        return render_template('notlogin.html')
    else:
        sql = 'SELECT * FROM users WHERE user_name = %s;'
        parm = (host,)
        rows = User().get_User(sql, parm)
        hostid = rows[0]
        print(hostid)
        content = request.form['postbox']

        if content.strip() == '':
            error = 'You can not send nothing!'
            # can not send nothing
            sql = 'SELECT * FROM message WHERE user_id = %s ORDER BY message_id DESC;'
            parm = (hostid,)
            posts = Post().get_AllPost(sql, parm)
            return render_template('homeopage.html', hosts=rows, posts=posts, error=error)
        else:
            # insert a post
            sql_add = 'INSERT INTO message (message_info,message_time,user_id) VALUES (%s,%s,%s);'
            # 获取当前时间
            import datetime
            now = datetime.datetime.now()
            # 转换为指定的格式
            otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")

            parm_add = (request.form['postbox'], otherStyleTime, hostid)
            Post().set_Post(sql_add, parm_add)

            # update host's number of post
            sql_update = 'UPDATE users SET postnum = postnum + 1  WHERE user_id = %s;'
            parm = (hostid,)
            User().set_User(sql_update, parm)
            return redirect(url_for('home', host=host))


def deletePost(postid,host):
    if session.get('username') != host:
        return render_template('notlogin.html')
    else:
        # delete post
        sql_del = 'DELETE FROM message WHERE message_id = %s;'
        parm_del = (postid,)
        Post().set_Post(sql_del, parm_del)
        # udate the number of post
        sql_update = 'UPDATE users SET postnum = postnum - 1  WHERE user_name = %s;'
        parm = (host,)
        User().set_User(sql_update, parm)
        # delete the like of post
        sql_del1 = 'DELETE FROM likes WHERE message_id = %s;'
        parm_del1 = (postid,)
        Like().del_Like(sql_del1, parm_del1)
        # delete comments of post
        sql_del2 = 'DELETE FROM comment WHERE message_id = %s;'
        parm_del2 = (postid,)
        Comment().set_Comment(sql_del2, parm_del2)

        return redirect(url_for('home', host=host))


def editPage(postid,host):

    if session.get('username') != host:
        return render_template('notlogin.html')
    else:
        sql1 = 'SELECT * FROM message WHERE message_id = %s;'
        parm1 = (postid,)
        rows = Post().get_Post(sql1, parm1)
        userid = rows[6]
        post = rows[1]
        return render_template('post_edit.html', host=host, postid=postid, post=post)

def editPost(postid,host):

    if session.get('username') != host:
        return render_template('notlogin.html')
    else:
        content = request.form['posteditbox']
        if content.strip() == '':
            error = 'you left nothing'
            return render_template('post_edit.html', host=host, postid=postid, error=error)
        else:
            # update post to datebase
            sql = 'UPDATE message SET message_info = %s  WHERE message_id = %s;'
            parm = (request.form['posteditbox'], postid)
            Post().set_Post(sql, parm)
            return redirect(url_for('home', host=host))


