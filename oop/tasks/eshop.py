# Napis triedu Basket (z angl. košík), ktora bude v sebe uchovavat list poloziek (Item).
# bude obsahovat nasledovne metody:
# - add_item()
# - print_basket()
# - calculate_price() (treba zaokruhlit na 2 desatinne miesta (funkcia round))

class Basket:
    pass  # TODO

# Dalej napis triedu Item, ktory bude reprezentovat polozku. Kazda polozka bude mat atributy
# - Name
# - unit_price (jednotkova cena)
# - quantity (mnozstvo)
# a metodu get_price(), ktora vypocita cenu polozky

class Item:
    pass  # TODO

# Na zaver napis triedu WeightedItem (vazena polozka), ktora bude dedit z Item a bude mat navyse atribut `weight` (vaha)
# Atribut quantity bude mat vzdy hodnotu 1 a unit_price bude reprezentovat cenu za kilo.
# metoda get_price() teda bude musiet byt pre WeightedItem prepisana.

class WeightedItem(Item):
    pass  # TODO


# Priklad pouzitia:
if __name__ == "__main__":
    # Banan 27.90kc/kg, 2.61 kilo
    bananas = WeightedItem('banan', 27.90, 2.61)
    # 5 avokad za cenu 32Kc
    avocado = Item('avokado', 32, 5)
    # Jeden balik 4xAA bateriek za 89.90
    batteries = Item('baterky', 89.90, 1)

    # Vsetko hodime do kosiku
    basket = Basket()
    for item in [bananas, avocado, batteries]:
        basket.add_item(item)

    print(basket.print_basket())  # Vypise v rozumnom tvare zoznam poloziek v kosiku
    print(basket.calculate_price())  # Vypise 322.72
