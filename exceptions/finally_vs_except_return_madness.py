def foo():
    try:
        0 / 0
    except Exception as e:
        print('I am here', e)
        return 1
    # Finally very strong
    finally:
        print('Did I reach this as well!?')
        return 2


print(foo())
