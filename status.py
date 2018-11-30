target = open('dados.dat', 'r')
listar = []
for linha in target.readlines():
    ponteiro = [value for value in linha.split("|")]
    listar.append(ponteiro)
target.close()
print(listar[19])
listar.insert[7] = "S"
print(listar[19])
print(listar[7])
for x in listar:
    print (x)
