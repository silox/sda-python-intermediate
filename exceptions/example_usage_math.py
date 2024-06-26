from math import sqrt, log

# Task
# Napis funkciu handle_math(x) a vrati 3 vysledky (v tuple)
# - cislo 42 / x
# sqrt(x)
# log(x)

# Vytvor custom exception MathException a raisni ju s rozumnou hlaskou vtedy,
# ak nevieme vykonat jednu z danych operacii. V opacnom pripade vrat 3 vysledky.


class MathException(Exception):
    pass


def handle_math(x):
    if x == 0:
        raise MathException("Cannot divide by zero")
    if x < 0:
        raise MathException("Cannot calculate square root of negative number")
    # Useless, but what if customer really wants it?
    if x <= 0:
        raise MathException("Cannot calculate logarithm of non-positive number")

    return 42 / x, sqrt(x), log(x)


if __name__ == "__main__":
    res = handle_math(float(input("Enter a number: ")))
    print(res)
