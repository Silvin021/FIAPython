with open("arquivo1.txt", "w") as file:
    file.write("Arquivo de teste\n")
    file.write("Z, para testar o programa\n")
    file.write("S de silvio\n")

with open("arquivo1.txt", "r") as file:
    conteudo1 = file.read().splitlines()
conteudo1.sort()

with open("arquivo_ordenado.txt", "w") as file2:
    for linha in conteudo1:
        file2.write(linha + "\n")

with open("arquivo_ordenado.txt", "r") as file2:
    conteudo_ordenado = file2.read()
print(conteudo_ordenado)
