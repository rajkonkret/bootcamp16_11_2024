from zipfile import ZipFile
import xml.etree.ElementTree as ET

# Otwieramy plik Excel jako ZIP
with ZipFile("tabela_przestawna2.xlsx", "r") as archive:
    with archive.open("xl/sharedStrings.xml") as f:
        xml_content = f.read()

# Parsujemy XML
root = ET.fromstring(xml_content)

# Pobieramy wszystkie wartości tekstowe z sharedStrings.xml
shared_strings = [elem.text for elem in root.findall(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t")]

print("Odczytane wartości tekstowe:", shared_strings)

def convert_index_to_text(index):
    if index.isdigit():
        idx = int(index)
        if idx < len(shared_strings):  # Sprawdzenie, czy indeks mieści się w zakresie
            return shared_strings[idx]
        else:
            # return f"[BŁĄD: brak wartości dla index={idx}]"  # Komunikat o błędzie
            return idx

# Otwieramy sheet1.xml i zamieniamy indeksy na wartości
with ZipFile("tabela_przestawna2.xlsx", "r") as archive:
    with archive.open("xl/worksheets/sheet1.xml") as f:
        sheet_content = f.read()

# Parsujemy XML arkusza
sheet_root = ET.fromstring(sheet_content)

# Przechodzimy przez wszystkie komórki i zamieniamy indeksy na tekst
data = []
for row in sheet_root.findall(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row"):
    row_data = []
    for cell in row.findall(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c"):
        cell_value = cell.find(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v")
        row_data.append(convert_index_to_text(cell_value.text) if cell_value is not None else "")
    data.append(row_data)

# Tworzymy DataFrame
import pandas as pd
df = pd.DataFrame(data)
print(df.head())

df.to_excel("fix2.xlsx", index=False)