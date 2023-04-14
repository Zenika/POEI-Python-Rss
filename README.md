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

## Usage

Make sure you have `python` and therefore `pip` installed.<br>

(You can edit this `init_db` file and replace the "url" variable value by the RSS feed url of your choice)

Run the flask web application with:
```sh
flask run
```

Then go on your favorite internet Browser to the url :<br>
http://127.0.0.1:5000/

## Author

👤 **Jason Sycz**

* Github: [@Bullfrog666](https://github.com/Bullfrog666)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/Zenika/POEI-Python-Rss/issues/). 

## Show your support

Give a ⭐️ if this project helped you!
