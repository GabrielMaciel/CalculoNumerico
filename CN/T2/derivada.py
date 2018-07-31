# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

## FUNCOES

#função a ser derivada
def funcao(x):
    resultado=-0.1*pow(x,4)-0.15*pow(x,3)-0.5*pow(x,2)-0.25*x + 1.2            #resolve da função dada(tem que colocar na mão)
    return resultado      


###############PROGRESSIVA################
###PRIMEIRA DERIVADA PROGRESSIVA
#primeira derivada 1
def pderivada11(x,h):
    derivada=(funcao(x+h)-funcao(x-h))/(2*h)
    return derivada
#primeira derivada 2
def pderivada12(x,h):
    derivada=(-funcao(x+(2*h))+4*funcao(x+h)-3*funcao(x))/(2*h)
    return derivada

###SEGUNDA DERIVADA PROGRESSIVA
#segunda derivada 1
def pderivada21(x,h):
    derivada=(funcao(x+(2*h))-2*funcao(x+h)+funcao(x))/pow(h,2)
    return derivada
#segunda derivada 2
def pderivada22(x,h):
    derivada=(-funcao(x+(2*h))+4*funcao(x+(2*h))-5*funcao(x+h)+2*funcao(x))/pow(h,2)
    return derivada

###TERCEIRA DERIVADA PROGRESSIVA
#terceira derivada 1
def pderivada31(x,h):
    derivada=(funcao(x+(3*h))-3*funcao(x-(2*h))+3*funcao(x+h)-funcao(x))/pow(h,3)
    return derivada
#terceira derivada 2
def pderivada32(x,h):
    derivada=(-3*funcao(x+(4*h))+14*funcao(x+(3*h))-24*funcao(x+(2*h))+18*funcao(x+h)-5*funcao(x))/(2*pow(h,3))
    return derivada
###QUARTA DERIVADA PROGRESSIVA
#quarta derivada 1
def pderivada41(x,h):
    derivada=(funcao(x+(4*h))-4*funcao(x+(3*h))+6*funcao(x+(2*h))-4*funcao(x+h)+funcao(x))/pow(h,4)
    return derivada
#quarta derivada 2
def pderivada42(x,h):
    derivada=(-2*funcao(x+(5*h))+11*funcao(x+(4*h))-24*funcao(x+(3*h))+26*funcao(x+(2*h))-14*funcao(x+h)+3*funcao(x))/pow(h,4)
    return derivada

###############REGRESSIVA################
###PRIMEIRA DERIVADA REGRESSIVA
#primeira derivada 1
def rderivada11(x,h):
    derivada=(funcao(x)-funcao(x-h))/h
    return derivada
#primeira derivada 2
def rderivada12(x,h):
    derivada=(3*funcao(x)-4*funcao(x-h)+funcao(x-(2*h)))/(2*h)
    return derivada
###SEGUNDA DERIVADA REGRESSIVA
#segunda derivada 1
def rderivada21(x,h):
    derivada=(funcao(x)-2*funcao(x-h)+funcao(x-(2*h)))/pow(h,2)
    return derivada
#segunda derivada 2
def rderivada22(x,h):
    derivada=(2*funcao(x)-5*funcao(x-h)+4*funcao(x-(2*h))-funcao(x-(3*h)))/pow(h,2)
    return derivada
###TERCEIRA DERIVADA REGRESSIVA
#terceira derivada 1
def rderivada31(x,h):
    derivada=(funcao(x)-3*funcao(x-h)+3*funcao(x-(2*h))-funcao(x-(3*h)))/pow(h,3)
    return derivada
#terceira derivada 2
def rderivada32(x,h):
    derivada=(5*funcao(x)-18*funcao(x-h)+24*funcao(x-(2*h))-14*funcao(x-(3*h))+3*funcao(x-(4*h)))/(2*pow(h,3))
    return derivada
###QUARTA DERIVADA REGRESSIVA
#quarta derivada 1
def rderivada41(x,h):
    derivada=(funcao(x)-4*funcao(x-h)+6*funcao(x-(2*h))-4*funcao(x-(3*h))+ funcao(x-(4*h)))/pow(h,4)
    return derivada
#quarta derivada 2
def rderivada42(x,h):
    derivada=(3*funcao(x)-14*funcao(x-h)+26*funcao(x-(2*h))-24*funcao(x-(3*h))+11*funcao(x-(4*h))-2*funcao(x-(5*h)))/pow(h,4)
    return derivada


###############CENTRADA################
###PRIMEIRA DERIVADA CENTRADA
#primeira derivada 1
def cderivada11(x,h):
    derivada=(funcao(x+h)-funcao(x-h))/(2*h)
    return derivada
#primeira derivada 2
def cderivada12(x,h):
    derivada=(-funcao(x-(2*h))+8*funcao(x+h)-8*funcao(x-h)+funcao(x-(2*h)))/(12*h)
    return derivada
###SEGUNDA DERIVADA CENTRADA
#segunda derivada 1
def cderivada21(x,h):
    derivada=(funcao(x+h)-2*funcao(x)+funcao(x-h))/pow(h,2)
    return derivada
#segunda derivada 2
def cderivada22(x,h):
    derivada=(-funcao(x-(2*h))+16*funcao(x+h)-30*funcao(x)+16*funcao(x-h)-funcao(x-(2*h)))/(12*pow(h,2))
    return derivada
###TERCEIRA DERIVADA CENTRADA
#terceira derivada 1
def cderivada31(x,h):
    derivada=(funcao(x+(2*h))-2*funcao(x+h)+2*funcao(x-h)-funcao(x-(2*h)))/(2*pow(h,3))
    return derivada
#terceira derivada 2
def cderivada32(x,h):
    derivada=(-funcao(x+(3*h))+8*funcao(x+(2*h))-13*funcao(x+h)+13*funcao(x-h)-8*funcao(x-(2*h))+funcao(x-(3*h)))/(8*pow(h,3))
    return derivada
###QUARTA DERIVADA CENTRADA
#quarta derivada 1
def cderivada41(x,h):
    derivada=(funcao(x+(2*h))-4*funcao(x+h)+6*funcao(x)-4*funcao(x-h)+funcao(x-(2*h)))/pow(h,4)
    return derivada
#quarta derivada 2
def cderivada42(x,h):
    derivada=(-funcao(x+(3*h))+12*funcao(x+(2*h))-39*funcao(x+h)+56*funcao(x)-39*funcao(x-h)+12*funcao(x-(2*h))-funcao(x-(3*h)))/(6*pow(h,4))
    return derivada    
    

    
    
##############################EXECUCAO##########################################

#x=float(input())
#h=float(input())
x=0.5       #exemplo1
h=0.25      #exemplo1

print('{}'.format(cderivada11(x,h)))
print('{}'.format(cderivada12(x,h)))





