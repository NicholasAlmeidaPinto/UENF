#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 22:01:10 2018

@author: Nicholas de Almeida Pinto
"""

from mpmath import e1
import numpy as np
import matplotlib.pyplot as plt

#FUNCAO QUE CALCULA A VARIACAO DE PRESSAO 
#Para mudar para anp, mudar para True. 
#Calculo sem fator de pelicula, mudar ultimo termo para 0
def pressao(anp, q, B, mi, k, h, rw, ct, phi, r, t, S):
    if t == 0:
        return 0;

    if anp:
        ctd = k*0.0003484/(phi*mi*ct*rw*rw)
        cpd = k*h/(q*B*mi*19.03)
    else:
        ctd = k*0.0002637/(phi*mi*ct*rw*rw)
        cpd = k*h/(q*B*mi*141.2)

    x  = (r*r/(rw*rw))/(4*ctd*t)

    Pd = float(e1(x))/2
    if r == rw:
        DeltaPressao = Pd/cpd + S/cpd
    else:
        DeltaPressao = Pd/cpd
    return DeltaPressao
######################################################
    


    
espaco = np.arange(1, 10001, 1)
Pressao = np.empty(espaco.size)

pi = 2200
for t in range(1000):
    for i in range(espaco.size):
        Pressao[i] = pi - pressao(False, 100, 1.08, 1, 75, 20, 1, 0.00001, 0.2, espaco[i], t, 5)
        Pressao[i] = Pressao[i] - pressao(False, 100, 1.08, 1, 75, 20, 1, 0.00001, 0.2, espaco.size - espaco[i], t, 1.7)
         
    fig, ax = plt.subplots()
    plt.plot(espaco, Pressao)
    plt.ylim([2000, 2200])
    plt.title("Tempo: " + str(t))
    nome = str(t)+".png"
    plt.savefig("figure/" + nome)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
