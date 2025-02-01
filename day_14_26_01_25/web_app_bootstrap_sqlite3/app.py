from flask import Flask, render_template, url_for, request, flash, g, redirect
import sqlite3

from six import add_move

app_info = {
    # 'db_file' : 'C:/Users/Administrator/PycharmProjects/bootcamp16_11_2024/day_14_26_01_25/web_app_bootstrap_sqlite3/data/cantor.db'
    'db_file': 'data/cantor.db'
}
# app.py
app = Flask(__name__)
# dodajemy secret_key aby komunikacja flash wykonywała się w bezpieczny sposób
app.config['SECRET_KEY'] = "KluczTrudnyDOZlamania123!!!"


def get_db():
    if not hasattr(g, 'sqlite_db'):
        conn = sqlite3.connect(app_info['db_file'])
        conn.row_factory = sqlite3.Row
        g.sqlite_db = conn
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


class Currency:
    def __init__(self, code, name, flag):
        self.code = code
        self.name = name
        self.flag = flag

    def __repr__(self):
        return f'<Currency {self.code}>'


class CantorOffer:
    def __init__(self):
        self.currencies = []
        self.denied_code = []

    def load_offer(self):
        """
        Ładuje dane do systemu
        :return:
        """
        self.currencies.append(Currency('USD', "Dollar", 'currencies/dollar.png'))
        self.currencies.append(Currency('EUR', "Euro", 'currencies/euro.jpg'))
        self.currencies.append(Currency('HUF', "Forint", 'currencies/huf.jpg'))
        self.currencies.append(Currency('PLN', "Zloty", 'currencies/zloty.jpg'))
        self.currencies.append(Currency('GBP', "Pound", 'currencies/gbp.png'))
        self.denied_code.append('USD')

    def get_by_code(self, code):
        """
        Zwraca obiekt klasy Currency na podstawie kodu waluty
        :code:
        :return:
        """
        for currency in self.currencies:
            if currency.code == code:
                return currency

        return Currency('unknown', 'unknown', 'kantor.png')


@app.route("/")
def index():
    return render_template('index.html', active_menu='home')


@app.route('/exchange', methods=['GET', 'POST'])
def exchange():
    offer = CantorOffer()
    offer.load_offer()

    if request.method == "GET":
        return render_template('exchange.html', offer=offer, active_menu='exchange')
    else:
        flash("Debug: starting exchange in POST mode")

        amount = 100
        if 'amount' in request.form:
            amount = request.form['amount']
            print(amount)

        currency = 'EUR'
        if 'currency' in request.form:
            currency = request.form['currency']
            print(currency)

        if currency in offer.denied_code:
            flash("The currency {} cannot be accepted".format(currency))
        elif offer.get_by_code(currency) == 'unknown':
            flash("The selected currency is unknown and cannot be accepted")
        else:
            db = get_db()
            sql_command = 'insert into transactions(currency, amount, user) values (?, ?, ?)'
            db.execute(sql_command, [currency, amount, "admin"])
            db.commit()
            flash("Request to exchange {} was accepted".format(currency))

        return render_template('exchange_results.html', currency=currency, amount=amount,
                               currency_info=offer.get_by_code(currency), active_menu='exchange')


@app.route('/history')
def history():
    db = get_db()
    sql_command = 'select id, currency, amount from transactions;'
    cur = db.execute(sql_command)
    transactions = cur.fetchall()

    return render_template('history.html', active_menu='history', transactions=transactions)


@app.route('/delete_transaction/<int:transaction_id>')
def delete_transaction(transaction_id):
    db = get_db()
    sql_statement = 'delete from transactions where id = ?;'
    db.execute(sql_statement, [transaction_id])
    db.commit()

    return redirect(url_for('history'))


@app.route('/edit_transaction/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    offer = CantorOffer()
    offer.load_offer()
    db = get_db()

    if request.method == "GET":
        sql_statement = 'select id, currency, amount from transactions where id=?;'
        cur = db.execute(sql_statement, [transaction_id])
        transaction = cur.fetchone()

        if transaction == None:
            flash("No such transaction!")
            return redirect(url_for('history'))
        else:
            return render_template('edit_transaction.html', transaction=transaction, offer=offer,
                                   active_menu='history')
    else:

        amount = 100
        if 'amount' in request.form:
            amount = request.form['amount']
            print(amount)

        currency = 'EUR'
        if 'currency' in request.form:
            currency = request.form['currency']
            print(currency)

        if currency in offer.denied_code:
            flash("The currency {} cannot be accepted".format(currency))
        elif offer.get_by_code(currency) == 'unknown':
            flash("The selected currency is unknown and cannot be accepted")
        else:
            db = get_db()
            sql_command = '''update transactions set
            currency=?,
            amount=?,
            user=?
            where id=?;'''
            db.execute(sql_command, [currency, amount, "admin", transaction_id])
            db.commit()
            flash("Transaction was updated")

        return redirect((url_for('history')))


if __name__ == '__main__':
    app.run(debug=True)
