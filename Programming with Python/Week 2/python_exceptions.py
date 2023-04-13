def divide_by(a, b):
    return a / b


try:
    ans = divide_by(40, 0)
except Exception as e:
    print("Something went wrong!", e)
    print(e.__class__)

try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print(e, "We can not divide by zero")
    print(e.__class__)

try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print("Something went wrong!", e)
    print(e.__class__)
except Exception as e:
    print(e, "something went wrong!")
