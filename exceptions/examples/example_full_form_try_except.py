try:
    0 + 0
    print('try continuation')
except ZeroDivisionError as e:
    print('exception occured:', e)
else:
    print("we are in else block")
finally:
    print("always will be printed")

print('done')
