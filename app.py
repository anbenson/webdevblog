from flask import Flask, render_template
app = Flask(__name__)

SET_DEBUG = True

@app.route("/")
def home():
  return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
  return render_template("error404.html"), 404

if __name__ == "__main__":
  app.run(debug=SET_DEBUG)