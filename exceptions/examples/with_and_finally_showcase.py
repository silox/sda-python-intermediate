# Toto
with open("temp.txt") as file:
    file.write("Ala has a cat")


# A toto robi viacmenej to iste.
try:
    file = open("temp.txt")
    file.write("Ala has a cat")
finally:
    file.close()
