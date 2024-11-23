# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if - sterowana warunkiem
# if warunek:
#    komenda(blok) wykonywany gdy warunek spełniony

odp = True
print(bool(odp))  #
# odp = False
# debug - tryb do uruchaminia programu linijka po linijce i sprawdzaniu parametrów
if odp:
    # po dwukropku wcięcie
    # 4 spacje
    print("Brawo")  # Brawo
    print("Brawo")  # Brawo
    print("Brawo")  # Brawo
    print("Brawo")  # Brawo
    print("Brawo")  # Brawo
    print("Brawo")  # Brawo

print("Dalsza część programu")
# True
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo
# Brawo
# Dalsza część programu

odp = "Radek"
if odp == "Radek":
    print("Radek")
# Radek

odp = "Tomek"
if odp == "Radek":
    print("Radek")
else:  # działanie domyślne, gdy warunek niespełniony
    print("Inny przypadek")
# Inny przypadek

if True:
    pass  # nic nie rób

print("Dalej")

# kolejność warunków ma znaczenie
# po pierwszyw spełnionym warunku (True) wychodzi z drzewka
# podatek = 0.9
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:  # od 10000 do 29999
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.9
# print(f"Płacisz {zarobki * podatek} podatku")
# # dodac podatek 0.2 dla przedziału 10000 do 29999

# # tu ma znaczenie ostatni spełniony
# if zarobki < 10000:
#     podatek = 0
#
# if zarobki < 1000:
#     podatek = 0.4

suma_zam = 250
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabacik wynosi {rabacik}")

rabat = 25 if suma_zam > 150 else 0  # ternary operator, operator warunkowy
print(f"Rabacik wynosi {rabat}")
# Rabacik wynosi 25
# Rabacik wynosi 25

# testowanie użycia Tabnine
# if 10 < 5:
#     print("10 jest mniejsze od 5")
#     if 5 < 10:
#         print("5 jest mniejsze od 10")
#         if 10 < 15:
#             print("10 jest mniejsze od 15")
#             if 15 < 20:
#                 print("15 jest mniejsze od 20")
#
# rabat = 25 if suma_zam > 150 else 0
# if rabat > 0:
#     print("Rabat jest aktywny")
#     print(f"Rabacik wynosi {rabat}")
#     if rabat > 20:
#         print("Rabat jest zbyt duży")
# Rabat jest aktywny
# Rabacik wynosi 25
# Rabat jest zbyt duży

# zasymuluj system zbierania logów
# w zmiennej dostanie typ sytemu np.: console, email, inny
# w zależności od zawartości zmiennej:
# dla "console" -> "Stało się coś strasznego"
# dla "email" -> "System email"
# jesli system bedzie email to nalezy do listy błedów dodać opis błedu
# bład bedie w kolejnej zmiennej -> error, medium, inny
alert_system = "email"
error = "error"
lista_b = []

if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")
    if error == "error":
        lista_b.append("Krytyczny")
    elif error == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("inny bład")
else:
    print("Inny")

print("Lista błędów", lista_b)
# System email
# Lista błędów ['Ostrzeżenie']

alert_dict = {'console': "Coś poszło nie tak",
              'email': {'error': 'Krytyczny', 'medium': "Ostrzeżenie"}}

if alert_system == 'console':
    # print(alert_dict[alert_system])
    print(alert_dict.get(alert_system, "Nie ma takiego systemu"))
elif alert_system == "email":
    # errors = alert_dict[alert_system]
    errors = alert_dict.get(alert_system, {})
    # print(errors[error])
    print(errors.get(error, "Nie ma takiego błędu dla systemu email"))
else:
    print("inny")

if alert_system in alert_dict:
    if alert_system == 'console':
        print(alert_dict.get(alert_system))
    elif alert_system == "email":
        print("System email")
        print(alert_dict[alert_system])  # {'error': 'Krytyczny', 'medium': 'Ostrzeżenie'}
        if error in alert_dict[alert_system]:
            errors = alert_dict[alert_system]
            print(errors[error])
else:
    print("Inny")
# System email
# Krytyczny


# zrobic program
# test z historii, geografii....
# pomysleć jak dodac punktacje

punkty = 0
odp = input("Podaj datę Chrztu Polski")
if odp == "966":
    punkty += 1  # punkty = punkty + 1
    print("Odpowiedź prawidłowa")
else:
    print("Błąd")

odp = input("Podaj stolicę Polski")
if odp.casefold() == 'warszawa':
    punkty += 1
    print("Odpowiedź prawidłowa")
else:
    print("Błąd")

print(f"Zdobyłeś {punkty} punktów.")
