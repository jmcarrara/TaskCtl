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
result[nrlinhaInt][6] = 'S'
print("----------------------------\n")
print(result)

res = open('dados.dat', 'w')
for linhas in result:
    linhasStr = str(linhas)
    res.write(linhasStr.replace("[", "").replace("]", "").replace(", ", "|").replace("'", "") + "\n")


#atualiza = open('dados.dat', 'w')
#resultStr = str(result)
#atualiza.write(resultStr)
#atualiza.close
