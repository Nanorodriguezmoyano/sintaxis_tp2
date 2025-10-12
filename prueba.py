VN = ['A','B']

VT = ['TokenA','TokenB','TokenC','TokenD','TokenE']

P = { 'A': [['TokenA','A','TokenC'], # En lugar de está estructura de producciones
                                     # ustedes necesitarán una con los símbolos directrices
            ['B']] ,
      'B': [['TokenB','B','TokenD'],
            ['TokenE']]      }

def lex(codigo_fuente): # Esto esta solo como recordatorio que es necesario usar el lexer del TP1
                        # Esto no es verdaderamente un lexer
                        # Ustedes acá usaran el lexer del TP1, no es necesario ponerlo aquí, pueden importarlo
                        # como en algunos casos tenían los afd aparte y los importaron al lexer 
                        # Si recuerden agregar a su lexer el token Eof o fin de cadena como aquí 
    lista_tokens=[]
    for i in codigo_fuente:
        if i=='a':
            lista_tokens.append(('TokenA','a'))
        elif i=='b':
            lista_tokens.append(('TokenB','b'))
        elif i=='c':
            lista_tokens.append(('TokenC','c'))
        elif i=='d':
            lista_tokens.append(('TokenD','d'))
        elif i=='e':
            lista_tokens.append(('TokenE','e'))
        else:
            return []
    lista_tokens.append(('Eof','Eof'))
    return lista_tokens

def desc_rec_proc(codigo_fuente):
    datos_locales = {
        'lista_tokens': codigo_fuente,
        'index': 0,
        'error': False,
    }   
          
    def pni(no_terminal): # Este es el procedimiento que hay que cambiar por completo para que sea predictivo
        for cuerpo_produccion in P[no_terminal]:
            backtracking_index = datos_locales['index']
            procesar(cuerpo_produccion)
            if datos_locales['error']:
                datos_locales['index'] = backtracking_index
            else:
                break
    
    def procesar(cuerpo_produccion): # Este procedimiento puede usarse igual
        for simbolo in cuerpo_produccion:
            print(cuerpo_produccion)
            caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
            #lexema_actual = datos_locales['lista_tokens'][datos_locales['index']][1]
            datos_locales['error'] = False
            if simbolo in VT:
                if simbolo == caracter_actual:
                    datos_locales['index'] += 1                        
                else:
                    datos_locales['error'] = True
                    break
            elif simbolo in VN:
                pni(simbolo)
                if datos_locales['error']:
                    break
                
    
    def principal(): # Este procedimiento principal puede usarse igual, faltaría la parte de la derivación
        pni('A')
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
        if caracter_actual != 'Eof' or datos_locales['error']:
            print('La cadena no pertenece al lenguaje')
            return False
        print('La cadena pertenece al lenguaje') # Acá también habría que mostrar la derivación, o mejor dicho, la secuencia
                                                 # de producciones que llevan al código fuente, y el orden en que hay que usarlas
        return True
    
    return principal()

print(desc_rec_proc(lex('aaabbeddccc')))