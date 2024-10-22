import openpyxl

def exibir_titulo_planilha(path):
    arquivo = openpyxl.load_workbook(path)
    planilhas = [sheet.title for sheet in arquivo.worksheets]
    return planilhas