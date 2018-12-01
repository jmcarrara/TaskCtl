from sys import argv
script, nrlinha = argv

nrlinhaInt = int(nrlinha) - 1
result = []

dados = open('dados.dat', 'r')
for linhas in dados:
    linhas = linhas.split("|")
    result.append(linhas)

dados.close()

print(result)
# print (linhas [nrlinhaInt])
result[nrlinhaInt][6] = 'S\n'
print("----------------------------\n")
print(result)


atualiza = open('dados.dat', 'w')
resultStr = str(result)
atualiza.write(resultStr)
atualiza.close
