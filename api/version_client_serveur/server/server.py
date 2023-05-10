import os
import sqlite3
import init_db
from flask import Flask, render_template, request, url_for, flash, redirect, jsonify
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

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = dict_factory
    return conn

def get_feeds():
    conn = get_db_connection()
    feeds = conn.execute('SELECT DISTINCT(feed) FROM posts WHERE feed IS NOT NULL AND feed <> "" ORDER BY feed asc').fetchall()
    conn.close()
    if feeds is None:
        abort(404)
    print(feeds)
    return feeds

def get_all_posts():
    conn = get_db_connection()
    feeds = conn.execute('SELECT * FROM posts order by date desc').fetchall()
    conn.close()
    if feeds is None:
        return []
    return feeds

def get_feed(feed_name):
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts WHERE feed = ? order by date desc', (feed_name,)).fetchall()
    conn.close()
    if posts is None:
        abort(404)
    return posts


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


app = Flask(__name__)


@app.route('/feeds')
def feeds():
    feeds = get_feeds()
    return jsonify(feeds)

@app.route('/feeds/<string:feed_name>')
def feed_posts(feed_name):
    posts = get_feed(feed_name)
    return jsonify(posts)

@app.route('/feeds/post/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return jsonify(post)

@app.route('/posts')
def all_posts():
    posts = get_all_posts()
    return jsonify(posts)