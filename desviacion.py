import math ##para la raiz
archivo=open("desviacion.dat","r") ##abrimos archivo 
res = [] ##una lista para valores mas adelante
lineas=archivo.readlines() ##cuantas lineas tiene
suma = 0 ##para promedios
contador = 0 ##para promedios
for x in lineas:
	suma = suma + float(x)	##sumamos todos los valores
	contador = contador + 1

promedio = suma/contador ##sacamos el promedio de los valores
print "Media aritmetica: ",promedio
res = 0
sumad = 0
for x in lineas:
	#res.append(float(x) - promedio)	
	cuadrado = (float(x) - promedio)**2 ##para la desviacion es
					    ##la diferencia de todos los numeros con el
				            ##promedio  al cuadrado mas sus sumas nos da
					    ##la varianza
					    ## y la raiz de esta es el desviacion
	sumad = sumad + cuadrado
promediod = sumad/contador
print "Varianza: ",promediod
raiz = math.sqrt(promediod)
print "Desviacion estandar: ",raiz
archivo.close
