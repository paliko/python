import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Expenses02.xlsx')
worksheet = workbook.add_worksheet()


for radek in range(100):
    worksheet.write(radek,0,f"Ja jsem radek {radek}")

workbook.close()