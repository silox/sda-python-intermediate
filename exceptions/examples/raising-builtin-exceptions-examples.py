# AssertionError
assert 0 == 1

# NameError
unknown_variable

# AttributeError
a = []
a.add(1)

# Sluzi na vypis vsetkych atributov objektu. Velmi uzitocne!
print(dir(a))

# FileNotFoundError
with open('abcd.txt', 'r') as file:
    file.write('asdf')

# IndexError
b = []
print(b[0])

# ModuleNotFoundError
import nieco_co_neexistuje

# KeyError
dct = {}
print(dct['nope'])
