try:
    arr = []
    'asdf' + 1
except ZeroDivisionError:
    print('zero division error')
except IndexError:
    print('index error')
except Exception:
    print('other exception')
