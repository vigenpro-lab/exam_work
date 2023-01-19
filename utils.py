import json


def get_posts_all():
    with open("data/posts.json", "r",
              encoding="utf-8") as file_json:  # открываем джисон файл, читаем, добавляем encoding="utf-8" чтоб вывоодил адекватный вывод
        posts = json.load(file_json)  # превращаем в текст
        return posts  # возвращаем джейсон файл


def get_comments_all():
    with open("data/comments.json", "r",
              encoding="utf-8") as file_json:  # открываем джисон файл, читаем, добавляем encoding="utf-8" чтоб вывоодил адекватный вывод
        comment = json.load(file_json)  # превращаем в текст
        return comment  # возвращаем джейсон файл


def get_posts_by_user(user_name):
    try:
        post = []
        all_post = get_posts_all()
        for i in all_post:
            if user_name == i["poster_name"]:
                post.append(i)
        return post
    except ValueError:
        return []


def get_comments_by_post_id(post_id):
    try:
        comment = []
        all_comment = get_comments_all()
        for i in all_comment:
            if post_id == i['post_id']:
                comment.append(i)
        return comment
    except ValueError:
        return []


def search_for_posts(query):
    try:
        contents = []
        all_posts = get_posts_all()
        for i in all_posts:
            if query.lower() in i["content"].lower():
                contents.append(i)
        return contents
    except ValueError:
        return []


def get_post_by_pk(pk):
    try:
        one_post = get_posts_all()
        for i in one_post:
            if pk == i["pk"]:
                return i
    except ValueError:
        return []


def get_post_by_id(post_id):
    posts_pk = []
    posts = get_posts_all()
    for post in posts:
        if post_id == post['pk']:
            posts_pk.append(post)
    return posts_pk

