# CONTADOR DE PALAVRAS

arquivo = input("Digite o nome do arquivo: ")

with open(arquivo, 'r') as file:
    texto = file.read()
    palavras = texto.split()
    print(f"O arquivo tem {len(palavras)} palavras.")