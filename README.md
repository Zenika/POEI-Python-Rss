<h1 align="center">Welcome to POEI-Python-Rss 👋</h1>


> The final goal of this project is to retrieve RSS feeds and display the contained articles in a flask web application with a Swagger interface for a user who subscribed to it.

## Progression

- [x]  Application shows RSS stream on the terminal
- [x]  Application shows RSS stream in a web UI
- [ ]  Application has one scrapper component and one reader component
- [ ]  Application support multiple user profiles


- 03/04/2023 :<br>
First iteration of the project.
Installation of the "Feedparser" lib and creation of a python script that retrieves some information from a rss feed link.<br>

- 07/04/2023 :<br>
Add some information retrieved by the python script.
Some problem using flask. Even if installed, the script seems not to find it and can't use it.<br>

- 11/04/2023 :<br>
Problem with flask was related to the script file naming (don't name it "flask.py")
Create a flask web application that display "hello world!" on http://127.0.0.1:5000/. <br>
Followed flask tuto to create a web app that display some post (with titles, timstamp, link and content) from a local db initialized by a init_db python script
Db is initialized with values retrieved from an RSS feed url.<br>

- 12/04/2023 :<br>
  Project is migrated on Zenika GitHub organization.<br>README.md file upgraded.<br>CONTRIBUTING.md file added<br>

- 13/04/2023 :<br>
  init_db.py is now executed when flask run.<br>

- 14/04/2023 :<br>
  We can now have multiple rss feed in init_db.<br>Post content in html is now interpreted as html (not just a string).<br>

- 17/04/2023 :<br>
  Rss feed URLs are now read from a `RssFeeds` file.<br>Flask run will ask user if they want to generate the database.db.<br>Add a new page `feed`.<br>

- 19/04/23 :<br>
  Ordered feed and post by name.<br>Feed Filter by name.<br>

## Usage

Make sure you have `python` and therefore `pip` installed.<br>

Download all the python packages required.<br>You can do it from the requirements.txt file with `pip`:
```sh
pip install -r requirements.txt --use-pep517 --user
```
The --use-pep517 is required by sgmllib (a dependency of feedparser) and the --user is required by flask.<br>

Run the flask web application with:
```sh
flask run
```

We need a database.db file.<br>One is already in the project file to avoid you to generate it yourself, but you can edit the `Rssfeeds` file to add, replace or delete some Rss feed url and the app will then ask if you want to generate a new database.db file from the actual  `RssFeeds` file.

```sh
Do you want to create a new database.db from actual RssFeeds file ? (Y/N)
```

The generation can take a few minutes.

Then go on your favorite internet Browser to the url :<br>
http://127.0.0.1:5000/

## Author

👤 **Jason Sycz**

* Github: [@Bullfrog666](https://github.com/Bullfrog666)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/Zenika/POEI-Python-Rss/issues/). 

## Show your support

Give a ⭐️ if this project helped you!
