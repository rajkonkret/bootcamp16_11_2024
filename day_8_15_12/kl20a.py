class MyError(Exception):
    def __init__(self, message, err_code):
        super().__init__(message)
        self.err_code = err_code


class MyValueError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=100)


class MyTypeError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=200)


def my_function(x: int, y: int) -> float:
    if not isinstance(x, int):
        raise MyTypeError("x must be integer")
    if not isinstance(y, int):
        raise MyTypeError("y must be integer")
    if y == 0:
        raise MyValueError('y cannot be zero')

    return x / y


try:
    result = my_function(4, 5)
    # result = my_function(4, 0)
    result = my_function("A", 0)
except MyTypeError as e:
    print("Caught a MyTypeError", e)
    print("Error code:", e.err_code)
except MyValueError as e:
    print("Caught a MyValueError", e)
    print("Error code:", e.err_code)
except Exception as e:
    print("Error:", e)
else:
    print(f"Result is {result}")
finally:
    print("End")
# Caught a MyValueError y cannot be zero
# Error code: 100
# End
# Caught a MyTypeError x must be integer
# Error code: 200
# End
