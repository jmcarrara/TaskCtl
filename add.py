from sys import argv
script, data, setor, tipo, usuario, descricao, finalizado = argv

contador = open('contador.dat', 'r')
contadorInt = int(contador.read())
contadorInt = contadorInt + 1

contadorStr = str(contadorInt)

contadorUpt = open('contador.dat', 'w')
contadorUpt.write(contadorStr)
contadorUpt.close

target = open('dados.dat', 'a')

linha = contadorStr + '|' + data + '|' + setor + '|' + tipo + '|' + usuario + '|' + descricao + '|' + finalizado.upper() + '\n'

target.write(linha)
target.close
