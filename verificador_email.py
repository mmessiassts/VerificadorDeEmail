import re
import csv

lista_valid_email = [] # lista para armazenar e-mails válidos
lista_invalid_email = [] # lista para armazenar e-mails inválidos

def verificador_de_e_mail(email):
    if re.search(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', email):
        lista_valid_email.append(email)
    else:
        lista_invalid_email.append(email)

ficheiro = "/home/oem/Área de Trabalho/VerificadorEmails/dados.csv"

emails = [] # inicializando a lista de e-mails

with open(ficheiro) as file:
    ler_csv = csv.reader(file)
    for row in ler_csv:
        verificador_de_e_mail(row[2]) # verifica o e-mail na coluna 2
        emails.append(row[2])         # adiciona o e-mail na lista de e-mails

print("E-mails válidos:")
for email in lista_valid_email:
    print(email)

print("\nE-mails inválidos:")
for email in lista_invalid_email:
    print(email)             






