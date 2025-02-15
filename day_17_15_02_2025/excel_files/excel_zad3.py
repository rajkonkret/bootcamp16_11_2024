import xlrd
from xlwt.Utils import cell_to_rowcol2

person = xlrd.open_workbook('dane_person.xls')
print(person.sheet_names())  # ['Arkusz1']

for sheet in person.sheets():
    print(sheet.name)

# Arkusz1

sheet = person.sheet_by_index(0)
print(sheet.name)  # Arkusz1

sheet = person.sheet_by_name("Arkusz1")
print(sheet.name)  # Arkusz1

print(sheet.nrows)  # 2
print(sheet.ncols)  # 3

print(sheet.cell(1, 0).value)  # Radek
print(sheet.cell(*cell_to_rowcol2("B1")).value)
