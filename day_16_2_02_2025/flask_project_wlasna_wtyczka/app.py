from datetime import datetime

from flask import Flask
from wtyczka import MojaWtyczka

app = Flask(__name__)
moja_wtyczka = MojaWtyczka(app)


@app.route("/")
def index():
    time_now = datetime.now().strftime('%H:%M:%S')
    print(moja_wtyczka)  # <wtyczka.MojaWtyczka object at 0x000002690316FCB0>
    return f"Witaj w moje aplikacji {time_now}"


if __name__ == '__main__':
    app.run(debug=True)
