from flask import request,render_template,Flask,redirect,url_for,session
from main.models import User,Post,Like,Comment,Relation,connect_db

# def handleError(function):
#     def handleProblems(*args, **kwargs):
#         try:
#             return function(*args, **kwargs)
#         except:
#             return render_template('error.html')
#     return handleProblems
#
# @handleError
# def friend(host):
#     if session.get('username') != host:
#         return render_template('notlogin.html')
#
#     else:
#         #get host info
#         sql = 'SELECT * FROM users WHERE user_name = %s;'
#         parm = (host,)
#         hosts = User().get_User(sql, parm)
#         #get info of users who host follow
#         sql1 = 'SELECT users.* FROM users,relation WHERE relation.user_id = %s AND users.user_id = relation.follow_id;'
#         parm1 = (hosts[0],)
#         friends = Relation().get_AllRelation(sql1, parm1)
#         friend = Relation().get_Relation(sql1, parm1)
#         if friend is None:
#             info='You haven not been following anyone yet.Go and find friends ↑↑↑'
#             return render_template('friend.html', hosts=hosts,nofriend=info)
#         else:
#             return render_template('friend.html', hosts=hosts,friends=friends)
#
# @handleError
# def unFollow(host,userid):
#
#     if session.get('username') != host:
#         return render_template('notlogin.html')
#
#     else:
#         # get host info
#         sql = 'SELECT * FROM users WHERE user_name = %s;'
#         parm = (host,)
#         hosts = User().get_User(sql, parm)
#
#         # get info of user
#         # sql = 'SELECT * FROM users WHERE user_id = %s;'
#         # parm = (userid,)
#         # userinfo = User().get_User(sql, parm)
#
#         # delete relation
#         sql_del = 'DELETE FROM relation WHERE user_id = %s AND follow_id = %s;'
#         parm_del = (hosts[0], userid)
#         Relation().set_Relation(sql_del, parm_del)
#
#         # update the number of host follow
#         sql_update = 'UPDATE users SET follownum = follownum - 1  WHERE user_id = %s;'
#         parm = (hosts[0],)
#         User().set_User(sql_update, parm)
#
#         # update the number of user fans
#         sql_update1 = 'UPDATE users SET fansnum = fansnum - 1  WHERE user_id = %s;'
#         parm1 = (userid,)
#         User().set_User(sql_update1, parm1)
#
#         return redirect(url_for('friend',host=host))
#
# @handleError
# def searchFriend(host):
#
#     if session.get('username') != host:
#         return render_template('notlogin.html')
#
#     else:
#         #get info of search
#         sql = 'SELECT * FROM users WHERE user_name LIKE %s ORDER BY user_id DESC;'
#         parm = ("%" + request.form['searchfriend'] + "%",)
#         key = request.form['searchfriend']
#         users = User().get_AllUser(sql, parm)
#         user = User().get_User(sql, parm)
#         parm1 = (host,)
#         hosts = User().get_User(sql, parm1)
#         if user is None:
#             error = 'user is not exist!'
#             return render_template('friend.html', hosts=hosts,error=error)
#         else:
#             #查找已关注的人，与用户对比，确定状态
#             sql1 = 'SELECT users.* FROM users,relation WHERE relation.user_id = %s AND users.user_id = relation.follow_id;'
#             parm1 = (hosts[0],)
#             follows = Relation().get_AllRelation(sql1, parm1)
#             # followid = Relation().get_Relation(sql1, parm1)
#             return render_template('friend.html', hosts=hosts, users=users, follows=follows, key=key,list='User list')

def friend(host):
    try:
        if session.get('username') != host:
            return render_template('notlogin.html')
        else:
            try:
                #get host info
                sql = 'SELECT * FROM users WHERE user_name = %s;'
                parm = (host,)
                hosts = User().get_User(sql, parm)
                #get info of users who host follow
                sql1 = 'SELECT users.* FROM users,relation WHERE relation.user_id = %s AND users.user_id = relation.follow_id;'
                parm1 = (hosts[0],)
                friends = Relation().get_AllRelation(sql1, parm1)
                friend = Relation().get_Relation(sql1, parm1)
            except:
                return render_template('error1.html')
            if friend is None:
                info='You haven not been following anyone yet.Go and find friends ↑↑↑'
                return render_template('friend.html', hosts=hosts,nofriend=info)
            else:
                return render_template('friend.html', hosts=hosts,friends=friends)
    except:
        return render_template('error.html')


def unFollow(host,userid):

    try:
        if session.get('username') != host:
            return render_template('notlogin.html')
        else:
            try:
                # get host info
                sql = 'SELECT * FROM users WHERE user_name = %s;'
                parm = (host,)
                hosts = User().get_User(sql, parm)
            except:
                return render_template('error1.html')
            try:
                # delete relation
                sql_del = 'DELETE FROM relation WHERE user_id = %s AND follow_id = %s;'
                parm_del = (hosts[0], userid)
                Relation().set_Relation(sql_del, parm_del)
                # update the number of host follow
                sql_update = 'UPDATE users SET follownum = follownum - 1  WHERE user_id = %s;'
                parm = (hosts[0],)
                User().set_User(sql_update, parm)
                # update the number of user fans
                sql_update1 = 'UPDATE users SET fansnum = fansnum - 1  WHERE user_id = %s;'
                parm1 = (userid,)
                User().set_User(sql_update1, parm1)
            except:
                conn = connect_db()
                conn.rollback()
                conn.close()
                return render_template('error1.html')
            return redirect(url_for('friend',host=host))
    except:
        return render_template('error.html')


def searchFriend(host):
    try:
        if session.get('username') != host:
            return render_template('notlogin.html')
        else:
            try:
                #get info of search
                sql = 'SELECT * FROM users WHERE user_name LIKE %s ORDER BY user_id DESC;'
                parm = ("%" + request.form['searchfriend'] + "%",)
                key = request.form['searchfriend']
                users = User().get_AllUser(sql, parm)
                user = User().get_User(sql, parm)
                parm1 = (host,)
                hosts = User().get_User(sql, parm1)
            except:
                return render_template('error1.html')
            if user is None:
                error = 'user is not exist!'
                return render_template('friend.html', hosts=hosts,error=error)
            else:
                try:
                    #查找已关注的人，与用户对比，确定状态
                    sql1 = 'SELECT users.* FROM users,relation WHERE relation.user_id = %s AND users.user_id = relation.follow_id;'
                    parm1 = (hosts[0],)
                    follows = Relation().get_AllRelation(sql1, parm1)
                except:
                    return render_template('error1.html')
                return render_template('friend.html', hosts=hosts, users=users, follows=follows, key=key,list='User list')
    except:
        return render_template('error.html')


