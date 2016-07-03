from bitarray import bitarray
import sys
import array

def generar_cagada(tamano_combs):
	cadenitas = list()
	for posi in range(0, tamano_combs):
		a = bitarray(tamano_combs)
		a[:] = False
# 		print("carmen %s"%a)
		a[posi] = True
		a = list(reversed(a))
		a = bitarray(a)
# 		print("la cadenita gen %s"%a)
		cadenitas.append(a)
	return cadenitas

def elevar_caca(cadenita, num_a_ele):
	resultado_final = None

	resultado_final = cadenita
	tam_actual = resultado_final.length()
# 	print("resultado final inicial        %s"%resultado_final)
	for num_ac in range(0, num_a_ele):
		resultado_parcial = bitarray()
		for bitch in resultado_final:
			if(not bitch):
				carmen = cadenita.copy()
				resultado_parcial.extend(carmen)
			else:
				puros_1 = bitarray(tam_actual)
				puros_1[:] = True
				resultado_parcial.extend(puros_1)
		resultado_final = resultado_parcial
# 		print("resultado final actual nivel %u %s"%(num_ac+1,resultado_final))
# 	print("resultado final final %s"%resultado_final)
	return resultado_final


tam_seq = 0
complejidad = 0
posiciones_busca = array.array("L")

print("that im")

tam_seq = int(sys.argv[1])
complejidad = int(sys.argv[2]) - 1
posiciones_busca = sys.argv[3:len(sys.argv) ]
bits_posiciones = [array.array("L") for x in range(len(posiciones_busca))]
if(posiciones_busca):
	print("las posiciones sexuales %s" % posiciones_busca)
	print("las posiciones de bitchs %s" % bits_posiciones)
else:
	print("no ay posiciones")


# mierda = generar_cagada(5)
mierda = generar_cagada(tam_seq)
for meirde in mierda:
	ass = elevar_caca(meirde, complejidad)
#	print(ass)
	if(not posiciones_busca):
		print(ass)
	for idx, bit_pos in enumerate(posiciones_busca):
# 		print("la pos de bits %lu"%int(bit_pos))
# 		print(bits_posiciones[idx])
# 		print(ass[int(bit_pos)])
		bits_posiciones[idx].append(ass[int(bit_pos) - 1])
	
#print("mierda %s" % bits_posiciones)
if(posiciones_busca):
	for fila in range(len(bits_posiciones[0])):
		cadenita = ""
		for idx, columna in enumerate(posiciones_busca):
			cadenita += str(bits_posiciones[idx][fila])
		print("%s"%cadenita)
