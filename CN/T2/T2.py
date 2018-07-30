
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
	Metodos gerais
'''



'''
	Integracao
'''

#Inicio
def integral(x0,x1):
	#Seleciona o tipo de equacao
	if tipo == "trapezio":
		Trapezio(x0,x1)
	elif tipo == "simpson":
		Simpson(x0,x1)
	elif tipo == "romberg":
		Romberg(f,x0,x1)

	return 0;


'''
		Trapezios
'''

#Integrar
def integrar(f,a,b,N=0.1):
	i = a
	s = 0
	iterations = 0
	while i <= b:
		iterations+=1
		x = i
		i += N
		s += eval(f)

	r = float(s/iterations)

#calcula f(x)    [x4]
def fx(xi):
	x= xi
	r = eval(f)

	return r

#integral de x0 e x1 trapezio
def iF():

	h = x1 - x0
	step1 = h/2
	step2 = fx(x0) + fx(x1)

	r = step1*step2

	return r

#Define erro Trapezio
def erro(f2):

	h = x1 - x0
	x = Symbol('x')
	#*(-(h*h*h/12))
	s1 = f2
	x = (x1-x0)/2
	r = eval(s1) *(-(h*h*h/12))

	return r
	
#Calcula trapezio
def Trapezio(x0,x1):

	result = iF()

	#Resultado
	print("tR = ", result)

	#Erro
	try:
		f2 = raw_input("f''")
		if f2 != "" and f2 != 'EOF':
			print("E = ", erro(f2))
		else:
			print("\n\nsem f'' = sem calculo de erro")
	except IOError as e:
		print("sem funcao  = sem calculo do erro")



	return 0


'''
		Simpson
'''


#Simpson
def Simpson(x0,x1):

	#Calcula h
	h = (x1-x0)/2
	
	#Define os 3 x que sao usados na funcao
	xa = x0
	xb = x0 + h
	xc = x1

	#calcula a funcao passo a passo [ (h/3) * (f(x0)+f(x1)+f(x2)) ]
	#Try para evitar divisao por 0
	try:
		s1 = h/3
		x = xa
		s2 = eval(f)
		
		x = xb
		s3 = eval(f)*4

		x = xc
		s4 = eval(f)
	
		Is = s1 *(s2+s3+s4)
		print ("Is = {0} ".format(Is))
		plt.plot(Is)
		
	except ZeroDivisionError as detail:
		print(detail)
	#resultado
	
	x = xa
	Es = (-(h**5)/90 )*eval(f)
	print("Es = ", Es)

	
	return 0

'''
		Romberg
'''

def trapezcomp(f, a, b, n):

 	h = (x1 - x0) / n
 	x = x0
 
    # Regra

	In = eval(f)
	for k in range(1, n):
	    x  = x + h
	    In += 2*eval(f)
		
	x = x1
	return (In + eval(f))*h*0.5

def Romberg(fun,x0,x1):

	p=3
	I = np.zeros((p, p))
	for k in range(0, p):
	    # Composite trapezoidal rule for 2^k panels
	    I[k, 0] = trapezcomp(f, x0, x1, 2**k)

	    # Romberg recursive formula
	    for j in range(0, k):
	        I[k, j+1] = (4**(j+1) * I[k, j] - I[k-1, j]) / (4**(j+1) - 1)

	    #print(I[k,0:k+1])   # display intermediate results
 	
 	print(I)
	return I



'''
def Romberg1(fun,x0,x1):
	e = 2.7182
	n = int(input())
	r = np.array([[0]*(n)]*(n),float)

	h = x1-x0

	#R00
	x = x0
	s1 = eval(f)
	x=x1
	s2 = eval(f)

	# r00 = h*(f(a)*f(b))/2
	r[0,0] = h * 0.5 * (s1+s2)

	#R10
	s = 0.0
	for k in range(1,2):
		x = x0 + (k - 0.5) * h
		s+= eval(fun)

	r[1,0] = 0.5 * ( r[0,0] + h * s )



	#R20
	#h = h*0.125

	s = 0.0
	for k in range(1,3):
		x = x0 +(k-0.5) * h
		s+= eval(fun)

	r[2,0] = 0.5 * ( r[0,0] + h * s )

	
	#R11
	r[1,1] = (4 * r[1,0] - r[0,0]) / (4-1)


	#R21
	r[2,1] = (4 * r[2,0] - r[1,0])  / (4-1)


	#R22
	r[2,2] = ((4**2)*r[2,1]-r[1,1])/(4**2-1)


	s = 0.0
	for k in range(1,2**(2-1)):
		x = x0 +(2*k-1)*h
		s+= eval(fun)

	r[2,0] = (1/2) * r[0,0] + h * s


	print (r)


	return 0
'''


#Romberg V1
'''
def Romberg2(fun,x0,x1):
	e = 2.7182
	n = int(input())
	r = np.array([[0]*(n+1)]*(n+1),float)
	h = x1-x0
	x = x0
	s1 = eval(fun)
	x = x1
	s2 = eval(fun)
	r[0,0] = (1/2) * h*(s1+s2)
	


	p2 = 1
	
	for i in xrange(0, 3):

		h = h/2
		s = 0.0
		p2 = 2 * p2
		for k in xrange(1, p2, 2):
			x = x0 + k * h
			s = s + eval(fun)

		r[i,0] = 0.5 * r[i-1,0] + s*h

		p4 = 1

		for j in xrange(1, i+1):
			p4 = 4*p4
			r[i,j] = r[i,j-1]+(r[i,j-1] - r[i-1,j-1])/(p4-1)


	print (r)

	return r
'''
'''
	Derivacao
'''

#progressiva


#regressiva


#centrada




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

#deriv ou integ?
s=""
while(s!="a" and s!="b"):
	s = raw_input("a)derivada\nb)integral\n\t")

if(s=="a"):
	derivada()
else :
	#Input de X0 e X1 [intervalos]
	x0 = float(input("X0 "))
	x1 = float(input("\n\tX1 "))
	x = 1
	e = 2.7182
	#input da formula
	f = raw_input("\n\tformula ")

	#input da equacao  [trapezio, simpson, romberg]
	tipo = raw_input("\n\tregra \n")

	integral(x0,x1)
