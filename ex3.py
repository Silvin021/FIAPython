# 1. Abre o arquivo chamado 'dados.txt' para leitura ('r')
arquivo = open('meu arquivo.txt', 'r')

# 2. Pede para você digitar a palavra
busca = input("O que você quer procurar? ")

# 3. Criamos um contador para saber em qual linha estamos
numero_da_linha = 1

# 4. O 'for' vai passar por cada linha do arquivo, uma de cada vez
for linha in arquivo:
    
    # Se a palavra estiver dentro da linha...
    if busca in linha:
        print("Encontrei na linha:", numero_da_linha)
    
    # Soma +1 para a próxima volta do laço
    numero_da_linha = numero_da_linha + 1

# 5. Fecha o arquivo (sempre importante!)
arquivo.close()
