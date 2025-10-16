from producciones import *
from lexer import *

VT=[TOKEN_OPERADOR_RELACIONAL,TOKEN_PR_PROGRAM,TOKEN_PR_VAR,TOKEN_PR_BEGIN,TOKEN_PR_END, TOKEN_PR_IF,TOKEN_PR_ELSE,TOKEN_PR_INT,TOKEN_PR_BOOL,TOKEN_PR_TRUE,TOKEN_PR_FALSE,TOKEN_PR_NOT,TOKEN_PR_AND,TOKEN_PR_OR,TOKEN_PR_GOTO,TOKEN_PR_LET,TOKEN_ASIGNACION,TOKEN_OM_MAS, TOKEN_OM_GUION, TOKEN_OM_ASTERISCO, TOKEN_SP_PUNTO,TOKEN_SP_COMA,TOKEN_SP_DOSPUNTOS, TOKEN_SP_PUNTOCOMA,TOKEN_SP_PARENTESIS_IZQ,TOKEN_SP_PARENTESIS_DER,TOKEN_SP_TRIPLEPUNTO,TOKEN_NUM,TOKEN_ID]
VN=[TCode, Body, DecVarList,DecVar,DecVarBody,Statement,StatementList,StatementBody,Goto,Assignment,Op,MatOp,BoolOp,Lvalue,Rvalue,Conditional,CompExpr,CompOp,DecVarList0,StatementList0,Rbody,A0,B0,C0,Bool0]

def parser_predictivo_por_tabla(codigo_fuente):
    datos_locales = {
        'lista_tokens': codigo_fuente,
        'index': 0,
        'error': False,
        'pila': ['Eof', TCode]
    }
    while datos_locales['pila'][-1] != 'Eof' and datos_locales['lista_tokens'][datos_locales['index']] != 'Eof' and not datos_locales['error']:  
        for simbolo in datos_locales['lista_tokens']: # Esto está mal, no se tienen que mirar todos los tokens, sino el token actual pues es predictivo
            print(simbolo, '   ',datos_locales['pila'][-1])
            if datos_locales['pila'][-1] in VT:
                if datos_locales['pila'][-1] == simbolo:
                    datos_locales['pila'].pop()
                    datos_locales['index']+=1 # El index solo se incrementa si el terminal coincide con el token, pero si el tope de la pila era no terminal que se expandía a una producción vacía, no se hacía pop correctamente
                else:
                    print('La cadena no pertenece al lenguaje2')
                    datos_locales['error']=True
                    break
            else:
                if datos_locales['lista_tokens'][datos_locales['index']] in P[datos_locales['pila'][-1]].keys():
                    tope=datos_locales['pila'][-1]
                    datos_locales['pila'].pop()
                    datos_locales['pila'].extend(P[tope][datos_locales['lista_tokens'][datos_locales['index']]])
                else:
                    print('La cadena no pertenece al lenguaje.')
                    datos_locales['error']=True
                    break

def parser_predictivo_por_tabla2(codigo_fuente):
    datos_locales = {
        'lista_tokens': codigo_fuente,
        'index': 0,
        'error': False,
        'pila': ['Eof', TCode]
    }

    while datos_locales['pila'][-1] != 'Eof' and datos_locales['lista_tokens'][datos_locales['index']] != 'Eof' and not datos_locales['error']:
        # Elimino el for que recorria todos los tokens, entonces en cada iteración del while solo se analiza el token actual
        simbolo = datos_locales['lista_tokens'][datos_locales['index']]
        tope = datos_locales['pila'][-1]

        print(simbolo, "   ", tope)

        if tope in VT:
            if tope == simbolo:
                datos_locales['pila'].pop()
                datos_locales['index'] += 1 #Si coincide con el token actual, se hace pop y se incrementa el index
            else:
                print("Error: se esperaba", tope, "y se encontró", simbolo) # Agregué la recuperación del error (porque me la re contra banco)
                datos_locales['error'] = True # Si un no temminal no coincide , error = true
        else:
            if simbolo in P[tope]:
                datos_locales['pila'].pop()
                produccion = P[tope][simbolo]
                if produccion != []:
                    datos_locales['pila'].extend(reversed(produccion)) # Si la producción es distinta al epsilon, hago pop del no terminal y luego extend de los simbolos de la producción  
            else:
                print(f"No hay regla para {tope} con {simbolo}")
                datos_locales['error'] = True # Si no hay producción para el token actual en un no terminal, entonces error = True

    if not datos_locales['error'] and datos_locales['pila'][-1] == 'Eof' and datos_locales['lista_tokens'][datos_locales['index']] == 'Eof':
        print("La cadena pertenece al lenguaje.")
    else:
        print("La cadena no pertenece al lenguaje.")
# Nota importante: antes,en algunos casos el for sobre toda la lista causaba que el mismo token se procesara varias veces. Ahora, solo se consume un token a la vez, y la pila se actualiza correctamente.

#str=[TOKEN_PR_PROGRAM, TOKEN_ID, TOKEN_SP_PUNTOCOMA, TOKEN_PR_VAR, DecVarList, TOKEN_PR_BEGIN, StatementList, TOKEN_PR_END, 'Eof']
#parser_predictivo_por_tabla(str)

tokens_validos = [
    TOKEN_PR_PROGRAM, TOKEN_SP_PUNTO,               # program .
    TOKEN_PR_VAR,                                   # var
    TOKEN_ID, TOKEN_SP_DOSPUNTOS,                   # x :
    TOKEN_PR_INT, TOKEN_SP_PARENTESIS_IZQ, TOKEN_NUM, TOKEN_SP_TRIPLEPUNTO, TOKEN_NUM,
    TOKEN_SP_PARENTESIS_DER, TOKEN_ASIGNACION, TOKEN_NUM, TOKEN_SP_PUNTOCOMA,  # int(0...10)=0;
    TOKEN_PR_BEGIN,                                 # begin
    TOKEN_PR_IF, TOKEN_ID, TOKEN_OPERADOR_RELACIONAL, TOKEN_NUM,               # if x < 10
    TOKEN_PR_GOTO, TOKEN_ID, TOKEN_SP_PUNTOCOMA,                             # goto label;
    TOKEN_PR_ELSE, TOKEN_PR_GOTO, TOKEN_ID, TOKEN_SP_PUNTOCOMA,              # else goto end;
    TOKEN_PR_END,                                   # end
    'Eof'
]

parser_predictivo_por_tabla(tokens_validos) #Este no funciona 
parser_predictivo_por_tabla2(tokens_validos) #Este funciona