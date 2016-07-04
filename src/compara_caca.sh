#!/bin/sh -x

for mierda in $(seq 1 14)
do
	nombre_archivo=caca_tmp_$mierda.txt
	pref_nombre_res=${nombre_archivo%.txt}
	echo "trabajando complejidad $mierda"
	cat << CACA > $nombre_archivo
1
28 $mierda 28
CACA
./ass < $nombre_archivo > ${pref_nombre_res}_ass.log
python3.5 fractal/mierda.py < $nombre_archivo > ${pref_nombre_res}_mierda.log
diff ${pref_nombre_res}_ass.log ${pref_nombre_res}_mierda.log
done
