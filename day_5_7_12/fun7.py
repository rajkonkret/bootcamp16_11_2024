def connect(**opcje):  # ** - argumenty słownikowe, keywords
    print(opcje)
    print(type(opcje))  # <class 'dict'>
    param = {
        'host': '127.0.0.1',
        'port': '8080'
    }
    param.update(opcje)
    print(param)  # {'host': '127.0.0.1', 'port': '8080', 'a': 9, 'name': 'Radek'}
    param['pwd'] = opcje
    print(param)  # {'host': '127.0.0.1', 'port': '8080', 'a': 9, 'name': 'Radek', 'pwd': {'a': 9, 'name': 'Radek'}}


connect()  # {}
connect(a=9)  # {'a': 9}
connect(a=9, name="Radek")  # {'a': 9, 'name': 'Radek'}

dict = {'host': '127.0.0.1', 'port': '8080', 'a': 9, 'name': 'Radek', 'pwd': {'a': 9, 'name': 'Radek'}}
print(dict['pwd'])  # {'a': 9, 'name': 'Radek'}
print(dict['pwd']['name'])  # Radek


def connect_all(*args, **kwargs):
    print(args, kwargs)


connect_all()  # () {}
connect_all(1, 2, 3, 4, 5, 6, 7)  # (1, 2, 3, 4, 5, 6, 7) {}
connect_all(1, 2, 3, 4, 5, 6, 7, 'Zenek')  # (1, 2, 3, 4, 5, 6, 7, 'Zenek') {}
connect_all(a=0, b=9)  # () {'a': 0, 'b': 9}
connect_all(1, 2, 3, 4, 5, 6, 7, 'Zenek', a=0, b=9)  # (1, 2, 3, 4, 5, 6, 7, 'Zenek') {'a': 0, 'b': 9}
# connect_all(c=9, 1, 2, 3, 4, 5, 6, 7, 'Zenek', a=0, b=9)  SyntaxError: positional argument follows keyword argument
