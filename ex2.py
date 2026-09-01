arquivo1 = input('digite o nome do primeiro arquivo: ')
arquivo2 = input('digite o nome do segundo arquivo: ')
arquivo_final = input('digite o nome do arquivo de saida: ')

#lendo o conteudo do primeiro
with open(arquivo1, 'r') as f1:
    conteudo1 = f1.read()

#lendo o conteudo do segundo
with open(arquivo2, 'r') as f2:
    conteudo2 = f2.read()

# Criando o terceiro arquivo e gravando a junção dos dois
with open(arquivo_final, 'w') as f_saida:
    f_saida.write(conteudo1 + "\n" + conteudo2)

print(f"Sucesso! O arquivo '{arquivo_final}' foi criado.")