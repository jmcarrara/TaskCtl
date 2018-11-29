target = open('dados.dat', 'r')
listar = target.read()
print(listar.replace("|"," "))
target.close()
