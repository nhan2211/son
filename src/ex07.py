import openpyxl
wb = openpyxl.load_workbook('aloha.xlsx')
ws = wb['Sheet']
ws.cell(row=1, column=1).value = 'ALOHA!'
wb.save('aloha.xlsx')