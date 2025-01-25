import fun_transactions as ft


def test_filter_transactions_income():
    expected_list = [
        {'amount': 1000, 'currency': 'USD', 'id': 1, 'type': 'income'},
        {'amount': 500, 'currency': 'USD', 'id': 3, 'type': 'income'},
        {'amount': 700, 'currency': 'USD', 'id': 5, 'type': 'income'},
        {'amount': 100, 'currency': 'EUR', 'id': 7, 'type': 'income'}
    ]
    assert ft.filter_transactions(ft.transactions, "income") == expected_list


# napisać test dla map_transactions()
def test_map_transactions_usd():
    result = [1000, 200, 500, 300, 700, 0, 0]
    assert ft.map_transactions(ft.transactions, "USD") == result


def test_reduce_transactions():
    assert ft.reduce_transactions([1000, 500, 700, 0]) == 2200


def test_process_transactions_expense_eur():
    assert ft.process_transactions(ft.transactions, "expense", "EUR") == 400

# (.venv) PS C:\Users\Administrator\PycharmProjects\bootcamp16_11_2024\day_13_25_01_25> pytest .\test_fun_transactions.py
# ====================================================================================================== test session starts =======================================================================================================
# platform win32 -- Python 3.12.7, pytest-8.3.4, pluggy-1.5.0
# rootdir: C:\Users\Administrator\PycharmProjects\bootcamp16_11_2024\day_13_25_01_25
# plugins: anyio-4.8.0
# collected 4 items
#
# test_fun_transactions.py ....                                                                                                                                                                                               [100%]
#
# ======================================================================================================= 4 passed in 0.05s ========================================================================================================
# (.venv) PS C:\Users\Administrator\PycharmProjects\bootcamp16_11_2024\day_13_25_01_25>
