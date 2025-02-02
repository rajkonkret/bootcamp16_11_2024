from flask import Flask, render_template, url_for, request, flash, g, redirect, session
# import sqlite3
from flask_sqlalchemy import SQLAlchemy
import random
import string
import hashlib
import binascii

# app_info = {
#     # 'db_file' : 'C:/Users/Administrator/PycharmProjects/bootcamp16_11_2024/day_14_26_01_25/web_app_bootstrap_sqlite3/data/cantor.db'
#     'db_file': 'data/cantor.db'
# }
# app.py
app = Flask(__name__)
# dodajemy secret_key aby komunikacja flash wykonywała się w bezpieczny sposób
# app.config['SECRET_KEY'] = "KluczTrudnyDOZlamania123!!!"
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(5))
    amount = db.Column(db.Integer)
    user = db.Column(db.String(30))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.Text)
    is_active = db.Column(db.Boolean())
    is_admin = db.Column(db.Boolean())


# def get_db():
#     if not hasattr(g, 'sqlite_db'):
#         conn = sqlite3.connect(app_info['db_file'])
#         conn.row_factory = sqlite3.Row  # dane zwracane jako słownik
#         g.sqlite_db = conn
#     return g.sqlite_db
#
#
# @app.teardown_appcontext
# def close_db(error):
#     if hasattr(g, 'sqlite_db'):
#         g.sqlite_db.close()


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


class UserPass:

    def __init__(self, user='', password=''):
        self.user = user
        self.password = password
        self.email = ""
        self.is_valid = False
        self.is_admin = False

    def hash_password(self):
        os_urandom_static = b'\xee\x8b\x9c\xe6n\x96\xa9\xf5@\x99\x9c\xf3\xbf\xf1\x03\x86sr\x05\xcf\xa7\xac\xcf\xb2H\xfe\x7f\x10\x14\x9f%5\xde\xe5\xbd\xaef\x9d\xcd\xf4\xc9Be\xf9\x04\xf9\x1c}\xf9\x8a|\xe4\x92\xe1\xdb\xff~R\x0e\xb1'
        salt = hashlib.sha256(os_urandom_static).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', self.password.encode('utf=8'), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    def verify_password(self, stored_password, provided_password):
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf=8'), salt.encode('ascii'), 100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def get_random_user_password(self):
        random_user = ''.join(random.choice(string.ascii_lowercase) for i in range(3))
        self.user = random_user

        password_characters = string.ascii_letters  # + string.digits + string.punctuation
        random_password = ''.join(random.choice(password_characters) for i in range(3))
        self.password = random_password

    def login_user(self):
        # db = get_db()
        # sql_statement = 'select id, name, email, password, is_active, is_admin from users where name=?'
        # cur = db.execute(sql_statement, [self.user])
        # user_record = cur.fetchone()  # jako słownik
        user_record = User.query.filter(User.name == self.user).first()

        if user_record != None and self.verify_password(user_record.password, self.password):
            return user_record
        else:
            self.user = None
            self.password = None
            return None

    def get_user_info(self):

        # db = get_db()
        # sql_statement = 'select name, email, is_active, is_admin from users where name=?;'
        # cur = db.execute(sql_statement, [self.user])
        # db_user = cur.fetchone()
        db_user = User.query.filter(User.name == self.user).first()

        if db_user == None:
            self.is_valid = False
            self.is_admin = False
            self.email = ""
        elif db_user.is_active != 1:
            self.is_valid = False
            self.is_admin = False
            self.email = db_user.email
        else:
            self.is_valid = True
            self.is_admin = db_user.is_admin
            self.email = db_user.email


@app.route('/login', methods=['GET', 'POST'])
def login():
    login = UserPass(session.get('user'))
    login.get_user_info()

    if request.method == 'GET':
        return render_template('login.html', active_menu="login", login=login)
    else:
        user_name = '' if "user_name" not in request.form else request.form['user_name']
        user_pass = '' if "user_pass" not in request.form else request.form['user_pass']

        login = UserPass(user_name, user_pass)
        login_record = login.login_user()

        if login_record != None:
            session['user'] = user_name
            flash("Logon succesfull, welcome {}".format(user_name))
            return redirect(url_for('index'))
        else:
            flash("Logon failed, try again")
            return render_template('login.html', active_menu='login', login=login)


@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user', "None")
        flash("You are logged out")
    return redirect(url_for('login'))


@app.route('/init_app')
def init_app():
    # db = get_db()
    db.create_all()
    # sql_statement = 'select count(*) as cnt from users where is_active and is_admin;'
    # cur = db.execute(sql_statement)
    # active_admins = cur.fetchone()
    active_admins = User.query.filter(User.is_active == True, User.is_admin == True).count()

    # delete from users where id=1; usunięcie usera
    # User nyc with password Sqt has been created
    # if active_admins != None and active_admins['cnt'] > 0:
    #     flash("Application is already set-up. Nothing to do")
    #     return redirect(url_for('index'))
    if active_admins > 0:
        flash("Application is already set-up. Nothing to do")
        return redirect(url_for('index'))

    user_pass = UserPass()
    user_pass.get_random_user_password()
    # db.execute('''insert into users(name, email, password,is_active,is_admin)
    # values(?,?,?,True,True);''',
    #            [user_pass.user, 'rajkonkret@rajkonkret.pl', user_pass.hash_password()])
    # db.commit()
    new_admin = User(name=user_pass.user, email='a@a.pl', password=user_pass.hash_password(),
                     is_active=True, is_admin=True)
    db.session.add(new_admin)
    db.session.commit()
    # User xbb with password GTz has been created
    flash("User {} with password {} has been created".format(user_pass.user, user_pass.password))
    return redirect(url_for('index'))


@app.route("/")
def index():
    login = UserPass(session.get('user'))
    login.get_user_info()
    return render_template('index.html', active_menu='home', login=login)


@app.route('/exchange', methods=['GET', 'POST'])
def exchange():
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    offer = CantorOffer()
    offer.load_offer()

    if request.method == "GET":
        return render_template('exchange.html', offer=offer,
                               active_menu='exchange', login=login)
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
            # db = get_db()
            # sql_command = 'insert into transactions(currency, amount, user) values (?, ?, ?)'
            # db.execute(sql_command, [currency, amount, "admin"])
            # db.commit()
            new_tran = Transaction(currency=currency, amount=amount, user='admin')
            db.session.add(new_tran)
            db.session.commit()

            flash("Request to exchange {} was accepted".format(currency))

        return render_template('exchange_results.html', currency=currency, amount=amount,
                               currency_info=offer.get_by_code(currency), active_menu='exchange',
                               login=login)


@app.route('/history')
def history():
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    # db = get_db()
    # sql_command = 'select id, currency, amount from transactions;'
    # cur = db.execute(sql_command)
    # transactions = cur.fetchall()
    transactions = Transaction.query.all()

    return render_template('history.html', active_menu='history',
                           transactions=transactions, login=login)


@app.route('/delete_transaction/<int:transaction_id>')
def delete_transaction(transaction_id):
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    # db = get_db()
    # sql_statement = 'delete from transactions where id = ?;'
    # db.execute(sql_statement, [transaction_id])
    # db.commit()
    del_tran = Transaction.query.filter(Transaction.id == transaction_id).first()
    db.session.delete(del_tran)
    db.session.commit()

    return redirect(url_for('history'))


@app.route('/edit_transaction/<int:transaction_id>', methods=['GET', 'POST'])
def edit_transaction(transaction_id):
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid:
        return redirect(url_for('login'))

    offer = CantorOffer()
    offer.load_offer()
    # db = get_db()

    if request.method == "GET":
        # sql_statement = 'select id, currency, amount from transactions where id=?;'
        # cur = db.execute(sql_statement, [transaction_id])
        # transaction = cur.fetchone()
        transaction = Transaction.query.filter(Transaction.id == transaction_id).first()

        if transaction == None:
            flash("No such transaction!")
            return redirect(url_for('history'))
        else:
            return render_template('edit_transaction.html', transaction=transaction, offer=offer,
                                   active_menu='history', login=login)
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
            # db = get_db()
            # sql_command = '''update transactions set
            # currency=?,
            # amount=?,
            # user=?
            # where id=?;'''
            # db.execute(sql_command, [currency, amount, "admin", transaction_id])
            # db.commit()
            transaction = Transaction.query.filter(Transaction.id == transaction_id).first()
            transaction.currency = currency
            transaction.amount = amount
            transaction.user = 'admin'
            db.session.commit()

            flash("Transaction was updated")

        return redirect((url_for('history')))


@app.route('/users')
def users():
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid or not login.is_admin:
        return redirect(url_for('login'))

    # db = get_db()
    # sql_command = 'select id, name, email, is_admin, is_active from users;'
    # cur = db.execute(sql_command)
    # users = cur.fetchall()
    users = User.query.all()

    return render_template('users.html', active_menu="users", users=users, login=login)


@app.route('/user_status_change/<action>/<user_name>')
def user_status_change(action, user_name):
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid or not login.is_admin:
        return redirect(url_for('login'))

    # if not 'user' in session:
    #     return redirect(url_for('login'))
    # login = session['user']

    # db = get_db()
    if action == 'active':
        user = User.query.filter(User.name == user_name, User.name != login.user).first()
        # db.execute("""update users set is_active = (is_active + 1) % 2
        # where name = ? and name <> ?;""", [user_name, login.user])
        # db.commit()
        if user:
            user.is_active = (user.is_active + 1) % 2
            db.session.commit()

    elif action == 'admin':
        user = User.query.filter(User.name == user_name, User.name != login.user).first()
        # db.execute("""update users set is_admin = (is_admin + 1) % 2
        # where name = ? and name <> ?;""", [user_name, login.user])
        # db.commit()
        if user:
            user.is_admin = (user.is_admin + 1) % 2
            db.session.commit()

    return redirect(url_for('users'))


@app.route('/edit_user/<user_name>', methods=['GET', 'POST'])
def edit_user(user_name):
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid or not login.is_admin:
        return redirect(url_for('login'))

    # db = get_db()
    # cur = db.execute('select name, email from users where name = ?', [user_name])
    # user = cur.fetchone()
    user = User.query.filter(User.name == user_name).first()

    message = None

    if user == None:
        flash("No such user")
        return redirect(url_for('users'))

    if request.method == 'GET':
        return render_template('edit_user.html', active_menu='users', user=user, login=login)
    else:
        new_email = '' if 'email' not in request.form else request.form['email']
        new_password = '' if 'password' not in request.form else request.form['password']

        if new_email != user.email:
            # sql_statement = 'update users set email = ? where name = ?;'
            # db.execute(sql_statement, [new_email, user_name])
            # db.commit()
            user.email = new_email
            db.session.commit()

            flash("Email was changed")

        if new_password != "":
            user_pass = UserPass(user_name, new_password)
            # sql_statement = 'update users set password = ? where name = ?'
            # db.execute(sql_statement, [user_pass.hash_password(), user_name])
            # db.commit()
            user.password = user_pass.hash_password()
            db.session.commit()

            flash("Password was changed")

        return redirect(url_for('users'))


@app.route('/user_delete/<user_name>')
def delete_user(user_name):
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid or not login.is_admin:
        return redirect(url_for('login'))

    # if not 'user' in session:
    #     return redirect(url_for('login'))

    # login = session['user']

    # db = get_db()
    # sql_statement = "delete from users where name =? and name <> ?"
    # db.execute(sql_statement, [user_name, login.user])
    # db.commit()
    user = User.query.filter(User.name == user_name, User.name != login.user).first()
    if user:
        flash('User {} has been removed'.format(user_name))
        db.session.delete(user)
        db.session.commit()

    return redirect(url_for('users'))


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    login = UserPass(session.get('user'))
    login.get_user_info()
    if not login.is_valid or not login.is_admin:
        return redirect(url_for('login'))
    # if not 'user' in session:
    #     return redirect(url_for('login'))
    #
    # login = session['user']

    # db = get_db()
    message = None
    user = {}

    if request.method == 'GET':
        return render_template('new_user.html', active_menu='users', user=user, login=login)
    else:
        user['user_name'] = '' if not 'user_name' in request.form else request.form['user_name']
        user['email'] = '' if not 'email' in request.form else request.form['email']
        user['user_pass'] = '' if not 'user_pass' in request.form else request.form['user_pass']

        # cur = db.execute('select count(*) as cnt from users where name = ?', [user['user_name']])
        # record = cur.fetchone()
        # is_user_name_unique = (record['cnt'] == 0)
        is_user_name_unique = (User.query.filter(User.name == user['user_name']).count() == 0)

        # cur = db.execute('select count(*) as cnt from users where email = ?', [user['email']])
        # record = cur.fetchone()
        # is_user_email_unique = (record['cnt'] == 0)
        is_user_email_unique = (User.query.filter(User.email == user['email']).count() == 0)

        if user['user_name'] == "":
            message = "Name cannot be empty"
        elif user['email'] == '':
            message = "Email cannot be empty"
        elif user['user_pass'] == '':
            message = 'Password cannot be empty'
        elif not is_user_name_unique:
            message = f"User with the name {user['user_name']} already exists"
        elif not is_user_email_unique:
            message = f"User with the email {user['email']} already exists"

        if not message:
            user_pass = UserPass(user['user_name'], user['user_pass'])
            password_hash = user_pass.hash_password()
            # sql_statement = '''insert into users(name, email, password, is_active, is_admin)
            # values(?,?,?,TRue,False);'''
            #
            # db.execute(sql_statement, [user['user_name'], user['email'], password_hash])
            # db.commit()
            new_user = User(name=user['user_name'], email=user['email'], password=password_hash,
                            is_active=True, is_admin=False)
            db.session.add(new_user)
            db.session.commit()

            flash(f"User {user['user_name']} crated.")
            return redirect(url_for('users'))
        else:
            flash("Correct reror: {}".format(message))
            return render_template('new_user.html', active_menu='users', user=user, login=login)


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port="80")
    app.run(debug=True, host='0.0.0.0')
