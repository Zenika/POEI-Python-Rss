from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


def get_feeds():
    feeds = [
        {
            "feed": "1000 idées de culture générale"
        },
        {
            "feed": "ABSOLUMENT TOUT"
        },
        {
            "feed": "Abstruse Goose"
        },
        {
            "feed": "xkcd"
        },
    ]
    if feeds is None:
        abort(404)
    return feeds

def get_posts():
    feeds = [
          {
            "content": "<p><img class=\"quicklook\" height=\"240\" src=\"https://taoofmac.com/thumb/links/2023/05/04/2331/640,480/1sEsV5RM2Em15yfYGwLo6fxHqWo=/large.jpg\" style=\"height: auto !important;\" width=\"320\" /></p>\n<p class=\"lead\">Like I wrote <a href=\"https://taoofmac.com/space/blog/2023/03/18/0140\" rel=\"next\">a few weeks back</a>:</p>\n<blockquote>\n<p><em>like this past couple of weeks&#8217; spate of news around <code>llama.cpp</code> proves, there is a lot of low hanging fruit where it regards optimizing running the models, and at multiple levels</em></p>\n</blockquote>\n<p>And, apparently, I was right. And I&#8217;m likely also right on tailored models and the value proposition of running them on-premises, or, at the very least, without needing to rely on a gigantic corporation.</p>\n<p>Whether this is really a leaked Google memo or not (and I suspect it is), I&#8217;m positive about two things: the genie has escaped the bottle, and nobody has a moat, yes.</p>\n<p>But, also, nobody has that big of a treasure inside their castle either (the industry keeps trying to create walled gardens of various kinds&#8230;).</p>\n\n<br />",
            "date": "2023-05-04T22:31:21+00:00",
            "feed": "Tao of Mac",
            "id": 2841,
            "link": "https://taoofmac.com/space/links/2023/05/04/2331",
            "title": "We Have No Moat, And Neither Does OpenAI"
          },
          {
            "content": "<p>recent victims:<br /><a href=\"https://belong.io/\" title=\"BELONG\">BELONG</a> and <a href=\"https://johnjohnston.info/blog/re-tdc4124-ds106-is-today-the-day-it-all-breaks/\">Daily Create</a></p>\n\n<p><a href=\"https://brid.gy/publish/mastodon\"></a></p>",
            "date": "2023-05-03T17:39:01+00:00",
            "feed": "i.webthings.hub",
            "id": 3254,
            "link": "https://iwebthings.joejenett.com/bluemuskr-continues-breaking-the-web/",
            "title": "blueMuskr continues breaking the web"
          },
          {
            "content": "<p><a href=\"https://eycndy.com/\" title=\"Eyecandy - Visual Technique Library\">Eyecandy</a><br />[<a href=\"https://pinboard.in/u:locuna\" title=\"locuna\">locuna</a>]</p>\n\n<p><a href=\"https://brid.gy/publish/mastodon\"></a></p>",
            "date": "2023-05-03T14:35:28+00:00",
            "feed": "i.webthings.hub",
            "id": 3255,
            "link": "https://iwebthings.joejenett.com/the-visual-technique-library-for-visual-technique-lovers/",
            "title": "‘the visual technique library for visual technique lovers’"
          },
    ]
    if feeds is None:
        abort(404)
    return feeds

def get_feed(post_feed):
    post = [
        {
            "content": "My new book, How To: Absurd Scientific Advice for Common Real-World Problems, comes out in a week! You can preorder it now on Amazon, Barnes &#38; Noble, IndieBound, and Apple Books. Here&#8217;s an excerpt from the How To chapter on file transfers. Chapter 19: How to Send a File Sending large data files can be difficult. Modern software systems have moved &#8230; <p class=\"link-more\"><a class=\"more-link\" href=\"https://blog.xkcd.com/2019/08/26/how-to-send-a-file/\">Continue reading<span class=\"screen-reader-text\"> \"How to Send a&#160;File\"</span></a></p>",
            "date": "Mon, 26 Aug 2019 13:41:54 +0000",
            "feed": "xkcd",
            "id": 1011,
            "link": "https://blog.xkcd.com/2019/08/26/how-to-send-a-file/",
            "title": "How to Send a File"
        },
        {
            "content": "I&#8217;m going to be at Comic-Con in San Diego this week! I&#8217;ll be appearing on panels with some really neat people for conversations about science, comics, and writing, and talking about my new book, How To: Absurd Scientific Advice for Common Real-World Problems. Here&#8217;s my panel/event schedule. If you&#8217;re attending, come see me there! THURSDAY &#8230; <p class=\"link-more\"><a class=\"more-link\" href=\"https://blog.xkcd.com/2019/07/15/san-diego-comic-con/\">Continue reading<span class=\"screen-reader-text\"> \"San Diego Comic-Con\"</span></a></p>",
            "date": "Mon, 15 Jul 2019 14:10:56 +0000",
            "feed": "xkcd",
            "id": 1016,
            "link": "https://blog.xkcd.com/2019/07/15/san-diego-comic-con/",
            "title": "San Diego Comic-Con"
        },
        {
            "content": "My new book, How To: Absurd Scientific Advice for Common Real-World Problems, is coming out on September 3rd, and I&#8217;ll be going on a short book tour! (Full information for each stop is included at the bottom of this post.) How to invite me to your town Don&#8217;t see your city on the list? You can &#8230; <p class=\"link-more\"><a class=\"more-link\" href=\"https://blog.xkcd.com/2019/06/10/book-tour-announcement/\">Continue reading<span class=\"screen-reader-text\"> \"Book tour announcement!\"</span></a></p>",
            "date": "Mon, 10 Jun 2019 16:35:56 +0000",
            "feed": "xkcd",
            "id": 1017,
            "link": "https://blog.xkcd.com/2019/06/10/book-tour-announcement/",
            "title": "Book tour announcement!"
        },
    ]
    if post is None:
        abort(404)
    return post


def get_post(post_id):
    post = {
        "content": "My new book, How To: Absurd Scientific Advice for Common Real-World Problems, is coming out on September 3rd, and I&#8217;ll be going on a short book tour! (Full information for each stop is included at the bottom of this post.) How to invite me to your town Don&#8217;t see your city on the list? You can &#8230; <p class=\"link-more\"><a class=\"more-link\" href=\"https://blog.xkcd.com/2019/06/10/book-tour-announcement/\">Continue reading<span class=\"screen-reader-text\"> \"Book tour announcement!\"</span></a></p>",
        "date": "Mon, 10 Jun 2019 16:35:56 +0000",
        "feed": "xkcd",
        "id": 1017,
        "link": "https://blog.xkcd.com/2019/06/10/book-tour-announcement/",
        "title": "Book tour announcement!"
    }
    if post is None:
        abort(404)
    return post


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
