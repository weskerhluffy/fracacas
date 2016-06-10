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
nivel_log = logging.ERROR
#nivel_log = logging.DEBUG

def fractal_minimo_esclavos(tam_seq_orig, complejidad):
    min_esc = 0
    tam_seq_final = 0
    logger_cagada.debug("tam seq %u, complejidad %u" % (tam_seq_orig, complejidad))
    tam_seq_final = int(tam_seq_orig ** complejidad)
    logger_cagada.debug("tam seq final %u" % tam_seq_final)
    if(complejidad == 1):
        min_esc = tam_seq_orig
    else:
        min_esc = math.ceil(tam_seq_orig / (complejidad ))
    if(min_esc == 0):
        min_esc = 1
    return min_esc

def fractal_posiciones_sensuales(tam_seq_orig, complejidad):
    niveles_cubiertos = 0
    excedente_niveles = 0
    pos_sensual = 0
    posiciones = array.array("L")
    
    excedente_niveles = tam_seq_orig
    
    while(excedente_niveles):
        pos_sensual=0
        tam_seq_act = tam_seq_orig ** (complejidad - 1)
        while(int(tam_seq_act) > 0 and niveles_cubiertos < tam_seq_orig):
            pos_sensual += niveles_cubiertos * tam_seq_act
            logger_cagada.debug("la primera pos %u con nivel %u con pedazo de tamano %u" % (pos_sensual, niveles_cubiertos, tam_seq_act))
            niveles_cubiertos += 1
            tam_seq_act /= tam_seq_orig
        excedente_niveles = tam_seq_orig - niveles_cubiertos
        logger_cagada.debug("el xcedente de nivl %u" % excedente_niveles)
    
        pos_sensual = int(pos_sensual) + 1
        logger_cagada.debug("anadiendo posicion %u" % (pos_sensual))
        posiciones.append(pos_sensual)
    
    assert(excedente_niveles == 0)
    
    return posiciones
    
    

def fractal_main():
    casos = 0
    num_caso = 1
    lineas = None

    lineas = list(fileinput.input())
    logger_cagada.debug("las lienas son %s" % lineas)
    casos = int(lineas[0])
    
    logger_cagada.debug("el num de casos %u" % casos)
    for linea in lineas[1:]:
        posible = False
        min_esc = 0
        (tam_seq, comple, escla) = 0, 0, 0
        posiciones_sex = array.array("L")
        
        logger_cagada.debug("la linea orginal %s" % linea)
        (tam_seq, comple, escla) = [int(x.strip()) for x in linea.split(" ")]
        
        logger_cagada.debug("case %u: el tam seq %u, al comple %u y los escla %u" % (num_caso, tam_seq, comple, escla))
        min_esc = fractal_minimo_esclavos(tam_seq, comple)
        logger_cagada.debug("el min d esclavos nec %u, el provisto %u" % (min_esc, escla))
        posible = min_esc <= escla
        logger_cagada.debug("CAZA %u es %s" % (num_caso, posible))
        if(posible):
            posiciones_sex = fractal_posiciones_sensuales(tam_seq, comple)
            logger_cagada.debug("las posiciones sensualonas %s" % posiciones_sex)
            assert(len(posiciones_sex) == min_esc)
            print("Case #%lu: %s" % (num_caso, " ".join([str(x) for x in posiciones_sex])))
        else:
            print("Case #%lu: IMPOSSIBLE" % (num_caso))
        num_caso += 1
        
        
    
    

if __name__ == '__main__':
    logging.basicConfig(level=nivel_log)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)

    fractal_main()
