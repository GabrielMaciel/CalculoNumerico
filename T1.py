'''
	Trabalho de Calculo numerico
	Integrantes: Gabriel Maciel e Henrique Saenger

'''
#region Import
import numpy as np
import matplotlib.pyplot as plt
#endregion 

'''---------------------''
''						''
''		  Funcoes		''
''						''
''----------------------'''

#Calculos de somatorio simples e polinomial
#calcula: Somatorio de X
def calcularSomatorioX(m):
	s = 0
	for i in range(l):
		s = s + m[i][0]
	return s

def calcularSomatorioXVet(m, nX):
	s = 0
	for i in range(nX):
		s = s + m[i]
	return s

#calcula: Somatorio de Y
def calcularSomatorioY(m):
	s = 0
	for i in range(l):
		s = s + m[i][1]
	return s

#calcula: Somatorio de Y
def calcularSomatorioY(m, nX):
	s = 0
	for i in range(nX):
		s = s + m[i]
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

#Calcula: Somatorio de X*Y
def calcularSomatorioXYMulti(x,y,nX):
	s = 0
	
	for i in range(nX):
		s = s + x[i]*y[i]
	return s

#Calculos de somatorio multiplo
def calcularSomatorioXX(x1,x2):
	soma = 0
	for i in range(c):
		soma += x1[i]*x2[i]

	return soma

#divide a matriz XY em um vetor X e um Y
def XYVetor(m):
	vX = [0]*l
	vY = [0]*l

	if l>2 or s == "linear multiplo":
		for i in range(l-1):
			vX[i] = [0]*c

	for i in range(l):
		vX[i] = [0]*c-1
		for j in range(c-1):
			vX[i]= m[i][j]
	for i in range(l):
		vY[i]= m[i][1]
	
	return vX,vY

#retorna o maior valor do vetor
def maiorValor(vet, l):
	m = vet[0]
	for i in range(l):
		if (m > vet[i]):
			m = vet[i]
	return m

#retorna o menor valor do vetor
def menorValor(vet, l):
	m = vet[0]
	for i in range(l):
		if (m < vet[i]):
			m = vet[i]
	return m

#calcula o vetor resultante Multiplo de alpha
def calculaAlpha(m, x, y):
	#Alpha auxiliar
	a = [0]*l

	i = l-1

	#Calcular
	while i >= 0:
		for j in range(i-1):
			if j == l:
				a[i] += m[i][y]/m[i][j]
			else:
				a[i] += -a[j]*m[i][j]
		i -= 1

	return a


#Retorna a matriz depois de GAUSS
def GAUSS(matA, n):
	print("Gauss Entrada:")
	print(matA)

	#Declara matriz final 
	matI = [0]*(l)
	for k in range(l):
		matI[k] = [0]*(l+1)

	# | 1 2 3 |
	# | 4 5 6 |
	# | 2 5 1 |

	matI = matA


	#Calculo de Gaus 
	#Faz a matriz superior
	for i in range(n-1):
		#Cada linha
		for k in range(i+1,n):
			#escolhe o base  
			base = matA[k][i]/matI[i][i]
			#Calcula cada elemento
			for j in range(i,l+1):
				print("i: {2} k: {0} j: {1} base{3}".format(k,j,i,base))
				matI[k][j] = matI[k][j] - matI[i][j]*base
			print("k:{0}  mat: {1}".format(k,matA[k]))


	print("Matriz resultante")
	print(matI)

	return matI

def LinearSimples():
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
	b = 0
	#leitura dos elementos da matriz
	for i in range(c):
		for j in range(l):
			mat[j][i] = float(input())
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
	print("a0 = {0}".format(a0))
	print("")
	print("a1 = {0}".format(a1))
	print("")
	print("r = {0}*x+{1}".format(a0,a1))
	#MQ
	if s=="linear simples":
		for i in range(l):
			r[i] = a0*vetX[i]+a1
	elif s=="linear multiplo":
		for i in range(l):
			r[i] = a[0]*vetX[i]*vetX[i]+a[1]*vetX[i]+a[2]
		
	plt.plot(vetX,vetY,'ro', vetX,r,'-')
	plt.axis([vetX[0] - 1 ,vetX[l-1] + 1,maiorValor(vetY,l)*0.8, menorValor(vetY,l)*1.2])
	plt.show()
	return 1

def LinearMultiplo():

	#declara matriz
	mat = [0]*l
	for i in range(l):
		mat[i] = [0]*c

	#leitura dos elementos da matriz
	for i in range(l):
		for j in range(c):
			mat[i][j] = float(input())

	print(mat)
	#Valores dos coeficientes
	alpha = [0]*l

	#Matriz Resultante
	matR = [0]*(l)
	for i in range(l):
		matR[i] = [0]*(l+1)

	#n
	matR[0][0] = l
	#Y
	matR[0][l] = calcularSomatorioY(mat[l-1],c)

	for i in range(1,l):
		matR[i][0] = calcularSomatorioXVet(mat[i-1], c)
		matR[0][i] = calcularSomatorioXVet(mat[i-1], c)
		matR[i][l] = calcularSomatorioXX(mat[i-1],mat[l-1])

	matR[0][l] = calcularSomatorioXVet(mat[l-1], c)

	for i in range(1,l):
		for j in range(1,l+1):
			 matR[i][j] = calcularSomatorioXX(mat[i-1], mat[j-1])

	print(matR)

	MF = GAUSS(matR, l)
	
	alpha = calculaAlpha(MF,l,l+1)
	
	print(alpha)

	return 0

def LinearPolinomial():



	return 0




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
c = int(input())
l = int(input())

if not( l>0 and c>1):
	print("Numeros minimos da tabela nao foram atingidos, tente com uma tabela de ao menos 1 linha e 2 colunas")
	exit()


#leitura do tipo
s = raw_input()

if s == "linear simples":
	LinearSimples()

#Caso multiplo
elif s == "linear multiplo":
	LinearMultiplo()

elif s == "linear polinomial":
	LinearPolinomial()

else:
	GAUSS(mat, l)