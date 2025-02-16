import openpyxl

# read_only=True
book = openpyxl.load_workbook("openpyxl_optimized.xlsx",
                              data_only=True,
                              read_only=True,
                              keep_links=False)  # wyłaczenie odnośników
# book.close() # wymagane przy read_only=True
print(book)
for b in book:
    print(b)
    for i in b:
        print(i)

book.close()
