import unittest
from flask import current_app,session
from main.models import *
from weigo import create_app

app = create_app('testing')

class WeigoTestCase(unittest.TestCase):


    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        self.conn = connect_db()
        self.client = app.test_client()


    def tearDown(self):
        self.conn.commit()
        self.conn.close()


    def test_app_exits(self):
        self.assertFalse(current_app is None)


    def test_a_register(self):

        #register
        response = self.client.post('/rgs',data={
            'username' : 'test',
            'password' : '111111',
            'repassword' : '111111'
        })
        data = response.get_data(as_text=True)
        self.assertTrue(response.status_code == 200)
        response = self.client.post('/rgs', data={
            'username': 'test0',
            'password': '111111',
            'repassword': '111111'
        })
        data = response.get_data(as_text=True)
        self.assertTrue(response.status_code == 200)

        #input a exist name
        response = self.client.post('/rgs', data={
            'username': 'test',
            'password': '111111',
            'repassword': '111111'
        })
        data = response.get_data(as_text=True)
        self.assertTrue('user is already exist!' in data)

        #password is not same
        response = self.client.post('/rgs', data={
            'username': 'test1',
            'password': '111111',
            'repassword': '111'
        })
        data = response.get_data(as_text=True)
        self.assertTrue('password is not same!' in data)

        # password is less than six
        response = self.client.post('/rgs', data={
            'username': 'test1',
            'password': '111',
            'repassword': '111111'
        })
        data = response.get_data(as_text=True)
        self.assertTrue('length of password should be more than six!' in data)


    def test_b_login(self):

        response = self.client.post('/log',data={
            'username' : 'test',
            'password' : '111111'
        },follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('Hello,test' in data)

        #test logout method
        response = self.client.get('/logout', follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('Log in' in data)


    def test_c_home(self):

        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'
        response = self.client.get('/home/%s' % 'test',follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('Hello,test' in data)


    def test_d_add_post(self):

        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'
        #add a post
        response = self.client.post('/addpost/%s' % 'test', data={
            'postbox' : 'post1'
        },follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('post1' in data)

        #add nothing
        response = self.client.post('/addpost/%s' % 'test', data={
            'postbox': ''
        }, follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('You can not send nothing!' in data)


    def test_e_edit_page(self):

        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'
        post = Post()
        parm = ('post1',)
        result = post.get_Post('SELECT * FROM message WHERE message_info = %s ORDER BY message_id DESC ;', parm)

        response = self.client.get('/editpage/%s/%s' % (result[0],'test'),
                                   follow_redirects=True)
        data = response.get_data(as_text=True)
        # print(data)
        self.assertTrue('Update post:' in data)


    def test_f_postlist(self):

        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'

        response = self.client.get('/postlist/%s' % 'test',
                                   follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('post1' in data)


    def test_g_edit_post(self):

        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'
        post = Post()
        parm = ('post1',)
        result = post.get_Post('SELECT * FROM message WHERE message_info = %s ORDER BY message_id DESC ;', parm)

        #edit post
        response = self.client.post('/editpost/%s/%s' % (result[0],'test'),data={
                                        'posteditbox' : 'post111'
                                    }, follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('post111' in data)

        #input nothing
        response = self.client.post('/editpost/%s/%s' % (result[0], 'test'), data={
            'posteditbox' : ''
        }, follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('you left nothing' in data)


    def test_h_like(self):

        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'
        post = Post()
        parm = ('post111',)
        result = post.get_Post('SELECT * FROM message WHERE message_info = %s ORDER BY message_id DESC ;', parm)

        #add like
        self.client.post('/like/%s/%s' % (result[0],'test'),follow_redirects=True)
        post = Post()
        parm = ('post111',)
        result = post.get_Post('SELECT * FROM message WHERE message_info = %s ORDER BY message_id DESC ;', parm)
        self.assertEqual(result[4], 1)

        #cancel like
        self.client.post('/like/%s/%s' % (result[0], 'test'),follow_redirects=True)
        post = Post()
        parm = ('post111',)
        result = post.get_Post('SELECT * FROM message WHERE message_info = %s ORDER BY message_id DESC ;', parm)
        self.assertEqual(result[4], 0)

        #others add like
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test0'
        self.client.post('/like/%s/%s' % (result[0], 'test0'),follow_redirects=True)
        post = Post()
        parm = ('post111',)
        result = post.get_Post('SELECT * FROM message WHERE message_info = %s ORDER BY message_id DESC ;', parm)
        self.assertEqual(result[4], 1)


    def test_i_comment_page(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'
        post = Post()
        parm = ('post111',)
        result = post.get_Post('SELECT * FROM message WHERE message_info = %s ORDER BY message_id DESC ;', parm)
        response = self.client.post('/comment/%s/%s' % (result[0], 'test'),
                        follow_redirects=True)
        data = response.get_data(as_text=True)
        # print(data)
        self.assertTrue('Comments for:' in data)


    def test_j_add_comment(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'
        # add a comment
        post = Post()
        parm = ('post111',)
        result = post.get_Post('SELECT * FROM message WHERE message_info = %s ORDER BY message_id DESC ;', parm)
        response = self.client.post('/addcomment/%s/%s' % (result[0], 'test'), data={
            'commbox': 'hello'
        }, follow_redirects=True)
        data = response.get_data(as_text=True)
        # print(data)
        self.assertTrue('hello' in data)

        # add nothing
        response = self.client.post('/addcomment/%s/%s' % (result[0], 'test'), data={
            'commbox': ''
        }, follow_redirects=True)
        data = response.get_data(as_text=True)
        # print(data)
        self.assertTrue('You left nothing!' in data)

        #others add a comment
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test0'
        post = Post()
        parm = ('post111',)
        result = post.get_Post('SELECT * FROM message WHERE message_info = %s ORDER BY message_id DESC ;', parm)
        response = self.client.post('/addcomment/%s/%s' % (result[0], 'test0'), data={
            'commbox': 'hi,test'
        }, follow_redirects=True)
        data = response.get_data(as_text=True)
        # print(data)
        self.assertTrue('hi,test' in data)


    def test_k_comment_edit_page(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'

        comm = Comment()
        parm = ('hello',)
        result = comm.get_Comment('SELECT * FROM comment WHERE comment_info = %s ORDER BY comment_id DESC ;', parm)
        response = self.client.get('/editcommpage/%s/%s' % (result[0],'test'),
                                   follow_redirects=True)
        data = response.get_data(as_text=True)
        # print(data)
        self.assertTrue('Update comment:' in data)


    def test_l_edit_comment(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'
        comm = Comment()
        parm = ('hello',)
        result = comm.get_Comment('SELECT * FROM comment WHERE comment_info = %s ORDER BY comment_id DESC ;', parm)
        # edit comment
        response = self.client.post('/editcomment/%s/%s' % (result[0], 'test'), data={
            'commeditbox': 'hello,test'
        }, follow_redirects=True)
        data = response.get_data(as_text=True)
        # print(data)
        self.assertTrue('hello,test' in data)

        # input nothing
        response = self.client.post('/editcomment/%s/%s' % (result[0], 'test'), data={
            'commeditbox': ''
        }, follow_redirects=True)
        data = response.get_data(as_text=True)
        # print(data)
        self.assertTrue('you left nothing' in data)


    def test_m_delete_comment(self):

        # delete post
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'

        # get postid
        post = Post()
        parm = ('post111',)
        result = post.get_Post('SELECT * FROM message WHERE message_info = %s ORDER BY message_id DESC ;', parm)

        #get commentid
        comm = Comment()
        parm = ('hello,test',)
        result1 = comm.get_Comment('SELECT * FROM comment WHERE comment_info = %s ORDER BY comment_id DESC ;', parm)
        response = self.client.post('/delcomment/%s/%s/%s' % (result[0],result1[0],'test'),
                                    follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('hello,test' not in data)

        #delete post
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test0'

        # get postid
        post = Post()
        parm = ('post111',)
        result2 = post.get_Post('SELECT * FROM message WHERE message_info = %s ORDER BY message_id DESC ;', parm)

        # get commentid
        comm = Comment()
        parm = ('hi,test',)
        result3 = comm.get_Comment('SELECT * FROM comment WHERE comment_info = %s ORDER BY comment_id DESC ;', parm)
        response = self.client.post('/delcomment/%s/%s/%s' % (result2[0],result3[0],'test0'),
                                    follow_redirects=True)
        data = response.get_data(as_text=True)
        # print(data)
        self.assertTrue('hi,test' not in data)


    def test_n_friend_page(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'
        response = self.client.get('/friend/%s' % 'test',follow_redirects=True)
        data = response.get_data(as_text=True)
        # print(data)
        self.assertTrue('You haven not been following anyone yet.Go and find friends ↑↑↑' in data)


    def test_o_unfollow_friend(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'

        # follow a friend
        response = self.client.post('/dofollow/%s/%s/%s/%s' % ('FOLLOW', 'test', 'test0', 'te'),
                                    follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('test' in data)

        # friend page list the users you follow
        response = self.client.get('/friend/%s' % 'test', follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('test0' in data)

        # unfollow a friend
        users = User()
        parm = ('test0',)
        result = users.get_User('SELECT * FROM users WHERE user_name = %s ORDER BY user_id DESC ;', parm)
        response = self.client.post('/unfollow/%s/%s' % ('test',result[0]),
                                    follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('test0' not in data)


    def test_p_search_friend(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'
        # search friend
        response = self.client.post('/searchfriend/%s' % 'test', data={
            'searchfriend': 'te'
        }, follow_redirects=True)
        data = response.get_data(as_text=True)
        # print(data)
        self.assertTrue('test' in data)

        # search a not exist friend
        response = self.client.post('/searchfriend/%s' % 'test', data={
            'searchfriend': 'aaa'
        }, follow_redirects=True)
        data = response.get_data(as_text=True)
        # print(data)
        self.assertTrue('user is not exist!' in data)


    def test_q_dofollow_friend(self):

        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'

        #follow a friend
        response = self.client.post('/dofollow/%s/%s/%s/%s' % ('FOLLOW','test','test0','te'),
                                    follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('test' in data)

        #unfollow a friend
        response = self.client.post('/dofollow/%s/%s/%s/%s' % ('UNFOLLOW', 'test', 'test0', 'te'),
                                    follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('test' in data)

        # follow youself
        response = self.client.post('/dofollow/%s/%s/%s/%s' % ('FOLLOW', 'test', 'test', 'te'),
                                    follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('you can not follow yourself' in data)


    def test_r_followlist_fanslist(self):

        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'

        # follow a friend
        response = self.client.post('/dofollow/%s/%s/%s/%s' % ('FOLLOW', 'test', 'test0', 'te'),
                                    follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('test' in data)

        #test followlist
        response = self.client.get('/followlist/%s' % 'test',
                                   follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('test0' in data)

        #test fanslist
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test0'
        response = self.client.get('/fanslist/%s' % 'test0',
                                   follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('test' in data)

        # unfollow a friend
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'
        response = self.client.post('/dofollow/%s/%s/%s/%s' % ('UNFOLLOW', 'test', 'test0', 'te'),
                                    follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('test' in data)


    def test_s_delete_post(self):

        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'test'
        post = Post()
        parm = ('post111',)
        result = post.get_Post('SELECT * FROM message WHERE message_info = %s;', parm)

        # delete post
        response = self.client.post('/delete/%s/%s' % (result[0], 'test'),
                                    follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('post111' not in data)


    def test_t_index(self):

        response = self.client.get('/',follow_redirects=True)
        data = response.get_data(as_text=True)
        # print(data)
        self.assertTrue('Log in' in data)


    def test_u_rgs(self):

        response = self.client.get('/register',follow_redirects=True)
        data = response.get_data(as_text=True)
        # print(data)
        self.assertTrue('Register' in data)


if __name__ == '__main__':
    unittest.main()