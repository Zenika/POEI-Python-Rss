import sqlite3
from datetime import datetime
from os import abort


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_posts():
    conn = get_db_connection()
    feeds = conn.execute('SELECT * FROM posts order by lower(title) asc').fetchall()
    conn.close()
    if feeds is None:
        abort(404)
    return feeds

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


posts = get_posts()

test = "{";
for i in posts:
    test = test + "\"" + str(i[0]) + "\": {\"feed\": \"" + i[1] + "\",\"title\": \"" + i[2] + "\",\"date\": \"" + i[3] + "\",\"link\": \"" + i[4] + "\"},"
test = test[:-1] + "}"

# Données sous-jacentes à l'API
PEOPLE = test


# Création d'un handler read (GET) pour les données people
def read():
    # Création de la liste de personnes à partir de nos données
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
