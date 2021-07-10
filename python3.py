import csv


with open('users.csv', 'w', encoding="utf-8", newline='') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['Pietro', 'Ribeiro', 'pietro@email.com', 'masculino'])
    