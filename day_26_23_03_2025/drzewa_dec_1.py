def decyzja_po_ifach(wiek, zarobki):
    # if wiek > 30 and zarobki > 40000:
    #     return "Pożyczka przyznana"
    # else:
    #     return "pożyczka odrzucona"
    if wiek > 50:
        if zarobki > 60_000:
            return "Pożyczka przyznana"
        else:
            return "Pożyczka odrzucona"
    else:
        if wiek > 30:
            if zarobki > 40_000:
                return "Pożyczka przyznana"
            else:
                return "Pożyczka odrzucona"
        else:
            return "Pożyczka odrzucona"


print(decyzja_po_ifach(30, 40000))  # pożyczka odrzucona
print(decyzja_po_ifach(55, 70000))  # Pożyczka przyznana
print(decyzja_po_ifach(25, 100000))  # Pożyczka odrzucona
print(decyzja_po_ifach(45, 35_000))  # Pożyczka odrzucona
print(decyzja_po_ifach(45, 60_000))  # Pożyczka przyznana
#          Czy wiek > 50?
#            /       \
#          Tak        Nie
#         /             \
# Czy zarobki>60?   Czy wiek>30?
#     /    \             /    \
#   Tak   Nie         Tak     Nie
#  (OK)  (NIE)     Czy zarobki>40?  \
#                          /   \     \
#                        Tak  Nie   (NIE)
#                       (OK) (NIE)
