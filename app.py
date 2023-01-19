from flask import Flask, render_template, request, jsonify
import logging
from utils import *

app = Flask(__name__)
logging.basicConfig(filename="logs/api.log", level=logging.INFO, filemode="w",
                    format="%(asctime)s [%(levelname)s] %(message)s")


@app.route('/')
def main_page():
    posts = get_posts_all()
    logging.info("Я перешел на главную страницу")
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def podrobnee(post_id):
    posts = get_post_by_id(post_id)
    comments = get_comments_by_post_id(post_id)
    logging.info(f"Запрос /post/{post_id}")
    return render_template('post.html', comments=comments, posts=posts)


@app.route('/search')
def search_page():
    s = request.args.get("s")
    posts = search_for_posts(s)
    logging.info(f"Запрос /search")
    return render_template("search.html", posts=posts)


@app.route('/users/<username>')
def profil(username):
    user = get_posts_by_user(username)
    poster_name = user[0]['poster_name']
    logging.info(f"Запрос /users")
    return render_template("user-feed.html", user=user, poster_name=poster_name)


@app.errorhandler(404)  # для вывода ошибки 404/ просто вставь точно такую же функцию
def page_not_found(e):
    return f"Упс произошла ошибка 404"


# Обработка ошибки 500
@app.errorhandler(500)  # для вывода ошибуи 500/ просто вставь тоже самое
def page_not_found(e):
    return f"Упс произошла ошибка 500"


@app.route('/api/posts')
def everyone_post():
    everyone_post = get_posts_all()
    logging.info(f"Запрос /api/posts")
    return jsonify(everyone_post)


@app.route('/api/posts/<int:post_id>')
def one_post(post_id):
    list_for_one_post = []
    for i in get_post_by_id(post_id):
        list_for_one_post.append(i)
    logging.info(f"Запрос /api/posts/{post_id}")
    return jsonify(list_for_one_post)


app.run()
