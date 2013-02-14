
REPE=10 ##maximo de repeticiones
cosa=canal.dat
tiocosa=mugre.dat
tiolucas=desviacion.dat

##para ver si existen los archivos
##si es asi los borra
##agradecimiento a pedrito por 
##esta parte

if [ -e $cosa ]; then
	rm canal.dat
fi
if [ -e $tiocosa ]; then
	rm mugre.dat
fi
if [ -e $tiolucas ]; then
	rm desviacion.dat
fi


touch canal.dat
touch desviacion.dat


for POTENCIA in 0 1 2 3 4 5 6 7 8
do
	for PCERO in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 ##porcentajes de aparicion
	do
		for PECERO in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 ##posibilidades de exito cero y uno
		do
			for CONTADOR in 1 2 3 4 5 ##cuantas palabras de un mismo tamaño se aran para sacar el promedio luego
			do
			        touch mugre.dat
				res=`python canal.py $PCERO $POTENCIA $PECERO $PECERO $REPE`
			        echo $res >> mugre.dat
			done
			res=`awk -f cosa.awk mugre.dat`
			echo valor de res $res
			rm mugre.dat
			echo $POTENCIA $PCERO $PECERO $res >> canal.dat
			echo $res >> desviacion.dat
		done
	done
	echo '' >> canal.dat
	echo $POTENCIA
done
python desviacion.py
gnuplot grafica.plot
