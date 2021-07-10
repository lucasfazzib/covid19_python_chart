import csv

with open('brasilcovid.csv', 'r', encoding='utf-8') as arquivocsv:
    leitor = csv.reader(arquivocsv)
    header = next(leitor)
    next(leitor)
    for linha in leitor:
        if float(linha[2]) > 1:
            print(linha)

