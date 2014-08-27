webdevblog-example
==================

The example webdevblog for the server-side programming session for ScottyLabs' WebDevWeeks.

This repo is NOT for students in the WebDevWeeks session - there is a separate repo for that, and we'll probably have a zip file for you to download in a separate location.

This repo, in addition to the filled out files for WebDevWeeks, includes files for Heroku, like the Procfile.

You can find this website hosted at webdevblog.herokuapp.com. Beware that since this blog uses SQLite, which is stored locally, and because Heroku likes to clear out local storage around once a day, blog posts won't persist for very long.

Steps to run:
- git clone git@github.com:anbenson/webdevblog-example.git
- cd webdevblog-example
- pip install -r requirements.txt
- python main.py
- go to localhost:5000

(I use "python main.py" instead of "foreman run" because foreman does weird things on my computer.)
