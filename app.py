from flask import Flask, render_template

# from flask_sqlalchemy import SQLAlchemy

# app instance
app = Flask(__name__)

# safe: just compiles html tags


# app routes
@app.route("/")
def home_page():
    stuff = "this is some <u>safe scripting</u> text."
    book = ['one', 'two', 'three', 'readdhead']
    return render_template("index.html", stuff=stuff, book=book)


@app.route("/user/<name>")
def user_page(name):
    return render_template("user.html", name=name)


# custom error pages
# 1. invalid url page (C E P)
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error/404.html", 404)


# 2. internal server error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("error/500.html", 500)


# run script
if __name__ == "__main__":
    app.run(debug=True, port=8000)
