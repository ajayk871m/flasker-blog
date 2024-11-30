from flask import Flask, render_template, flash
from forms import NamerForm, Userform
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# app instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config["SECRET_KEY"] = "Asnhcieyueaois748ycabyhiweyr93wuioewcadj"

# creating database
db = SQLAlchemy(app)

# model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name 



# app routes
@app.route("/")
def home_page():
    stuff = "this is some <u>safe scripting</u> text."
    book = ["one", "two", "three", "readdhead"]
    return render_template("index.html", stuff=stuff, book=book)


@app.route("/user/<name>")
def user_page(name):
    return render_template("user.html", name=name)


@app.route("/name", methods=["GET", "POST"])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("Form submitted Successfully!!")
    return render_template("name.html", name=name, form=form)


@app.route("/user/add", methods=["GET", "POST"])
def add_user():
    name = None
    form = Userform()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        flash("User created successfully!!")
    
    our_users = Users.query.order_by(Users.added)
    return render_template("add_user.html", form=form, name=name, our_users=our_users)


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
