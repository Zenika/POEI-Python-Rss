import os
import sqlite3
import init_db
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

if os.path.isfile("./database.db"):
    dbCreate = input("You already got a database.db file\n"
                     "Do you want to create a new database.db from actual RssFeeds file ? (Y/N)")
    while (dbCreate != 'y') and (dbCreate != 'Y') and (dbCreate != 'n') and (dbCreate != 'N'):
        dbCreate = input("Answer with Y (for yes) or N (for no)\n"
                         "Create database from RssFeeds file ? (Y/N)")
    if dbCreate == 'y' or dbCreate == 'Y':
        init_db.init()
else:
    print(
        "You have no database.db file\nOne will be generated from url in the RssFeeds file, it can take a few minutes")
    go = input("Continue ? (Y/N)")
    while (go != 'y') and (go != 'Y') and (go != 'n') and (go != 'N'):
        go = input("Answer with Y (for yes) or N (for no)\n"
                   "Continue ? (Y/N)")
    if go == 'y' or go == 'Y':
        init_db.init()
    else:
        quit()


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_feeds():
    conn = get_db_connection()
    feeds = conn.execute('SELECT * FROM posts where feed is not null group by feed order by lower(feed) asc').fetchall()
    conn.close()
    if feeds is None:
        abort(404)
    return feeds

def get_posts():
    conn = get_db_connection()
    feeds = conn.execute('SELECT * FROM posts order by lower(title) asc').fetchall()
    conn.close()
    if feeds is None:
        abort(404)
    return feeds

def get_feed(post_feed):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE feed = ? order by lower(title) asc', (post_feed,)).fetchall()
    conn.close()
    if post is None:
        abort(404)
    return post


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


@app.route('/')
def index():
    feeds = get_feeds()
    posts = get_posts()
    return render_template('index.html', feeds=feeds, posts=posts)


@app.route('/<string:post_feed>')
def posts(post_feed):
    posts = get_feed(post_feed)
    return render_template('feed.html', posts=posts, feed=post_feed)


@app.route('/<string:post_feed>/<int:post_id>')
def post(post_feed, post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')
