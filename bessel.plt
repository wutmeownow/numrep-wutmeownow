# a simle gnuplot macro

#set xlabel "x"
#set ylabel "bessel_0(x)"

#plot "bessel0.dat" using 1:2 pt 19 title "down calc", "bessel0.dat" using 1:3 pt 15 title "up calc"

### Start multiplot (2x2 layout) - from documentation
set multiplot layout 2,2 rowsfirst
# --- GRAPH a
set xlabel "x"
set ylabel "bessel_0(x)"
plot "bessel0.dat" using 1:2 pt 19 title "down calc", "bessel0.dat" using 1:3 pt 15 title "up calc"
# --- GRAPH b
set xlabel "x"
set ylabel "bessel_3=(x)"
plot "bessel3.dat" using 1:2 pt 19 title "down calc", "bessel3.dat" using 1:3 pt 15 title "up calc"
# --- GRAPH c
set xlabel "x"
set ylabel "bessel_5=(x)"
plot "bessel5.dat" using 1:2 pt 19 title "down calc", "bessel5.dat" using 1:3 pt 15 title "up calc"
# --- GRAPH d
set xlabel "x"
set ylabel "bessel_8=(x)"
plot "bessel8.dat" using 1:2 pt 19 title "down calc", "bessel8.dat" using 1:3 pt 15 title "up calc"
unset multiplot
### End multiplot
