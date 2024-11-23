# od python 3.10 mamy match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.lower().replace(" ", ""):
    case "python":
        print("Lubię pythona")
        lista.append(lang)
    case "java":
        print("Java to kawa")
        lista.append(lang)
    case "c++":
        print('Kto to jescze używa')
        lista.append(lang)
    case _:
        print("Nie znam takiego języka")

print(f"Lista z odpowiedziami {lista}")
# Podaj znany Ci język programowania ja va
# Java to kawa
# Lista z odpowiedziami [' ja va']