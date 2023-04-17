DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    feed TEXT NOT NULL,
    title TEXT NOT NULL,
    date timestamp NOT NULL,
    link TEXT NOT NULL,
    content TEXT NOT NULL
);
