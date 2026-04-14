#abrir um arquivo para escrita
with open('arquivo.txt', 'w') as file:
    file.write('Ola mundo!')

#abrir um arquivo para leitura e escrita
with open('arquivo.txt','r+') as file:
    conteudo = file.read()
    file.write('\nAdcionando mais conteudo. ')

 #abrir um arquivo para anexo
with open('arquivo.txt', 'a') as file:
    file.write('\nMais uma linha no final do arquivo. ')   

#abre o arquivo em modo de escrita(w)
with open('arquivo.txt', 'w') as file:
    #escreve no arquivo
    file.write('Line 1\n')    
    file.write('Line 2\n')    
    file.write('Line 3\n')    