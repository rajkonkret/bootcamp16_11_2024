# # od python 3.10 mamy match case
#
# lista = []
# lang = input("Podaj znany Ci język programowania")
#
# match lang.lower().replace(" ", ""):
#     case "python":
#         print("Lubię pythona")
#         lista.append(lang)
#     case "java":
#         print("Java to kawa")
#         lista.append(lang)
#     case "c++":
#         print('Kto to jescze używa')
#         lista.append(lang)
#     case _: # odpowiednik else
#         print("Nie znam takiego języka")
#
# print(f"Lista z odpowiedziami {lista}")
# # Podaj znany Ci język programowania ja va
# # Java to kawa
# # Lista z odpowiedziami [' ja va']

# dane = [1, 2, 3]
dane = {'nazwa': "Radek", "wiek": 45}
match dane:
    case [a, b, c]:
        print(f"Lista z trzema elementami {a=} {b=} {c=}")
    case {'nazwa': n, "wiek": w}:
        print(f"Słownik reprezentujący osobę {n}, wiek {w}")
    case _:  # else
        print("Błędny typ danych")
# Słownik reprezentujący osobę Radek, wiek 45
#
# Process finished with exit code 0
