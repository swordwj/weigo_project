from flask import request,render_template,Flask,redirect,url_for
from main.models import User,Post,Like,Comment,Relation

def postList(host):
    #get infomation of host
    sql = 'SELECT * FROM users WHERE user_name = %s;'
    parm = (host,)
    hosts = User().get_User(sql, parm)
    #get infomation of posts
    sql1 = 'SELECT * FROM message WHERE user_id = %s ORDER BY message_id DESC;'
    parm = (hosts[0],)
    posts = Post().get_AllPost(sql1,parm)

    return render_template('postlist.html',hosts=hosts,posts=posts)

def deletePostlist(postid,host):
    #delete post
    sql_del= 'DELETE FROM message WHERE message_id = %s;'
    parm_del = (postid,)
    Post().set_Post(sql_del,parm_del)
    #udate the number of post
    sql_update = 'UPDATE users SET postnum = postnum - 1  WHERE user_name = %s;'
    parm = (host,)
    User().set_User(sql_update, parm)
    #delete the like of post
    sql_del1 = 'DELETE FROM likes WHERE message_id = %s;'
    parm_del1 = (postid,)
    Like().del_Like(sql_del1, parm_del1)
    #delete comments of post
    sql_del2 = 'DELETE FROM comment WHERE message_id = %s;'
    parm_del2 = (postid,)
    Comment().set_Comment(sql_del2, parm_del2)

    return redirect(url_for('postlist', host=host))

def postlistLike(postid,host):
    #查找当前用户ID
    print(postid,host)
    sql = 'SELECT * FROM users WHERE user_name = %s;'
    parm = (host,)
    rows = User().get_User(sql, parm)
    hostid = rows[0]

    #如果用户没有点过赞，那么添加一条点赞
    sql_search = 'SELECT * FROM likes WHERE message_id = %s AND user_id = %s;'
    parm = (postid,hostid)
    result = Like().get_Like(sql_search,parm)

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
        #删除点赞信息
        sql_del = 'DELETE FROM likes WHERE message_id = %s and user_id = %s;'
        parm_del = (postid,hostid)
        Like().del_Like(sql_del, parm_del)
        return redirect(url_for('postlist', host=host))
    else:
        sql_add = 'INSERT INTO likes (message_id,user_id) VALUES (%s,%s);'
        parm_add = (postid, hostid)
        Like().add_Like(sql_add, parm_add)
        #对应post点赞数+1
        sql1 = 'SELECT * FROM message WHERE message_id = %s;'
        parm1 = (postid,)
        rows = Post().get_Post(sql1, parm1)
        likenum = rows[4]
        likenew = likenum + 1
        #更新点赞数的值
        sql2 = 'UPDATE message SET message_likenum = %s  WHERE message_id = %s;'
        parm2 = (likenew, postid)
        Post().set_Post(sql2, parm2)
        return redirect(url_for('postlist', host=host))