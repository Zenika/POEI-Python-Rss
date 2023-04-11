# POEI-Python-Rss

#### The final goal of this project is to retrieve rss feeds and display the contained articles in a flask web application with a Swagger interface for a user who subscribed to it.

### Requierements :
click==8.1.3<br>
feedparser==6.0.10<br>
Flask==2.2.3<br>
itsdangerous==2.1.2<br>
Jinja2==3.1.2<br>
MarkupSafe==2.1.2<br>
sgmllib3k==1.0.0<br>
Werkzeug==2.2.3<br>

### Evolution :

03/04/2023 : <br>
First iteration of the project. <br>
Installation of the "Feedparser" lib and creation of a python script that retrieves some information from a rss feed link.<br>

07/04/2023 : <br>
Add some information retrieved by the python script.<br>
Some problem using flask. Even if installed, the script seems not to find it and can't use it. <br>

11/04/2023 : <br>
Problem with flask was related to the script file naming (don't name it "flask.py")<br>
Create a flask web application that display "hello world!" on http://127.0.0.1:5000/. <br>
Follow flask tuto to create a web app that display some post (with titles, timstamp, link and content) from a local db initialized by a init_db python script<br>
Db is initialized with values retrieved from a RSS feed url.<br>
