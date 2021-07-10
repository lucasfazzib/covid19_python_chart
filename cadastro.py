import csv


header = ['nome', 'sobrenome']
dados = []

opt = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')
while opt != '0':
    nome = input('Qual é o seu nome?')
    sobrenome = input('Qual é o seu sobrenome?')
    dados.append([nome, sobrenome])
    opt = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')

print(dados)

with open('users2.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerows(dados)

with open('users2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)

