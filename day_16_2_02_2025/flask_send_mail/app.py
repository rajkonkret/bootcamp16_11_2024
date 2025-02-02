import os
from threading import Thread

from flask import Flask, render_template
from dotenv import load_dotenv
from flask_mail import Mail, Message

#  pip install python-dotenv
load_dotenv()
app = Flask(__name__)
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config["FLASKY_MAIL_SUBJECT"] = '[Apka]'
app.config["FLASKY_MAIL_SENDER"] = os.getenv('MAIL_USERNAME')

mail = Mail(app)


def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)


@app.route("/")
def index():
    send_mail("rajkonkret660@gmail.com", "Nowy User", "mail/new_user", user="Admin")
    return '<h1>Hello</h1>'


def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    # mail.send(msg)
    thr = Thread(target=send_async_mail, args=[app, msg])
    thr.start()
    return thr


if __name__ == '__main__':
    app.run(debug=True)
