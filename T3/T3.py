
'''
	Trabalho de Calculo numerico
	Integrantes: Gabriel Maciel e Henrique Saenger
'''

#imports
import scipy.integrate as integrate
import scipy
import numpy as np
from sympy import *
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
	x = y = 1
	f = raw_input("Funcao ")
	r = np.array([0,0,0,0,0,0,0,0,0,0,0])

	x0 = int(input("intervalo inferior "))
	x1 = int(input("Intervalo superior "))

	raiz = int(input("Raiz "))

	print(eval(f))


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

forma = raw_input("\nclassica ou intervalar")

if forma=="classica":
	print("Forma classica")
elif forma == "intervalar":
	Intervalar()
else:
	print("Erro")
