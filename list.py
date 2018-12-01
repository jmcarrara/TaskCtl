dados = open('dados.dat', 'r')
listar = dados.read()
print(listar.replace("|"," "))
dados.close()
