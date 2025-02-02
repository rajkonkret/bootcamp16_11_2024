from flask import Flask, render_template, url_for, request, flash, g, redirect, session
from flask_sqlalchemy import SQLAlchemy

import random
import string
import hashlib
import binascii

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from urllib.parse import urlparse, urljoin

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'First, please log in'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.Text)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))

    def __repr__(self):
        return f"(User: {self.name})"


def get_hashed_password(password):
    os_urandom_static = b'\xee\x8b\x9c\xe6n\x96\xa9\xf5@\x99\x9c\xf3\xbf\xf1\x03\x86sr\x05\xcf\xa7\xac\xcf\xb2H\xfe\x7f\x10\x14\x9f%5\xde\xe5\xbd\xaef\x9d\xcd\xf4\xc9Be\xf9\x04\xf9\x1c}\xf9\x8a|\xe4\x92\xe1\xdb\xff~R\x0e\xb1'
    salt = hashlib.sha256(os_urandom_static).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf=8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf=8'), salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


@login_manager.user_loader
def load_user(id):
    return User.query.filter(User.id == id).first()


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url


class LoginForm(FlaskForm):
    name = StringField("User name")
    password = PasswordField("Password")
    remember = BooleanField("Remember me")


@app.route("/init")
def init():
    db.create_all()

    admin = User.query.filter(User.name == 'admin').first()
    if admin == None:
        admin = User(id=1, name='admin', password=get_hashed_password("Passw0rd"),
                     first_name="Radek", last_name="Kowalski")
        db.session.add(admin)
        db.session.commit()

    return '<h1>Initial configuration done!</h1>'


@app.route("/")
def index():
    return "<h>Hello!</h1>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        print(form.name.data, form.password.data)
        user = User.query.filter(User.name == form.name.data).first()
        if user != None and verify_password(user.password, form.password.data):
            login_user(user)

            next = request.args.get('next')
            if next and is_safe_url(next):
                return redirect(next)
            else:
                return "<h1>You are authenticated!</h1>"

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return '<h1>You are logged out</h1>'


@app.route("/docs")
@login_required
def docs():
    return f"<h1>You have access to protected docs. you are {current_user.name}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
