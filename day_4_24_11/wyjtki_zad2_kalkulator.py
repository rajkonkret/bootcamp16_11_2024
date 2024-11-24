# napisac program kalkulator z wykorzystaniem głownej petli while True
# przechwycic możliwe wyjątki i obsłużyc
# ładnie wypisac wynik np.: Dodawanie 2 + 4 = 6 - fstring
#
# wyswietlic opcje do wyboru (dodac opcje zakończenia)
# pobrac opcje od uzytkownika
# w zaleznosci od wybranej opcji wykonac działanie i wyswietlic wynik

while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)

    odp = input("Podaj dopcje menu")
    # if odp == "5":
    #     break
    if odp not in ["1", "2", "3", "4"]:
        break
    try:
        a = int(input("Podaj pierwszą liczby"))
        b = float(input("Podaj drugą liczbę"))

        if odp == "1":
            print(f"Wynik dodawania {a} + {b} = {a + b}")
        elif odp == "2":
            print(f"Wynik odejmowania {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"Wynik mnożenia {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"Wynik dzielenia {a} / {b} = {a / b}")
        else:
            print("Nie ma takiego działania")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except Exception as e:
        print("Błąd", e)
    else:
        print("Działanie wykonane poprawnie")
