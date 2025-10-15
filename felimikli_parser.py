from producciones import *
from tests import *
from lexer import *

VT=[TOKEN_OPERADOR_RELACIONAL,TOKEN_PR_PROGRAMA,TOKEN_PR_VAR,TOKEN_PR_BEGIN,TOKEN_PR_END, TOKEN_PR_IF,TOKEN_PR_ELSE,TOKEN_PR_INT,TOKEN_PR_BOOL,TOKEN_PR_TRUE,TOKEN_PR_FALSE,TOKEN_PR_NOT,TOKEN_PR_AND,TOKEN_PR_OR,TOKEN_PR_GOTO,TOKEN_PR_LET,TOKEN_ASIGNACION,TOKEN_OM_MAS, TOKEN_OM_GUION, TOKEN_OM_ASTERISCO, TOKEN_SP_PUNTO,TOKEN_SP_COMA,TOKEN_SP_DOSPUNTOS, TOKEN_SP_PUNTOCOMA,TOKEN_SP_PARENTESIS_IZQ,TOKEN_SP_PARENTESIS_DER,TOKEN_SP_TRIPLEPUNTO,TOKEN_NUM,TOKEN_ID,'Eof']
VN=[TCode, Body, DecVarList,DecVar,DecVarBody,Statement,StatementList,StatementBody,Goto,Assignment,Op,MatOp,BoolOp,Lvalue,Rvalue,Conditional,CompExpr,CompOp,DecVarList0,StatementList0,Rbody,A0,B0,C0,Bool0]

datos_locales= {
    'lista_tokens' : [],
    'error' : False,
    'index': 0,
    'derivaciones':[]
}

def procesar(cuerpo_produccion):
    for simbolo in cuerpo_produccion:
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']]
        datos_locales['error'] = False
        if simbolo in VT:
            if simbolo == caracter_actual:
                datos_locales['index'] += 1

            else:
                datos_locales['error'] = True
                print(f'Error, se esperaba {simbolo}, y se encontro, {caracter_actual}')
                print(datos_locales['derivaciones'])
                break
        elif simbolo in VN:
            pni(simbolo)
            if datos_locales['error']:
                break

def pni(no_terminal):
    if datos_locales['lista_tokens'][datos_locales['index']] in P[no_terminal].keys():
        cuerpo_produccion = P[no_terminal][datos_locales['lista_tokens'][datos_locales['index']]]
        datos_locales['derivaciones'].append({no_terminal:cuerpo_produccion})
        procesar(cuerpo_produccion)
    else:
        print(f'Error, no hay regla para {datos_locales['lista_tokens'][datos_locales['index']]}, con {no_terminal}')
        # datos_locales['error'] = True

def desc_rec_proc(tokens):
    for token_lexema in tokens:
        datos_locales['lista_tokens'].append(token_lexema[0]) # El tokenizer devuelve lista de tuplas (token, lexema), nos interesa el token
    datos_locales['lista_tokens'].append('Eof')

    pni(TCode)

    caracter_actual = datos_locales['lista_tokens'][datos_locales['index']]
    if caracter_actual != 'Eof' or datos_locales['error']:
        print('La cadena no pertenece al lenguaje')
        return False
    print('La cadena pertenece al lenguaje')
    print(datos_locales['derivaciones'])
    return True


# desc_rec_proc(tokenizer(cadena_valida_1))
desc_rec_proc(tokenizer(cadena_valida_2))
