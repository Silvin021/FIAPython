#abre o arquivo no modo de leitura ('r')

with open('arquivo.txt','r')as file:
    #le todo o conteudo do arquivo
    conteudo = file.read()
    print(conteudo)

#abre o arquivo no modo de leitura ('r')
with open('arquivo.txt', 'r') as file:
    #le a primeira linha do arquivo
    linha1 = file.readline()
    #le a segunda linha do arquivo
    linha2 = file.readline()
    #le a terceira linha do arquivo
    linha3 = file.readline()
    
    print(linha1)
    print(linha2)
    print(linha3)