from flask import request,render_template,abort,redirect,url_for,session
from main.models import User,connect_db
from hashlib import md5

# def handleError(function):
#     def handleProblems():
#         try:
#             return function()
#         except:
#             return render_template('error.html')
#     return handleProblems
#
# def create_md5(pwd,salt):
#     md5_obj = md5()
#     value = pwd + salt
#     md5_obj.update(value.encode("utf8"))
#     return md5_obj.hexdigest()
#
# @handleError
# def index():
#     return render_template('login.html')
#
# @handleError
# def rgs():
#     return render_template('register.html')
#
# @handleError
# def logout():
#     session.pop('username', None)
#     return render_template('login.html')
#
# @handleError
# def login():
#
#     salt_value = 'Ecm6'
#     sql = 'SELECT * FROM users WHERE user_name = %s;'
#     parm = (request.form['username'],)
#     rows = User().get_User(sql,parm)
#     if rows is None:
#         error = 'user not exist! please register first!'
#         return render_template('login.html',error1=error)
#
#     md5 = create_md5(request.form['password'], salt_value)
#     if request.form['username'] == rows[1] and md5 != rows[2]:
#         error = 'password is wrong!'
#         return render_template('login.html', error2=error)
#
#     if request.form['username'] == rows[1] and md5 == rows[2]:
#         host = rows[1]
#         session['username'] = request.form['username']
#         return redirect(url_for('home', host=host))
#
# @handleError
# def register():
#
#     sql = 'SELECT * FROM users WHERE user_name = %s;'
#     parm = (request.form['username'],)
#     rows = User().get_User(sql, parm)
#     if rows is not None:
#         error = 'user is already exist!'
#         return render_template('register.html', error1=error)
#     else:
#         if len(request.form['username']) < 2:
#             error = 'length of username is too short!'
#             return render_template('register.html', error1=error)
#         if len(request.form['password']) < 6:
#             error = 'length of password should be more than six!'
#             return render_template('register.html', error1=error)
#         else:
#             if request.form['password'] == request.form['repassword']:
#                 salt_value = 'Ecm6'
#                 md5 = create_md5(request.form['password'], salt_value)
#                 sql_add = 'INSERT INTO users (user_name,user_password) VALUES (%s,%s);'
#                 parm_add = (request.form['username'],md5)
#                 User().set_User(sql_add, parm_add)
#                 return render_template('success.html')
#             else:
#                 error = 'password is not same!'
#                 return render_template('register.html', error1=error)

def index():
    try:
        return render_template('login.html')
    except:
        return render_template('error.html')

def rgs():
    try:
        return render_template('register.html')
    except:
        return render_template('error.html')

def logout():
    try:
        session.pop('username', None)
        return render_template('login.html')
    except:
        return render_template('error.html')

def create_md5(pwd,salt):

    md5_obj = md5()
    value = pwd + salt
    md5_obj.update(value.encode("utf8"))
    return md5_obj.hexdigest()


def login():

    try:
        salt_value = 'Ecm6'
        sql = 'SELECT * FROM users WHERE user_name = %s;'
        parm = (request.form['username'],)
        rows = User().get_User(sql,parm)
    except:
        return render_template('error1.html')

    try:
        if rows is None:
            error = 'user not exist! please register first!'
            return render_template('login.html',error1=error)

        md5 = create_md5(request.form['password'], salt_value)
        if request.form['username'] == rows[1] and md5 != rows[2]:
            error = 'password is wrong!'
            return render_template('login.html', error2=error)

        if request.form['username'] == rows[1] and md5 == rows[2]:
            host = rows[1]
            session['username'] = request.form['username']
            return redirect(url_for('home', host=host))
    except:
        return render_template('error.html')


def register():

    try:
        sql = 'SELECT * FROM users WHERE user_name = %s;'
        parm = (request.form['username'],)
        rows = User().get_User(sql, parm)
    except:
        return render_template('error1.html')

    try:
        if rows is not None:
            error = 'user is already exist!'
            return render_template('register.html', error1=error)
        else:
            if len(request.form['username']) < 2:
                error = 'length of username is too short!'
                return render_template('register.html', error1=error)
            if len(request.form['password']) < 6:
                error = 'length of password should be more than six!'
                return render_template('register.html', error1=error)
            else:
                if request.form['password'] == request.form['repassword']:
                    try:
                        salt_value = 'Ecm6'
                        md5 = create_md5(request.form['password'], salt_value)
                        sql_add = 'INSERT INTO users (user_name,user_password) VALUES (%s,%s);'
                        parm_add = (request.form['username'],md5)
                        User().set_User(sql_add, parm_add)
                        return render_template('success.html')
                    except:
                        conn = connect_db()
                        conn.rollback()
                        conn.close()
                        return render_template('error1.html')
                else:
                    error = 'password is not same!'
                    return render_template('register.html', error1=error)
    except:
        return render_template('error.html')

