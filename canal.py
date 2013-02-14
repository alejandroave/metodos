import random
import sys
import numpy
from numpy import*



def palabra(frecuencia,tama):
	tamano = int(tama)
	vec = zeros(tamano)
	for i in range(tama):
		proba = random.random()
		if proba <= frecuencia:
			vec[i] = 0
		else:
			vec[i] = 1	
	return vec


def transmisor(cpalabra,probc,probou):
	tamp = len(cpalabra)
	vec = zeros(tamp)
	for i in range(tamp):
		pre = random.random()	
		if cpalabra[i] == 0:
			if pre <= probc:
				vec[i] = 0
			else:
				vec[i] = 1
		else:
			if pre <= probou:
				vec[i] = 1
			else:
				vec[i] = 0
	if list(cpalabra) == list(vec):
		return 1
	else:
		return 0


def simulacion(cpalabra,probc,probou,repeticion):
	cont = 0
	for i in range(repeticion):
		corrc = transmisor(cpalabra,probc,probou)
		if corrc == 1:
			cont = cont + 1
	probabilidad = float(cont)/float(repeticion)
	return probabilidad



#def main():

frec = float(sys.argv[1])  ##frecuencia que aparesca cero
tama = 2**int(sys.argv[2])  ##tamao de la letra
probc = float(sys.argv[3]) ##probabilidad de que pase cero
probou = float(sys.argv[4]) ##probabilidad de que pase uno 
repe = int(sys.argv[5])  ##repeticiones
word = palabra(frec,tama) ##para obtener la palabra
prob = simulacion(word,probc,probou,repe) ##optener la probabilidad
print prob ##imprimir la respuestao
#main()


