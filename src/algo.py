from bitarray import bitarray
import sys

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
# 	print("resultado final inicial %s"%resultado_final)
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
print("that im")

tam_seq = int(sys.argv[1])
complejidad = int(sys.argv[2]) - 1
# mierda = generar_cagada(5)
mierda = generar_cagada(tam_seq)
for meirde in mierda:
	ass = elevar_caca(meirde, complejidad)
	print(ass)
