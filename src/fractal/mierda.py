'''
Created on 20/05/2016

@author: ernesto
https://code.google.com/codejam/contest/6254486/dashboard#s=p3
'''

import math
import logging
import fileinput
import array
logger_cagada = None
# nivel_log = logging.ERROR
nivel_log = logging.DEBUG

def fractal_minimo_esclavos(tam_seq_orig, complejidad):
    min_esc = 0
    tam_seq_final = 0
    logger_cagada.debug("tam seq %u, complejidad %u" % (tam_seq_orig, complejidad))
    tam_seq_final = int(tam_seq_orig ** complejidad)
    logger_cagada.debug("tam seq final %u" % tam_seq_final)
    min_esc = tam_seq_orig - complejidad
    if(min_esc >= 0):
        min_esc += 1
    else:
        min_esc = 1
    return min_esc

def fractal_posiciones_sensuales(tam_seq_orig, complejidad):
    niveles_cubiertos = 0
    excedente_niveles = 0
    primer_pos_sensual = 0
    posiciones = array.array("I")
    
    tam_seq_act = tam_seq_orig ** (complejidad - 1)
    while(int(tam_seq_act) > 0 and niveles_cubiertos < tam_seq_orig):
        primer_pos_sensual += niveles_cubiertos * tam_seq_act
        logger_cagada.debug("la primera pos %u con nivel %u con pedazo de tamano %u" % (primer_pos_sensual, niveles_cubiertos, tam_seq_act))
        niveles_cubiertos += 1
        tam_seq_act /= tam_seq_orig
    excedente_niveles = tam_seq_orig - niveles_cubiertos
    logger_cagada.debug("el xcedente de nivl %u" % excedente_niveles)
    assert(excedente_niveles >= 0)
    primer_pos_sensual = int(primer_pos_sensual) + 1
    for pos_nueva in range(primer_pos_sensual, primer_pos_sensual + excedente_niveles + 1):
        logger_cagada.debug("anadiendo posicion %u extra" % (pos_nueva))
        posiciones.append(pos_nueva)
    return posiciones
    
    

def fractal_main():
    casos = 0
    num_caso = 1
    lineas = None

    lineas = list(fileinput.input())
    casos = int(lineas[0])
    
    for linea in lineas[1:]:
        posible = False
        min_esc = 0
        (tam_seq, comple, escla) = 0, 0, 0
        posiciones_sex = array.array("I")
        
        (tam_seq, comple, escla) = [int(x.strip()) for x in linea.split(" ")]
        
        logger_cagada.debug("case %u: el tam seq %u, al comple %u y los escla %u" % (num_caso, tam_seq, comple, escla))
        min_esc = fractal_minimo_esclavos(tam_seq, comple)
        logger_cagada.debug("el min d esclavos nec %u, el provisto %u" % (min_esc, escla))
        posible = min_esc <= escla
        logger_cagada.debug("CAZA %u es %s" % (num_caso, posible))
        num_caso += 1
        if(posible):
            posiciones_sex = fractal_posiciones_sensuales(tam_seq, comple)
            logger_cagada.debug("las posiciones sensualonas %s" % posiciones_sex)
            assert(len(posiciones_sex) >= min_esc)
        
        
    
    

if __name__ == '__main__':
    logging.basicConfig(level=nivel_log)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)

    fractal_main()
