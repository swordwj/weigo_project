from flask import request,render_template,Flask,redirect,url_for,session
from main.models import User,Post,Like,Comment,connect_db

def comment(postid,host):
    try:
        if session.get('username') != host:
            return render_template('notlogin.html')
        else:
            try:
                # 获取post内容，在评论页面显示
                sql1 = 'SELECT * FROM message WHERE message_id = %s;'
                parm1 = (postid,)
                rows = Post().get_Post(sql1, parm1)
                post = rows[1]
                posttime = rows[2]
                # 获取发post的用户信息，传递给页面
                posthostid = rows[6]
                sql2 = 'SELECT * FROM users WHERE user_id = %s;'
                parm2 = (posthostid,)
                row = User().get_User(sql2, parm2)
                posthost = row[1]
                posthostpic = row[6]
                # 获取post的所有评论，把信息返回给评论页面
                sql2 = 'SELECT comment.*,users.userpic FROM comment,users WHERE message_id = %s AND users.user_id = comment.user_id ORDER BY comment_id DESC;;'
                parm2 = (postid,)
                comms = Comment().get_AllComment(sql2, parm2)
                # 查询post的评论数量
                sql3 = 'SELECT COUNT(user_id) FROM comment WHERE message_id = %s;'
                parm3 = (postid,)
                commnum = Comment().get_Comment(sql3, parm3)
                # 更新到数据库
                sql4 = 'UPDATE message SET message_commentnum = %s  WHERE message_id = %s;'
                parm4 = (commnum[0], postid)
                Post().set_Post(sql4, parm4)
            except:
                return render_template('error1.html')
            return render_template('comments.html', postid=postid, host=host, post=post, posthost=posthost,posthostpic=posthostpic,
                                   posttime=posttime, comms=comms)
    except:
        return render_template('error.html')


def addComment(postid,host):

    try:
        if session.get('username') != host:
            return render_template('notlogin.html')
        else:
            try:
                # 查询登录用户的ID
                sql = 'SELECT * FROM users WHERE user_name = %s;'
                parm = (host,)
                rows = User().get_User(sql, parm)
                hostid = rows[0]
                hostname = rows[1]
                content = request.form['commbox']
            except:
                return render_template('error1.html')

            if content.strip() == '':
                try:
                    error = 'You left nothing!'
                    # 发送内容如果为空，提示并返回主页
                    sql = 'SELECT * FROM comment WHERE message_id = %s ORDER BY comment_id DESC;'
                    parm = (postid,)
                    comms = Comment().get_AllComment(sql, parm)
                    # 显示post
                    sql1 = 'SELECT * FROM message WHERE message_id = %s;'
                    parm1 = (postid,)
                    rows = Post().get_Post(sql1, parm1)
                    post = rows[1]
                    # 获取posthost和posttime
                    posthostid = rows[6]
                    sql2 = 'SELECT * FROM users WHERE user_id = %s;'
                    parm2 = (posthostid,)
                    row = User().get_User(sql2, parm2)
                    posthost = row[1]
                    posttime = rows[2]
                except:
                    return render_template('error1.html')
                return render_template('comments.html', postid=postid, posttime=posttime, posthost=posthost, host=host,
                                       error=error, post=post, comms=comms)
            else:
                try:
                    # 添加评论
                    sql_add = 'INSERT INTO comment (comment_info,comment_time,message_id,user_id,user_name) VALUES (%s,%s,%s,%s,%s);'
                    # 获取当前时间
                    import datetime
                    now = datetime.datetime.now()
                    # 转换为指定的格式
                    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")

                    parm_add = (request.form['commbox'], otherStyleTime, postid, hostid, hostname)
                    Comment().set_Comment(sql_add, parm_add)
                except:
                    conn = connect_db()
                    conn.rollback()
                    conn.close()
                    return render_template('error1.html')
                return redirect(url_for('comment', postid=postid, host=host))
    except:
        return render_template('error.html')


def delComment(postid,commid,host):
    try:
        if session.get('username') != host:
            return render_template('notlogin.html')
        else:
            try:
                # 删除comment
                sql_del = 'DELETE FROM comment WHERE comment_id = %s;'
                parm_del = (commid,)
                Comment().set_Comment(sql_del, parm_del)
            except:
                conn = connect_db()
                conn.rollback()
                conn.close()
                return render_template('error1.html')
            return redirect(url_for('comment', postid=postid, commid=commid, host=host))
    except:
        return render_template('error.html')


def editCommpage(commid,host):
    try:
        if session.get('username') != host:
            return render_template('notlogin.html')
        else:
            try:
                # 获取comm内容
                sql = 'SELECT * FROM comment WHERE  comment_id = %s;'
                parm = (commid,)
                row = Comment().get_Comment(sql, parm)
                comm = row[1]
            except:
                return render_template('error1.html')
            return render_template('comm_edit.html', host=host, commid=commid, comm=comm)
    except:
        return render_template('error.html')


def editComment(commid,host):
    try:
        if session.get('username') != host:
            return render_template('notlogin.html')
        else:
            try:
                sql = 'SELECT * FROM comment WHERE  comment_id = %s;'
                parm = (commid,)
                row = Comment().get_Comment(sql, parm)
                postid = row[3]
                content = request.form['commeditbox']
            except:
                return render_template('error1.html')
            if content.strip() == '':
                error = 'you left nothing'
                return render_template('comm_edit.html', host=host, commid=commid, error=error)
            else:
                try:
                    # 更改后的comment更新到数据库
                    sql = 'UPDATE comment SET comment_info = %s WHERE comment_id = %s;'
                    parm = (request.form['commeditbox'], commid)
                    Comment().set_Comment(sql, parm)
                except:
                    conn = connect_db()
                    conn.rollback()
                    conn.close()
                    return render_template('error1.html')
                return redirect(url_for('comment', postid=postid, host=host))
    except:
        return render_template('error.html')

