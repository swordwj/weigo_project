import psycopg2
from flask import current_app

def connect_db():
    # conn = psycopg2.connect(database="weigodb", user="postgres", password="123456", host="localhost", port="5432")
    # return conn
    conn = psycopg2.connect(host=current_app.config['HOST'],
        port = current_app.config['PORT'],
        user = current_app.config['USER'],
        password = current_app.config['PASSWORD'],
        database = current_app.config['DATABASE'])
    return conn


class User():

    # def __init__(self,autocommit=True):
    #     self.conn = psycopg2.connect(database="weigodb", user="postgres", password="123456", host="localhost", port="5432")
    #     self.autocommit = autocommit
    #     self.cur = self.conn.cursor()

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
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql, parm)
        conn.commit()
        conn.close()

class Post():

    # def __init__(self, autocommit=True):
    #     self.conn = psycopg2.connect(database="weigodb", user="postgres", password="123456", host="localhost",
    #                                  port="5432")
    #     self.autocommit = autocommit
    #     self.cur = self.conn.cursor()

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
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql, parm)
        conn.commit()
        conn.close()

class Comment():

    # def __init__(self, autocommit=True):
    #     self.conn = psycopg2.connect(database="weigodb", user="postgres", password="123456", host="localhost",
    #                                  port="5432")
    #     self.autocommit = autocommit
    #     self.cur = self.conn.cursor()

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
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql, parm)
        conn.commit()
        conn.close()

class Like():

    # def __init__(self, autocommit=True):
    #     self.conn = psycopg2.connect(database="weigodb", user="postgres", password="123456", host="localhost",
    #                                  port="5432")
    #     self.autocommit = autocommit
    #     self.cur = self.conn.cursor()

    def get_Like(self,sql='',parm=()):
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql,parm)
        self.result =  self.cur.fetchone()
        return self.result

    def add_Like(self,sql='',parm=()):
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql, parm)
        conn.commit()
        conn.close()

    def del_Like(self,sql='',parm=()):
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql, parm)
        conn.commit()
        conn.close()

class Relation():

    # def __init__(self, autocommit=True):
    #     self.conn = psycopg2.connect(database="weigodb", user="postgres", password="123456", host="localhost",
    #                                  port="5432")
    #     self.autocommit = autocommit
    #     self.cur = self.conn.cursor()

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
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql, parm)
        conn.commit()
        conn.close()

class Photo():

    # def __init__(self, autocommit=True):
    #     self.conn = psycopg2.connect(database="weigodb", user="postgres", password="123456", host="localhost",
    #                                  port="5432")
    #     self.autocommit = autocommit
    #     self.cur = self.conn.cursor()

    def get_Photo(self,sql='',parm=()):
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql,parm)
        self.result =  self.cur.fetchone()
        return self.result

    def set_Photo(self,sql='',parm=()):
        conn = connect_db()
        self.cur = conn.cursor()
        self.cur.execute(sql, parm)
        conn.commit()
        conn.close()