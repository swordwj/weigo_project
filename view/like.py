from flask import request,render_template,Flask,redirect,url_for,session
from main.models import User,Post,Like

def like(postid,host):
    if session.get('username') != host:
        return render_template('notlogin.html')
    else:

        # 查找当前用户ID
        print(postid, host)
        sql = 'SELECT * FROM users WHERE user_name = %s;'
        parm = (host,)
        rows = User().get_User(sql, parm)
        hostid = rows[0]

        # 如果用户没有点过赞，那么添加一条点赞
        sql_search = 'SELECT * FROM likes WHERE message_id = %s AND user_id = %s;'
        parm = (postid, hostid)
        result = Like().get_Like(sql_search, parm)

        if result is not None:
            # 对应post点赞数-1
            sql1 = 'SELECT * FROM message WHERE message_id = %s;'
            parm1 = (postid,)
            rows = Post().get_Post(sql1, parm1)
            likenum = rows[4]
            likenew = likenum - 1
            # 更新点赞数的值
            sql2 = 'UPDATE message SET message_likenum = %s  WHERE message_id = %s;'
            parm2 = (likenew, postid)
            Post().set_Post(sql2, parm2)
            # 删除点赞信息
            sql_del = 'DELETE FROM likes WHERE message_id = %s and user_id = %s;'
            parm_del = (postid, hostid)
            Like().del_Like(sql_del, parm_del)
            return redirect(url_for('home', host=host))
        else:
            sql_add = 'INSERT INTO likes (message_id,user_id) VALUES (%s,%s);'
            parm_add = (postid, hostid)
            Like().add_Like(sql_add, parm_add)
            # 对应post点赞数+1
            sql1 = 'SELECT * FROM message WHERE message_id = %s;'
            parm1 = (postid,)
            rows = Post().get_Post(sql1, parm1)
            likenum = rows[4]
            likenew = likenum + 1
            # 更新点赞数的值
            sql2 = 'UPDATE message SET message_likenum = %s  WHERE message_id = %s;'
            parm2 = (likenew, postid)
            Post().set_Post(sql2, parm2)
            return redirect(url_for('home', host=host))


