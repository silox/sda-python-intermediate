def foo():
    print(0)
    div_ab(1, 0)
    print(1)


def div_ab(a, b):
    return a / b


try:
    foo()
except ZeroDivisionError as e:
    print('exception occured:', e)
