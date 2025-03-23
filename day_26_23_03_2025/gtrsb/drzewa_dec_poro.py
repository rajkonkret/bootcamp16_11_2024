import math

from matplotlib import pyplot as plt

dane = [
    {"wiek": 55, "zarobki": 70, "decyzja": "tak"},
    {"wiek": 53, "zarobki": 50, "decyzja": "nie"},
    {"wiek": 47, "zarobki": 60, "decyzja": "tak"},
    {"wiek": 40, "zarobki": 30, "decyzja": "nie"},
    {"wiek": 35, "zarobki": 45, "decyzja": "tak"},
    {"wiek": 28, "zarobki": 65, "decyzja": "nie"},
    {"wiek": 31, "zarobki": 42, "decyzja": "tak"},
    {"wiek": 29, "zarobki": 50, "decyzja": "nie"},
    {"wiek": 52, "zarobki": 80, "decyzja": "tak"},
    {"wiek": 60, "zarobki": 55, "decyzja": "tak"},
]


# wskaźnik giniego lub entropia (entropia - logarytmiczna - wolniejsza)
# funkcja Giniego (0 - dobrze)
def gini_index(dane):
    total = len(dane)
    if total == 0:
        return 0

    decyzje = [x['decyzja'] for x in dane]
    pozytywne = decyzje.count("tak") / total
    negatywne = decyzje.count("nie") / total
    gini = 1 - (pozytywne ** 2 + negatywne ** 2)
    return gini


def gini_po_podziale(lewa, prawa):
    total = len(lewa) + len(prawa)
    w1 = len(lewa) / total
    w2 = len(prawa) / total
    return w1 * gini_index(lewa) + w2 * gini_index(prawa)


# entropia
def entropy_index(dane):
    total = len(dane)
    if total == 0:
        return 0
    decyzja = [x['decyzja'] for x in dane]
    p1 = decyzja.count("tak") / total
    p2 = decyzja.count("nie") / total
    ent = 0
    for p in [p1, p2]:
        if p > 0:
            ent -= p * math.log2(p)
    return ent


def entropy_po_podziale(lewa, prawa):
    total = len(lewa) + len(prawa)
    w1 = len(lewa) / total
    w2 = len(prawa) / total
    return w1 * entropy_index(lewa) + w2 * entropy_index(prawa)


def wypisz_grupe(nazwa, grupa):
    print(f"\n {nazwa} (liczba {len(grupa)}")
    print(f" tak:", sum(1 for x in grupa if x['decyzja'] == 'tak'))
    print(f" nie:", sum(1 for x in grupa if x['decyzja'] == 'nie'))
    print(f" Gini: {round(gini_index(grupa), 3)}")


wiek_value = 50
wiek_lewo = [x for x in dane if x['wiek'] > wiek_value]
wiek_prawo = [x for x in dane if x['wiek'] <= wiek_value]

# gini
print("Gini")
print("Gini (całość)", round(gini_index(dane), 3))
print("Gini po podziale (wiek > 50)", round(gini_po_podziale(wiek_lewo, wiek_prawo), 3))
# Gini (całość) 0.48
# Gini po podziale (wiek > 50) 0.45

zarobi_value = 50
zarobki_lewa = [x for x in dane if x['zarobki'] > zarobi_value]
zarobki_prawa = [x for x in dane if x['zarobki'] <= zarobi_value]
print("Gini po podziale (zarobki > 50)", round(gini_po_podziale(zarobki_lewa, zarobki_prawa), 3))
# Gini po podziale (zarobki > 50) 0.4

print("Entropy")
print("Entropia (całość)", round(entropy_index(dane), 3))
print("Entropia (wiek > 50)", round(entropy_po_podziale(wiek_lewo, wiek_prawo), 3))
print("Entropia (zarobki > 50)", round(entropy_po_podziale(zarobki_prawa, zarobki_lewa), 3))

wypisz_grupe("wiek > 50", wiek_lewo)
wypisz_grupe("wiek =< 50", wiek_prawo)
wypisz_grupe("zarobki =< 50", zarobki_prawa)
wypisz_grupe("zarobki >= 50", zarobki_lewa)

gini_values = [
    gini_index(dane),
    gini_po_podziale(wiek_lewo, wiek_prawo),
    gini_po_podziale(zarobki_lewa, zarobki_prawa)
]

entropy_values = [
    entropy_index(dane),
    entropy_po_podziale(wiek_lewo, wiek_prawo),
    entropy_po_podziale(zarobki_lewa, zarobki_prawa)
]

labels = ["Całość", 'Wiek > 50', "Zarobki > 50"]

x = range(len(labels))
plt.figure(figsize=(10, 5))
plt.bar(x, gini_values, width=0.4, label="Gini", align="center")
plt.bar([i + 0.4 for i in x], entropy_values, width=0.4, label="Entropia", align="center")
plt.xticks([i + 0.2 for i in x], labels)
plt.ylabel("Wartości miary")
plt.title("Porówanie GIni i Entropii")
plt.legend()
plt.tight_layout()
plt.show()
