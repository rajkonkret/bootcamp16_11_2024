from openpyxl import load_workbook

wb = load_workbook("tabela_przestawna2.xlsx")


wb.save("tabela_przestawna3.xlsx")