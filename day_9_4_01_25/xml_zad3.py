from xml.dom import minidom

# DOMTree = minidom.parse("../dane.xml") szuka katalog wyżej
DOMTree = minidom.parse("dane.xml")
print(DOMTree.toxml())
# <?xml version="1.0" ?><znajomi>
#     <osoba>
#         <imie foo="zzz">Zygmunt</imie>
#         <email>1@1.pl</email>
#     </osoba>
#     <osoba>
#         <imie foo="aaaa">Janina</imie>
#         <email>2@2.pl</email>
#     </osoba>
# </znajomi>

cNodes = DOMTree.childNodes
print(cNodes)  # [<DOM Element: znajomi at 0x1966bafb1d0>]
znajomi = cNodes[0]
print("Znajomi:", znajomi)  # Znajomi: <DOM Element: znajomi at 0x1d5c219b1d0>

print(znajomi.getElementsByTagName(
    "osoba"))  # [<DOM Element: osoba at 0x284b52fb650>, <DOM Element: osoba at 0x284b52fb800>]
persons = znajomi.getElementsByTagName("osoba")
print(persons[0].toxml())
# <osoba>
#         <imie foo="zzz">Zygmunt</imie>
#         <email>1@1.pl</email>
#     </osoba>
print(persons[1].toxml())
# <osoba>
#         <imie foo="aaaa">Janina</imie>
#         <email>2@2.pl</email>
#     </osoba>

osoba = persons[0]
imie = osoba.getElementsByTagName("imie")[0]
print(imie)  # [<DOM Element: imie at 0x202882eb6e0>]
imie_1 = imie.firstChild.data
print(imie_1)  # Zygmunt
atrybut = imie.getAttribute("foo")
print(atrybut)  # zzz
