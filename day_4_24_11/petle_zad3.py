# while - pętla sterowana warunki

# pętla nieskończona
# while True:
#     print("Komunika!!!")

licznik = 0
while True:
    print("Komunikat 1 !!!")
    licznik += 1
    if licznik > 15:
        break  # przerwanie pętli

print(licznik)  # 16
licznik = 0
while licznik < 15:
    licznik += 1
    print("Komunikat 2 !!!!")

# password = input("Podaj hasło")
# while password != 'secret':  # != - różne
#     password = input("Błędne hasło. Podaj ponownie")
# print("Hasło prawidłowe")
# Błędne hasło. Podaj ponowniewweggweg
# Błędne hasło. Podaj ponownieewgw
# Błędne hasło. Podaj ponowniesecret
# Hasło prawidłowe

# A string is numeric if all characters in the string are numeric
# lista = []
# lista_int = []
# while True:
#     wej = input("Podaj liczbę")  # str
#     if not wej.isnumeric():
#         break
#     lista.append(wej)
#     lista_int.append(int(wej))
# print(lista)
# print(lista_int)
# ['1', '2', '3', '333', '4444', '333333']
# [1, 2, 3, 333, 4444, 333333]
# Podaj liczbę4.566778 # kropka nie jest numeric, sprawdza wszystkie znaki
#
# []
# []

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
element_to_remove = 5
while element_to_remove in my_list:
    my_list.remove(element_to_remove)

print(my_list)  # [1, 2, 3, 4, 6]
