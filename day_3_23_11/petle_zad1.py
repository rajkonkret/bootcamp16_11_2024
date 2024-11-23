# pętla - możliwość wykonania tego samego fragmentu kodu wielokrotnie
# for - pętla iteracyjna
import random

for i in range(10):  # od 0 do 9
    print(i)

for i in range(10):  # od 0 do 9
    print(i, i, sep=":")  # 9:9

for i in range(10):
    print(i, end="")  # 0123456789, wszystko wypisane w jednej linii

print()  # ustawienie end="\n"
print("Konniec pętli")  # Konniec pętli

for i in range(1, 25):  # od 1 do 24
    print(i)

for _ in range(1, 5):  # _ niema zmienna
    print("Kominkat")
    # print(_)

my_string = "Radek"
for i in my_string:  # petla działa, aż skończą się w niej elementy
    print(i)

# przerobic lotto na pętle
print("----------------")
lista_kule = list(range(1, 50))
lista_wylosowane = []

for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    # print(wyn)
    lista_wylosowane.append(wyn)

print(lista_wylosowane)  # [48, 38, 17, 8, 18, 7]

# posortowac liste wyników
lista_wylosowane.sort()
print(lista_wylosowane)
# [46, 12, 7, 10, 45, 49]
# [7, 10, 12, 45, 46, 49]
