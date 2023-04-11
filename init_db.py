import sqlite3
import feedparser

connection = sqlite3.connect('database.db')

# Url de flux RSS
url = "https://valnuit.lepodcast.fr/rss"
# Création d'une instance
news_feed = feedparser.parse(url)

print("Items keys", news_feed.entries[0].keys(), "\n")
for entry in news_feed.entries:
    print(f"{entry.title} --> {entry.link}\n{entry.summary}\n")


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

for entry in news_feed.entries:
        cur.execute("INSERT INTO posts (title, link, date, content) VALUES (?, ?, ?, ?)",
                    (entry.title, entry.link, entry.updated, entry.summary)
                    )

connection.commit()
connection.close()
