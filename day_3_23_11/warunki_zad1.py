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

rabat = 25 if suma_zam > 150 else 0 # ternary operator, operator warunkowy
print(f"Rabacik wynosi {rabat}")
# Rabacik wynosi 25
# Rabacik wynosi 25