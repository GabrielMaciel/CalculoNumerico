
#region Import
import numpy as np
import matplotlib.pyplot as plt
#endregion 

'''---------------------''
''						''
''		  Funcoes		''
''						''
''----------------------'''

#calcula: Somatorio de X
def calcularSomatorioX(m):
	s = 0
	for i in range(l):
		s = s + m[i][0]
	return s

#calcula: Somatorio de Y
def calcularSomatorioY(m):
	s = 0
	for i in range(l):
		s = s + m[i][1]
	return s

#calcula: Somatorio de X^2
def calcularSomatorioX2(m):
	s = 0
	for i in range(l):
		for j in range(c-1):
			s = s + m[i][j]*m[i][j]
	return s

#Calcula: Somatorio de X*Y
def calcularSomatorioXY(m,colY):
	s = 0
	for i in range(l):
		for j in range(c-1):
			s = s + m[i][j]*m[i][colY-1]
	return s

#divide a matriz XY em um vetor X e um Y
def XYVetor(m):
	vX = [0]*l
	vY = [0]*l
	for i in range(l):
		vX[i]= mat[i][0]
	for i in range(l):
		vY[i]= mat[i][1]
	
	return vX,vY
	


'''---------------------''
''						''
''		   Code 		''
''						''
''----------------------'''

#region init
print ("Trabalho de Calculo numerico")
print ("Nomes: Gabriel Maciel e Henrique")
print ("");print ("");print ("")
#endregion

#leitura de linha e coluna
l = int(input())
c = int(input())

if not( l>0 and c>1):
	print("Numeros minimos da tabela nao foram atingidos, tente com uma tabela de ao menos 1 linha e 2 colunas")
	exit()

#leitura do tipo
s = raw_input()

#Declaracao da matriz
mat = [0]*l		#Matriz para input
vetX = [0]*l	#vetor de X
vetY = [0]*l	#vetor de Y
r = [0]*l 		#Vetor resultado

for k in range(l):
	mat[k] = [0]*c

#Declaracao de variaveis auxiliares
#somatorio
somatX = 0
somatY = 0
#numero de elementos		
n = l
#somatorio de potencias
somatX2 = 0
#somatorio de X*Y
somatXY = 0
#alfa0 e alfa1
a0 = 0
a1 = 0

#leitura dos elementos da matriz
for i in range(c):
	for j in range(l):
		mat[j][i]=float(input())

#repartir a matriz em X e Y
vetX,vetY = XYVetor(mat)

print('Matriz', mat)
print('X', vetX)
print('Y', vetY)

#calculando somatorio
somatX = calcularSomatorioX(mat)
somatY = calcularSomatorioY(mat)
somatX2 = calcularSomatorioX2(mat)
somatXY = calcularSomatorioXY(mat,c)

#Calculando valores
a0 = (n*somatXY - somatX*somatY) / (n*somatX2 - (somatX*somatX))
a1 = (somatX*somatXY - somatY*somatX2) / (somatX*somatX - n*somatX2)

print("")
print("a0")
print(a0)

print("a1")
print(a1)

#MQ
for i in range(l):
	r[i] = a0*vetX[i]+a1
	

plt.plot(vetX,vetY,'ro', vetX,r,'-' )
plt.axis([vetX[0] - 1 ,vetX[l-1] + 1, vetY[0] , vetY[l-1]])

plt.show()