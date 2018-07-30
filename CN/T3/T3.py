
'''
	Trabalho de Calculo numerico
	Integrantes: Gabriel Maciel e Henrique Saenger
'''

#imports
import scipy.integrate as integrate
import scipy
import numpy as np
import matplotlib.pyplot as plt



'''---------------------''
''						''
''		  Funcoes		''
''						''
''----------------------'''

'''
'' 	Classica
'''




'''
''	Intervalar
'''
#Forma intervalar
def Intervalar():
	x = 1
	f = raw_input("Funcao ")
	f1 = raw_input("Funcao derivada ")

	x0 = float(input("intervalo inferior "))
	x1 = float(input("Intervalo superior "))

	i = 0

	#conjunto 
	r = [0.0, 0.0] 
	o = [0.0, 0.0]

	o[0] = r[0] = x0
	o[1] = r[1] = x1


	while abs(abs(r[0]) - abs(r[1])) > 0.001:

		#numero de iteracoes
		i+=1
		#Media 
		mid = (r[0]+r[1])/2

		#calcula cada elemento do conjunto
		x = r[0]
		r[0] = eval(f1)
		x = r[1]
		r[1] = eval(f1)
	#	print("\nEtapa1: Calcular o intervalo na divisao:    ",r)

		#Calcula a parte f(mid[Xk])
		x = mid
		sup = eval(f)

	#	print("\nEtapa2: Calcular a parte superior da divisao:    ", sup)

		#inverte os elementos para multiplicar pela parte superior (Mesma coisa que dividir)
		r[0] = r[0]**(-1)
		r[1] = r[1]**(-1)

		#multiplica pela parte superior
		r[0] = r[0]*sup
		r[1] = r[1]*sup 

	#	print("\nEtapa3: Calcular a divisao:    ",r)


		r[0] = mid - r[0]
		r[1] = mid - r[1]

	#	print("\nEtapa4: Calcular a subtracao:    ",r)

		if o[0] > r[0]:
			r[0] = o[0]
		if o[1] < r[1]:
			r[1] = o[1]
		
		print(r,i)

	print();print()
	print("Resultado    , iteracoes")
	print(r,i)
	


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

Intervalar()
