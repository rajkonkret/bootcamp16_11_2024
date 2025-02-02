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

    def __repr__(self):
        return f"Vendor: {self.id}/{self.name}"


@app.route("/")
def index():
    db.create_all()

    # v1 = Vendor(id=1, name='Microsoft', discount=0, active=True)
    # db.session.add(v1)
    # db.session.commit()
    # v1 = Vendor(id=2, name='Samsung', discount=5, active=True)
    # db.session.add(v1)
    # db.session.commit()
    # v1 = Vendor( name='Samsung', discount=5, active=True) # automatyczny id
    # db.session.add(v1)
    # db.session.commit()
    # v1 = Vendor( name='Apple', discount=3, active=True) # automatyczny id
    # db.session.add(v1)
    # db.session.commit()

    # vendors = Vendor.query.all()
    # vendors = Vendor.query.filter(Vendor.discount > 0).all()
    # vendors = Vendor.query.filter(Vendor.discount > 3).all()
    # vendors = Vendor.query.filter(Vendor.name.like('%s%')).all()
    vendors = Vendor.query.filter(Vendor.name.like('%S%')).all()

    ret = ''
    for v in vendors:
        # ret += v.name + '<br>'
        ret += str(v) + '<br>'

    # return 'Hello'
    return f'Hello<br>{ret}'


if __name__ == '__main__':
    app.run(debug=True)
