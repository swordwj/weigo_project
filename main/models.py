import psycopg2
from flask import current_app,render_template
from DBUtils.PooledDB import PooledDB
import traceback

def connect_db():
    # try:
    #     conn = psycopg2.connect(host=current_app.config['HOST'],
    #         port = current_app.config['PORT'],
    #         user = current_app.config['USER'],
    #         password = current_app.config['PASSWORD'],
    #         database = current_app.config['DATABASE'])
    #     return conn
    # except:
    #     return render_template('error1.html')
    try:
        pool = PooledDB(psycopg2,
            mincached=1,
            maxcached=10,
            maxconnections=10,
            blocking=True,
            host=current_app.config['HOST'],
            port = current_app.config['PORT'],
            user = current_app.config['USER'],
            password = current_app.config['PASSWORD'],
            database = current_app.config['DATABASE'])
        conn = pool.connection()
        return conn
    except:
        print("can not connect database!")
        traceback.print_exc()
        return render_template('error1.html')

class User():

    def get_User(self,sql='',parm=()):
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql,parm)
        self.result =  self.cur.fetchone()
        return self.result

    def get_AllUser(self,sql='',parm=()):
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql,parm)
        self.result =  self.cur.fetchall()
        return self.result

    def set_User(self,sql='',parm=()):
        try:
            conn = connect_db()
            self.cur = conn.cursor()
            self.cur.execute(sql, parm)
        except:
            conn = connect_db()
            conn.rollback()
            traceback.print_exc()
            return render_template('error1.html')
        conn.commit()
        conn.close()

class Post():

    def get_Post(self,sql='',parm=()):
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql,parm)
        self.result =  self.cur.fetchone()
        return self.result

    def get_AllPost(self,sql='',parm=()):
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql,parm)
        self.result = self.cur.fetchall()
        return self.result

    def set_Post(self,sql='',parm=()):
        try:
            conn = connect_db()
            self.cur = conn.cursor()
            self.cur.execute(sql, parm)
        except:
            conn = connect_db()
            conn.rollback()
            traceback.print_exc()
            return render_template('error1.html')
        conn.commit()
        conn.close()

class Comment():

    def get_Comment(self,sql='',parm=()):
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql,parm)
        self.result =  self.cur.fetchone()
        return self.result

    def get_AllComment(self,sql='',parm=()):
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql,parm)
        self.result = self.cur.fetchall()
        return self.result

    def set_Comment(self,sql='',parm=()):
        try:
            conn = connect_db()
            self.cur = conn.cursor()
            self.cur.execute(sql, parm)
        except:
            conn = connect_db()
            conn.rollback()
            traceback.print_exc()
            return render_template('error1.html')
        conn.commit()
        conn.close()

class Like():

    def get_Like(self,sql='',parm=()):
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql,parm)
        self.result =  self.cur.fetchone()
        return self.result

    def add_Like(self,sql='',parm=()):
        try:
            conn = connect_db()
            self.cur = conn.cursor()
            self.cur.execute(sql, parm)
        except:
            conn = connect_db()
            conn.rollback()
            traceback.print_exc()
            return render_template('error1.html')
        conn.commit()
        conn.close()

    def del_Like(self,sql='',parm=()):
        try:
            conn = connect_db()
            self.cur = conn.cursor()
            self.cur.execute(sql, parm)
        except:
            conn = connect_db()
            conn.rollback()
            traceback.print_exc()
            return render_template('error1.html')
        conn.commit()
        conn.close()

class Relation():

    def get_Relation(self,sql='',parm=()):
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql,parm)
        self.result =  self.cur.fetchone()
        return self.result

    def get_AllRelation(self, sql='', parm=()):
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql, parm)
        self.result = self.cur.fetchall()
        return self.result

    def set_Relation(self,sql='',parm=()):
        try:
            conn = connect_db()
            self.cur = conn.cursor()
            self.cur.execute(sql, parm)
        except:
            conn = connect_db()
            conn.rollback()
            traceback.print_exc()
            return render_template('error1.html')
        conn.commit()
        conn.close()

class Photo():

    def get_Photo(self,sql='',parm=()):
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql,parm)
        self.result =  self.cur.fetchone()
        return self.result

    def set_Photo(self,sql='',parm=()):
        try:
            conn = connect_db()
            self.cur = conn.cursor()
            self.cur.execute(sql, parm)
        except:
            conn = connect_db()
            conn.rollback()
            traceback.print_exc()
            return render_template('error1.html')
        conn.commit()
        conn.close()

# def handleSqlError(function):
#     def handleProblems(*args, **kwargs):
#         try:
#             return function(*args, **kwargs)
#         except:
#             return render_template('error1.html')
#     return handleProblems
#
# @handleSqlError
# def connect_db():
#     # conn = psycopg2.connect(database="weigodb", user="postgres", password="123456", host="localhost", port="5432")
#     # return conn
#     try:
#         conn = psycopg2.connect(host=current_app.config['HOST'],
#             port = current_app.config['PORT'],
#             user = current_app.config['USER'],
#             password = current_app.config['PASSWORD'],
#             database = current_app.config['DATABASE'])
#         return conn
#     except:
#         return render_template('error1.html')
#
# class User():
#
#     @handleSqlError
#     def get_User(self,sql='',parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql,parm)
#         self.result =  self.cur.fetchone()
#         return self.result
#
#     @handleSqlError
#     def get_AllUser(self,sql='',parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql,parm)
#         self.result =  self.cur.fetchall()
#         return self.result
#
#     @handleSqlError
#     def set_User(self,sql='',parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql, parm)
#         conn.commit()
#         conn.close()
#
# class Post():
#
#     @handleSqlError
#     def get_Post(self,sql='',parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql,parm)
#         self.result =  self.cur.fetchone()
#         return self.result
#
#     @handleSqlError
#     def get_AllPost(self,sql='',parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql,parm)
#         self.result = self.cur.fetchall()
#         return self.result
#
#     @handleSqlError
#     def set_Post(self,sql='',parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql, parm)
#         conn.commit()
#         conn.close()
#
# class Comment():
#
#     @handleSqlError
#     def get_Comment(self,sql='',parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql,parm)
#         self.result =  self.cur.fetchone()
#         return self.result
#
#     @handleSqlError
#     def get_AllComment(self,sql='',parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql,parm)
#         self.result = self.cur.fetchall()
#         return self.result
#
#     @handleSqlError
#     def set_Comment(self,sql='',parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql, parm)
#         conn.commit()
#         conn.close()
#
# class Like():
#
#     @handleSqlError
#     def get_Like(self,sql='',parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql,parm)
#         self.result =  self.cur.fetchone()
#         return self.result
#
#     @handleSqlError
#     def add_Like(self,sql='',parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql, parm)
#         conn.commit()
#         conn.close()
#
#     @handleSqlError
#     def del_Like(self,sql='',parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql, parm)
#         conn.commit()
#         conn.close()
#
# class Relation():
#
#     @handleSqlError
#     def get_Relation(self,sql='',parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql,parm)
#         self.result =  self.cur.fetchone()
#         return self.result
#
#     @handleSqlError
#     def get_AllRelation(self, sql='', parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql, parm)
#         self.result = self.cur.fetchall()
#         return self.result
#
#     @handleSqlError
#     def set_Relation(self,sql='',parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql, parm)
#         conn.commit()
#         conn.close()
#
# class Photo():
#
#     @handleSqlError
#     def get_Photo(self,sql='',parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql,parm)
#         self.result =  self.cur.fetchone()
#         return self.result
#
#     @handleSqlError
#     def set_Photo(self,sql='',parm=()):
#         conn = connect_db()
#         self.cur = conn.cursor()
#         self.cur.execute(sql, parm)
#         conn.commit()
#         conn.close()