set term png
set output 'marticia.png'
set xrange [0:9] ##rangos
set yrange [0.1:0.9] ##rangos
set zrange [0.1:0.9] ##rangos
set xlabel "Potencia de 2" ##labes
set ylabel "Fre de 0"
set zlabel "% pase 0 u 1"
set pm3d implicit at s ##para los colores y paleta
splot 'canal.dat'
