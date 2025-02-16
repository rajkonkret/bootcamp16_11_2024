import xlwt
import xlrd
from xlutils.copy import copy

book = xlrd.open_workbook("xlwt.xls", formatting_info=True)
book = copy(book)
book.get_sheet(0).write(0, 0, "zmienione")

book.save("edited.xls")
