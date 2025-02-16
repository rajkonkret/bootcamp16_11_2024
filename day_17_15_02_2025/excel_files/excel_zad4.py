import xlwt
from xlwt.Utils import cell_to_rowcol2
import datetime as dt

book = xlwt.Workbook()

sheet = book.add_sheet("Arkusz1")

sheet.write(*cell_to_rowcol2("A1"), "Witaj 1")
sheet.write(r=1, c=0, label="Witaj 2")

formtting = xlwt.easyxf("font: bold on, color red;"
                        "align: horiz center;"
                        "borders: top_color red, bottom_color red,"
                        "right_color red, left_color red,"
                        "left thin, right thin,"
                        "top thin, bottom thin;"
                        "pattern: pattern solid, fore_color yellow;")
sheet.write(r=2, c=0, label="Witaj 3", style=formtting)

number_format = xlwt.easyxf(num_format_str="0.00")
sheet.write(3, 0, 3.33333, number_format)

date_format = xlwt.easyxf(num_format_str="yyyy/mm/dd")
sheet.write(4, 0, dt.datetime(2012, 2, 3), date_format)

sheet.write(5, 0, xlwt.Formula("SUM(A4, 2)"))

# sheet.insert_bitmap("images/pict.bmp", 0, 2)
book.save('xlwt.xls')
