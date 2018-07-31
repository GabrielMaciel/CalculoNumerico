import numpy as np
import matplotlib.pyplot as plt

############FUNCOES

#calcula o somatorio de X
def somatorioPolix(m,l):
    s=0
    for i in range(l):
        s+= m[i][0]
    return s

#calcula o somatorio de Y
def somatorioPoliy(m,l):
    soma=0
    for i in range(l):
        soma+=m[i][1]
    return soma

#calcula o somatorio de X*Y
def somatorioPolixy(m,l):
    soma=0
    for i in range(l):
        soma+=m[i][0]*m[i][1]
    return soma

#calcula o somatorio exponencial
def somatorioPolixexp(m,l,exp):
    soma=0
    for i in range(l):
        soma+=pow(m[i][0],exp)
    return soma

#calcula somatorio X^2*Y
def somatorioPoliX2Y(m,l):
    soma=0
    for i in range(l):
        soma+=(pow(m[i][0],2))* m[i][1]
    return soma






#############################EXECUCAO###########################################
l=5



#matriz original
mat=[[0.00,0.25],[0.50,0.75],[1.00,1.0000],[1.2840,1.6487],[2.1170,2.7183]]
x = [0]*l
y = [0]*l

for i in range(l):
	x[i] = mat[i][0]
	y[i] = mat[i][1]
#matriz resultante
matriz = [0]*(3)
for i in range(3):
	matriz[i] = [0]*(3)


#matriz Y
Y=np.zeros(3, dtype=float)


#calcula a matriz resultante de X
matriz[0][0]=l*2
matriz[0][1]=somatorioPolix(mat,l)
matriz[0][2]=somatorioPolixexp(mat,l,2)
matriz[1][0]=somatorioPolix(mat,l)
matriz[1][1]=somatorioPolixexp(mat,l,2)
matriz[1][2]=somatorioPolixexp(mat,l,3)
matriz[2][0]=somatorioPolixexp(mat,l,2)
matriz[2][1]=somatorioPolixexp(mat,l,3)
matriz[2][2]=somatorioPolixexp(mat,l,4)

#calcula a matriz resultante de Y
Y[0]=somatorioPoliy(mat,l)
Y[1]=somatorioPolixy(mat,l)
Y[2]=somatorioPoliX2Y(mat,l)

#calcula a inversa da matriz resultante de X

mR =(np.matrix(matriz)).I

#calcula o alph
alpha =np.matmul(mR,Y)

r=[0]*l

for i in range(l):
    r[i] = ((alpha[0,2])*((x[i])**2)) + (alpha[0,1])*x[i] + alpha[0,0]
plt.plot(x,y,'ro',r,r,'-')
	
plt.show()
