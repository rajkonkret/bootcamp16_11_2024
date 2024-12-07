# napisać dekorator, który zmieni wynik działania funkcji na duże litery
def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


# bold_decorator \033[1m
def bold_decorator(func):
    def wrapper():
        result = func()
        return f"\033[1m" + result + "\033[0m"

    return wrapper


@bold_decorator
@uppercase_decorator
def greeting():
    return "Hello World!"


@bold_decorator
def greeting2():
    return "Hello World!"


print(greeting())  # HELLO WORLD!
print(greeting2())  # Hello World!
