with open('meu arquivo.txt', 'w') as file:
    file.write('Olá Mundo!\n')
    file.write('Esse é um arquivo de texto\n')
    file.write('Criado por silvio neto\n')

with open('meu arquivo.txt', 'r+')as file:
    conteudo = file.read
    print(conteudo)



