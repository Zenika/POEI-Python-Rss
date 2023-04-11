#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import feedparser

# Url de flux RSS
url = "https://valnuit.lepodcast.fr/rss"

# Création d'une instance
news_feed = feedparser.parse(url)

# Propriétés du flux
print("Feed keys : ", news_feed.feed.keys())

# Date de publication du flux
print("Date :", news_feed.feed.updated)

# Titre du flux
print("Feed Title : ", news_feed.feed.title)

# Sous-titre du flux
print("Feed Subtitle : ", news_feed.feed.subtitle)

# Lien du flux
print("Feed Link : ", news_feed.feed.link, "\n")

# Propriétés de chaque item du flux
print("Items keys", news_feed.entries[0].keys(), "\n")

for entry in news_feed.entries:
    print(f"{entry.title} --> {entry.link}\n{entry.summary}\n")

# Récupération du dernier feed (dernier bulletin CERT-FR)

for i in range(0, len(news_feed.entries)):
    if i == (len(news_feed.entries) - 1):
        print("Alert: {} \nLink: {}".format(news_feed.entries[0]['title'], news_feed.entries[0]['id']))
