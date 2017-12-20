from view.users import *
from view.messages import *
from view.like import *
from view.comments import *
from view.friend import *
from view.follow import *
from view.postlist import *
from view.photo import *
from config import *


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.secret_key = '123'

    # login/register
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/login', 'login', index)
    app.add_url_rule('/logout', 'logout', logout)
    app.add_url_rule('/register', 'register', rgs)
    app.add_url_rule('/log', 'log', login, methods=['POST', 'GET'])
    app.add_url_rule('/rgs', 'rgs', register, methods=['POST', 'GET'])
    # post
    app.add_url_rule('/home/<host>', 'home', home, methods=['GET'])
    app.add_url_rule('/addpost/<host>', 'addPost', addPost, methods=['GET', 'POST'])
    app.add_url_rule('/delete/<postid>/<host>', 'deletePost', deletePost, methods=['GET', 'POST'])
    app.add_url_rule('/editpage/<postid>/<host>', 'editPage', editPage, methods=['GET'])
    app.add_url_rule('/editpost/<postid>/<host>', 'editPost', editPost, methods=['GET', 'POST'])
    # like
    app.add_url_rule('/like/<postid>/<host>', 'like', like, methods=['GET', 'POST'])
    # comment
    app.add_url_rule('/comment/<postid>/<host>', 'comment', comment, methods=['GET', 'POST'])
    app.add_url_rule('/addcomment/<postid>/<host>', 'addcomment', addComment, methods=['GET', 'POST'])
    app.add_url_rule('/delcomment/<postid>/<commid>/<host>', 'delcomment', delComment, methods=['GET', 'POST'])
    app.add_url_rule('/editcommpage/<commid>/<host>', 'editcommpage', editCommpage, methods=['GET', 'POST'])
    app.add_url_rule('/editcomment/<commid>/<host>', 'editcomment', editComment, methods=['GET', 'POST'])
    # friend
    app.add_url_rule('/friend/<host>', 'friend', friend, methods=['GET', 'POST'])
    app.add_url_rule('/searchfriend/<host>', 'searchfriend', searchFriend, methods=['GET', 'POST'])
    app.add_url_rule('/unfollow/<host>/<userid>', 'unfollow', unFollow, methods=['GET', 'POST'])
    # follow
    app.add_url_rule('/follow/<key>/<host>', 'follow', follow, methods=['GET', 'POST'])
    app.add_url_rule('/dofollow/<state>/<host>/<username>/<key>', 'dofollow', doFollow, methods=['GET', 'POST'])
    app.add_url_rule('/followlist/<host>', 'followlist', followList, methods=['GET', 'POST'])
    app.add_url_rule('/fanslist/<host>', 'fanslist', fansList, methods=['GET', 'POST'])
    # postlist
    app.add_url_rule('/postlist/<host>', 'postlist', postList, methods=['GET', 'POST'])
    app.add_url_rule('/postlistDel/<postid>/<host>', 'deletePostlist', deletePostlist, methods=['GET', 'POST'])
    app.add_url_rule('/postlistLike/<postid>/<host>', 'postlistLike', postlistLike, methods=['GET', 'POST'])
    # photo
    app.add_url_rule('/photopage/<host>', 'photopage', photoPage, methods=['GET', 'POST'])
    app.add_url_rule('/uploadphoto/<host>', 'uploadphoto', uploadPhoto, methods=['GET', 'POST'])

    return app

app = create_app('development')

# @app.errorhandler(404)
# def not_found(e):
#     return render_template("error.html")

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
