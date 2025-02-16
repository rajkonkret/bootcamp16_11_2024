import xlsxwriter

book = xlsxwriter.Workbook("xlswriter_optimized.xlsx",
                           options={"constant_memory": True})

sheet = book.add_worksheet()
for row in range(1000):
    sheet.write_row(row, 0, list(range(200)))

book.close()
