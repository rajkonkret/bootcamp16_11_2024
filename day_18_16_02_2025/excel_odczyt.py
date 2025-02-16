import xlrd

with xlrd.open_workbook("xlwt.xls", on_demand=True) as book:
    sheet = book.sheet_by_index(0)

print(sheet)  # Sheet  0:<Arkusz1>
print(sheet.nrows)  # liczba wierszy 6
