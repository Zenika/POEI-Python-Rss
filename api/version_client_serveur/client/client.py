import requests
import json
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from urllib.parse import quote

server_url = 'http://localhost:5000'

def get(path):
    response = requests.get(f"{server_url}{path}")
    if response.status_code == 404:
        abort(404)
    if response.status_code != 200:
        abort(500)
    return json.loads(response.content.decode('utf-8'))

def get_feeds():
    feeds = get(f"/feeds") 
    print(feeds)
    return feeds

def get_posts():
    posts = get(f"/posts") 
    print(posts)
    return posts

def get_feed(post_feed):
    return get(quote(f"/feeds/{post_feed}"))


def get_post(post_id):
    return get(f"/feeds/post/{post_id}")

app = Flask(__name__)


@app.route('/')
def home():
    feeds = get_feeds()
    posts = get_posts()
    return render_template('home.html', feeds=feeds, posts=posts)


@app.route('/<string:post_feed>')
def posts(post_feed):
    posts = get_feed(post_feed)
    return render_template('feed.html', posts=posts, feed=post_feed)


@app.route('/<string:post_feed>/<int:post_id>')
def post(post_feed, post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)
