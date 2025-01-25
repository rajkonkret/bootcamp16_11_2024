from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    print(request.query_string)
    # http://127.0.0.1:5000/?color=blue&style=italic
    # b'color=blue&style=italic'
    # print(request.args['color']) # blue
    # print(request.args['color1']) # BadRequestKeyError

    color = 'black'
    if 'color' in request.args:
        color = request.args['color']

    style = 'normal'
    if 'style' in request.args:
        style = request.args['style']

    for p in request.args:
        print(p, request.args[p])
    # b''
    # b'color=blue&style=italic'
    # color blue
    # style italic

    # http://127.0.0.1:5000/?color=red&style=italic;%22%3EHacked%3Ch1%20style=%22font-style:italic
    """
    <h1 style="color: red; font-style:italic;">
    Hacked<h1 style="font-style:italic;">Hello World</h1>
    """
    return f'<h1 style="color: {color}; font-style:{style};">Hello World</h1>'


# @app.route("/")
# def index():
#     return "Hello World!!!!!!"

@app.route("/exchange")
def exchange():
    body = """
    <form id="exchange_form" action="/exchange_process" method="POST">
    <label for="currency">Currency</label>
    <input type="text" id="currency" name="currency" value="EUR"><br>
    <label for="amount">Amount</label>
    <input type="text" id="amount" name="amount" value="100"><br>
    <input type="submit" value="Send">
    </form>
    """

    return body

# "POST /exchange_process HTTP/1.1" 200 -
@app.route("/exchange_process", methods=['POST'])
def exchange_process():
    currency = "EUR"
    if 'currency' in request.form:
        currency = request.form['currency']

    amount = 250
    if 'amount' in request.form:
        amount = request.form['amount']

        body = f"You want to exchange {amount} {currency}"
        return body


@app.route('/about')
def about():
    a = 10
    b = 1
    return '<h1>We are programers {} </h1>'.format(a / b)


@app.route('/error')
def error():
    a = 10
    b = 0
    return '<h1>We are programers {} </h1>'.format(a / b)


@app.route("/cantor/<string:currency>/<int:amount>")
# @app.route("/cantor/<currency>/<amount>")
def cantor(currency, amount):
    message = f"<h1>You selected {currency} and {amount}</h1>"
    return message


if __name__ == '__main__':
    app.run(debug=True)
# http://127.0.0.1/  localhost, nasz komputer
#  http://127.0.0.1:5000 - 5000 port
