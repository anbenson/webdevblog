webdevblog
==================

A simple blog written in Python and Flask with a SQLite backend. Check it out at webdevblog.herokuapp.com, but note that since Heroku clears out local storage (including our SQLite database) a couple times a day, blog posts won't persist for very long.

This was written for the Fall 2014 edition of WebDevWeeks, a ScottyLabs event created to teach the CMU community about web development. Students in the server-side programming session wrote a blog very similar to this one. The starter code and the handouts for the event can be found in the 'resources' folder in the repository.

Steps to run:
- git clone git@github.com:anbenson/webdevblog.git
- cd webdevblog
- pip install -r requirements.txt
- python main.py
- go to localhost:5000

(I use "python main.py" instead of "foreman run" because foreman does weird things on my computer.)
