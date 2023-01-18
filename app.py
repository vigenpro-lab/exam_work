from flask import Flask, render_template, request
from utils import *

app = Flask(__name__)


@app.route('/')
def main_page():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def podrobnee(post_id):
    posts = get_post_by_id(post_id)
    comments = get_comments_by_post_id(post_id)
    return render_template('post.html', comments=comments, posts=posts)


@app.route('/search')
def search_page():
    s = request.args.get("s")
    posts = search_for_posts(s)
    return render_template("search.html", posts=posts)



@app.route('/users/<username>')
def profil(username):
    user = get_posts_by_user(username)
    return render_template("user-feed.html", user=user)


app.run()