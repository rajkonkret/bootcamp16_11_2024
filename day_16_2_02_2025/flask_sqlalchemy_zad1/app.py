from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    discount = db.Column(db.Integer)
    active = db.Column(db.Boolean)

@app.route("/")
def index():
    db.create_all()
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True)
