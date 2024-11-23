import random

# import - słuzy do dołączania do naszego pliku innego pliku, biblioteki, frameworka itd...

# random - działania na liczbach pseudolosowych

print(random.randint(1, 6))  # int od 1 do 6
print(random.randrange(1, 6))  # int od 1 do 5
print(random.randrange(6))  # int od 0 do 5
print(random.random())  # float 0.9024250264716613, od 0 do 0.999999
print(random.random() * 7)  # float 3.3174267390281607 od 0 do 6.999999

lista = [5, 7, 45, 34, 56]

index = random.randrange(len(lista))  # len() = 5, 0 do 4
print(index, lista[index])  # 2 45

print(random.choice(lista))  # wylosowany element 34

print("--------------------")
print("-" * 20)

# maszyna lotto
# bęben maszyny zawiera kule -> lista
# losowanie kul -> random
# usnięcie kuli z bębna -> remove
# wyświetlenie w telewizji -> print

lista_kule = list(range(1, 50))  # od 1 do 49
# print(lista_kule)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))  # losuje z powtórzeniami [42, 46, 28, 28, 23, 16]
print(random.sample(lista_kule, k=6))  # [28, 8, 45, 5, 17, 48], losuje bez powtórzeń
print(random.sample(lista_kule, 6))  # [28, 8, 45, 5, 17, 48], losuje bez powtórzeń
# [30, 27, 23, 11, 26, 18]
# [14, 4, 44, 39, 10, 28]
print(random.sample(range(1, 50), 6))
# [14, 49, 24, 4, 11, 27]
# [12, 10, 42, 45, 48, 15]
# [10, 23, 8, 41, 6, 45]
