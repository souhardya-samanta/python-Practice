import openpyxl as xl
wb = xl.load_workbook("new.xlsx")
sheet = wb['Sheet1']
sheet.cell(1, 8).value = "Rounded Total"
wb.save("head.xlsx")
