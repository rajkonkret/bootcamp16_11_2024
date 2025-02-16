from openpyxl import Workbook
import openpyxl

wb = Workbook()
ws = wb.active
ws.title = "Dane"

data = [
    ["Data", "Kategoria", 'Produkt', "Sprzedaż"],
    ["2024-01-01", "Elektronika", "Telefon", 1500],
    ["2024-01-02", "Elektronika", "Telefon", 1500],
    ["2024-01-02", "Odzież", "Koszula", 50],
    ["2024-01-03", "Odzież", "Kurtka", 200],
    ["2024-01-04", "Elektronika", "Laptop", 3200],
]

for row in data:
    ws.append(row)

pivot_ws = wb.create_sheet("Tabela Przestawna")

wb.save("tabela_przetawna.xlsx")
