from flask import request,render_template,Flask,redirect,url_for,session
from main.models import User,Post,Like,Comment,Photo,connect_db
import os
from PIL import Image
import traceback

# UPLOAD_FOLDER = os.getcwd() + '//static//avatar//'
# ALLOWED_EXTENSIONS = ['png','jpg','bmp']
#
# def handleError(function):
#     def handleProblems(*args, **kwargs):
#         try:
#             return function(*args, **kwargs)
#         except:
#             return render_template('error.html')
#     return handleProblems
#
# @handleError
# def photoPage(host):
#     if session.get('username') != host:
#         return render_template('notlogin.html')
#     else:
#         # get infomation of host
#         sql = 'SELECT * FROM users WHERE user_name = %s;'
#         parm = (host,)
#         hosts = User().get_User(sql, parm)
#
#         return render_template('photo.html', hosts=hosts)
#
# @handleError
# def uploadPhoto(host):
#     if session.get('username') != host:
#         return render_template('notlogin.html')
#     else:
#         # get infomation of host
#         sql = 'SELECT * FROM users WHERE user_name = %s;'
#         parm = (host,)
#         hosts = User().get_User(sql, parm)
#
#         # 获取文件，判断格式
#         avatar = request.files['avatar']
#         fname = avatar.filename
#         flag = '.' in fname and fname.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
#         if not flag:
#             error = 'the type of file is wrong'
#             return render_template('photo.html', hosts=hosts, type_error=error)
#         # 添加文件到本地文件库
#         avatar.save('{}{}_{}'.format(UPLOAD_FOLDER, hosts[1], fname))
#         avatar_url = '/static/avatar/{}_{}'.format(hosts[1], fname)
#
#         #判断是否有已有头像
#         # sql = 'SELECT userpic FROM users WHERE user_id = %s;'
#         # parm = (hosts[0],)
#         # pic = User().get_User(sql, parm)
#         # if pic is None:
#         #     # 地址添加到数据库
#         #     sql_add = 'UPDATE users SET userpic = %s  WHERE user_id = %s;'
#         #     parm_add = (avatar_url,hosts[0])
#         #     User().set_User(sql_add,parm_add)
#         #     return redirect(url_for('home', host=host))
#         # else:
#
#         #更新
#         sql_add = 'UPDATE users SET userpic = %s  WHERE user_id = %s;'
#         parm_add = (avatar_url,hosts[0])
#         User().set_User(sql_add,parm_add)
#         return redirect(url_for('home', host=host))

UPLOAD_FOLDER = os.getcwd() + '//static//avatar//'
ALLOWED_EXTENSIONS = ['png','jpg','bmp']

def photoPage(host):
    try:
        if session.get('username') != host:
            return render_template('notlogin.html')
        else:
            try:
                # get infomation of host
                sql = 'SELECT * FROM users WHERE user_name = %s;'
                parm = (host,)
                hosts = User().get_User(sql, parm)
            except:
                traceback.print_exc()
                return render_template('error1.html')
            return render_template('photo.html', hosts=hosts)
    except:
        traceback.print_exc()
        return render_template('error.html')


def uploadPhoto(host):
    try:
        if session.get('username') != host:
            return render_template('notlogin.html')
        else:
            try:
                # get infomation of host
                sql = 'SELECT * FROM users WHERE user_name = %s;'
                parm = (host,)
                hosts = User().get_User(sql, parm)
            except:
                traceback.print_exc()
                return render_template('error1.html')
            # 获取文件，判断格式
            avatar = request.files['avatar']
            fname = avatar.filename
            flag = '.' in fname and fname.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
            if not flag:
                error = 'the type of file is wrong'
                return render_template('photo.html', hosts=hosts, type_error=error)
            # 添加文件到本地文件库
            avatar.save('{}{}_{}'.format(UPLOAD_FOLDER, hosts[1], fname))
            avatar_url = '/static/avatar/{}_{}'.format(hosts[1], fname)
            #更新
            try:
                sql_add = 'UPDATE users SET userpic = %s  WHERE user_id = %s;'
                parm_add = (avatar_url,hosts[0])
                User().set_User(sql_add,parm_add)
            except:
                conn = connect_db()
                conn.rollback()
                conn.close()
                traceback.print_exc()
                return render_template('error1.html')
            return redirect(url_for('home', host=host))
    except:
        traceback.print_exc()
        return render_template('error.html')

