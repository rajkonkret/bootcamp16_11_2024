# optymalizacja przy pracy z duzymi plikami
import openpyxl
# write_only=True efektywniej zarządza zużyciem pamięci
import lxml  # przyspiesa proces zapisu

book = openpyxl.Workbook(write_only=True)
# przy write_only=True nie zadziała book.active
sheet = book.create_sheet()

# 1000 x 200 komórek
for row in range(1000):
    sheet.append(list(range(200)))

book.save("openpyxl_optimized.xlsx")
