import sqlite3
import feedparser

def test():
    connection = sqlite3.connect('database.db')

    # Url de flux RSS
    url = ["http://www.audiodramax.com/feed",
           "https://valnuit.lepodcast.fr/rss",
           "http://radiofrance-podcast.net/podcast09/rss_14312.xml",
           "http://feeds.feedburner.com/salle101"]

    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    for urlFeed in url:
        news_feed = feedparser.parse(urlFeed)

        print("Items keys", news_feed.entries[0].keys(), "\n")
        for entry in news_feed.entries:
            print(f"{entry.title} --> {entry.link}\n{entry.summary}\n")

        for entry in news_feed.entries:
            cur.execute("INSERT INTO posts (feed, title, link, date, content) VALUES (?, ?, ?, ?, ?)",
                        (news_feed.feed.title, entry.title, entry.link, entry.updated, entry.summary)
                        )

    connection.commit()
    connection.close()