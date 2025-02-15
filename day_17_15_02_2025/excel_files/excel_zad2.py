# XlsxWriter

import xlsxwriter
import datetime as dt

book = xlsxwriter.Workbook('xlsxwriter.xlsx')

sheet = book.add_worksheet("Arkusz1")

sheet.write("A1", "Witaj 1")
sheet.write("A2", "Witaj 2")

formatting = book.add_format({"font_color": "#FF0000",
                              "bg_color": "#FFFF00",
                              "bold": True, "align": "center",
                              "border": 1, "border_color": "#FF0000"})
sheet.write("A3", "Witaj 3", formatting)

# formatowanie wartości numerycznych
number_format = book.add_format({"num_format": "0.00"})
sheet.write("A4", 3.33333, number_format)

# foramtowanie daty
date_format = book.add_format({"num_format": "yyyy/mm/dd"})
sheet.write("A5", dt.date(2016, 10, 13), date_format)

# formuły
sheet.write("A6", "=SUM(A4, 2)")


# dodanie obrazka
sheet. insert_image(0,2, "images/djngo_komendy.png")

# wykresy
categories = ['Styczeń', "Luty"]
values = [100, 150]
sheet.write_row("B10", categories)
sheet.write_row("B11", values)

chart = book.add_chart({"type": "column"})
chart.set_title({"name": "Sprzedaż"})
chart.add_series({"name": "=Arkusz1!A11",
                  "categories": "=Arkusz1!B10:C10",
                  "values": "=Arkusz1!B11:C11"})
chart.set_x_axis({"name": "Os X"})
chart.set_y_axis({"name": "Os X"})
sheet.insert_chart("A15", chart)

book.close()
