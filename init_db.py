import sqlite3
import feedparser


def init():
    connection = sqlite3.connect('database.db')

    file1 = open('RssFeeds', 'r')
    url = file1.readlines()

    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    print("Creating Database")

    for urlFeed in url:
        try:
            print("Adding " + urlFeed, end='')
            news_feed = feedparser.parse(urlFeed)

            print("Items keys : ", news_feed.entries[0].keys())

            for entry in news_feed.entries:
                cur.execute("INSERT INTO posts (feed, title, link, date, content) VALUES (?, ?, ?, ?, ?)",
                            (news_feed.feed.title, entry.title, entry.link, entry.updated, entry.summary)
                            )
            print('\033[92m' + "Done" + '\033[0m')
        except:
            print('\033[91m' + "Fail" + '\033[0m')

    print("Database Created")

    connection.commit()
    connection.close()
