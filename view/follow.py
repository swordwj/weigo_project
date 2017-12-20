from flask import request,render_template,Flask,redirect,url_for,session
from main.models import User,Post,Like,Comment,Relation

def follow(key,host):

    if session.get('username') != host:
        return render_template('notlogin.html')

    else:
        # get userinfo which host search
        sql = 'SELECT * FROM users WHERE user_name LIKE %s ORDER BY user_id DESC;'
        parm = ("%" + key + "%",)
        users = User().get_AllUser(sql, parm)
        # get hostinfo
        parm2 = (host,)
        hosts = User().get_User(sql, parm2)
        # get userinfo which host already followed
        sql1 = 'SELECT users.* FROM users,relation WHERE relation.user_id = %s AND users.user_id = relation.follow_id;'
        parm1 = (hosts[0],)
        follows = Relation().get_AllRelation(sql1, parm1)
        return render_template('friend.html', hosts=hosts, key=key, users=users, follows=follows)


# function decoration baidu or google
def doFollow(state,host,username,key):

    if session.get('username') != host:
        return render_template('notlogin.html')
    else:
        # get id of host follow or unfollow
        sql = 'SELECT * FROM users WHERE user_name = %s;'
        parm = (username,)
        # users = User().get_AllUser(sql, parm)
        userinfo = User().get_User(sql, parm)

        # get host info
        parm2 = (host,)
        hosts = User().get_User(sql, parm2)

        # get userinfo which host search
        sql = 'SELECT * FROM users WHERE user_name LIKE %s  ORDER BY user_id DESC;'
        parm = ("%" + key + "%",)
        users = User().get_AllUser(sql, parm)

        # get userinfo which host follow
        sql1 = 'SELECT users.* FROM users,relation WHERE relation.user_id = %s AND users.user_id = relation.follow_id;'
        parm1 = (hosts[0],)
        follows = Relation().get_AllRelation(sql1, parm1)

        if state == 'FOLLOW':
            # can not follow hostself
            if host == username:
                error = 'you can not follow yourself'
                return render_template('friend.html', hosts=hosts, users=users, key=key, follows=follows, error=error)
            else:
                # add relation
                sql_add1 = 'INSERT INTO relation (user_id,follow_id) VALUES (%s,%s);'
                parm_add1 = (hosts[0], userinfo[0])
                Relation().set_Relation(sql_add1, parm_add1)
                # update the num of follow
                sql_update = 'UPDATE users SET follownum = follownum + 1  WHERE user_id = %s;'
                parm = (hosts[0],)
                User().set_User(sql_update, parm)
                # update the number of fans
                sql_update = 'UPDATE users SET fansnum = fansnum + 1  WHERE user_id = %s;'
                parm = (userinfo[0],)
                User().set_User(sql_update, parm)

                return redirect(url_for('follow', key=key, host=host))

        else:

            # delete relation
            sql_del = 'DELETE FROM relation WHERE user_id = %s AND follow_id = %s;'
            parm_del = (hosts[0], userinfo[0])
            Relation().set_Relation(sql_del, parm_del)

            # update the number of host follow
            sql_update = 'UPDATE users SET follownum = follownum - 1  WHERE user_id = %s;'
            parm = (hosts[0],)
            User().set_User(sql_update, parm)

            # update the number of user fans
            sql_update1 = 'UPDATE users SET fansnum = fansnum - 1  WHERE user_id = %s;'
            parm1 = (userinfo[0],)
            User().set_User(sql_update1, parm1)

            return redirect(url_for('follow', key=key, host=host))


def followList(host):

    if session.get('username') != host:
        return render_template('notlogin.html')

    else:
        sql = 'SELECT * FROM users WHERE user_name = %s;'
        parm = (host,)
        hosts = User().get_User(sql, parm)
        # get follows
        sql1 = 'SELECT users.* FROM users,relation WHERE relation.user_id = %s AND users.user_id = relation.follow_id;'
        parm1 = (hosts[0],)
        users = User().get_AllUser(sql1, parm1)
        # state = "UNFOLLOW"
        return render_template('userlist.html', hosts=hosts, users=users, list='Follow List')


def fansList(host):

    if session.get('username') != host:
        return render_template('notlogin.html')

    else:
        sql = 'SELECT * FROM users WHERE user_name = %s;'
        parm = (host,)
        hosts = User().get_User(sql, parm)
        # get fans
        sql1 = 'SELECT users.* FROM users,relation WHERE relation.follow_id = %s AND users.user_id = relation.user_id;'
        parm1 = (hosts[0],)
        users = User().get_AllUser(sql1, parm1)
        return render_template('userlist.html', hosts=hosts, users=users, list='Fans List')


