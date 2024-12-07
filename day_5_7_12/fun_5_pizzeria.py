# zrobic funkcje restauracja()
# zamow_pizze, zamow_napoj
# w zaleznosci od parametru mamy zwrócic jedną z tych funkcji

def restauracja(typ_amowienia):
    print("Witam w naszej restauracji")

    def zamow_pizze(skladniki="pieczarki"):
        print("Zamówiono pizza, składniki:", skladniki)

    def zamow_napoj(nazwa="herbata"):
        print('Zamów napoj', nazwa)

    if typ_amowienia.casefold().strip() == 'pizza':
        return zamow_pizze
    else:
        return zamow_napoj  # zwracamy adres funkcji


zamowienie_pizza = restauracja('pizza')
zamowienie_pizza()  # Zamówiono pizza, składniki: pieczarki
zamowienie_pizza("pieczarki, szynka")  # Zamówiono pizza, składniki: pieczarki, szynka

zamowienie_napoj = restauracja("napoj")
zamowienie_napoj()
zamowienie_napoj("cola")

zamowienie_pizza()  # Zamówiono pizza, składniki: pieczarki
# Witam w naszej restauracji
# Zamówiono pizza, składniki: pieczarki
# Zamówiono pizza, składniki: pieczarki, szynka
# Witam w naszej restauracji
# Zamów napoj herbata
# Zamów napoj cola
# Zamówiono pizza, składniki: pieczarki
