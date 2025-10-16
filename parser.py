from producciones import *

VT=[TOKEN_OPERADOR_RELACIONAL,TOKEN_PR_PROGRAMA,TOKEN_PR_VAR,TOKEN_PR_BEGIN,TOKEN_PR_END, TOKEN_PR_IF,TOKEN_PR_ELSE,TOKEN_PR_INT,TOKEN_PR_BOOL,TOKEN_PR_TRUE,TOKEN_PR_FALSE,TOKEN_PR_NOT,TOKEN_PR_AND,TOKEN_PR_OR,TOKEN_PR_GOTO,TOKEN_PR_LET,TOKEN_ASIGNACION,TOKEN_OM_MAS, TOKEN_OM_GUION, TOKEN_OM_ASTERISCO, TOKEN_SP_PUNTO,TOKEN_SP_COMA,TOKEN_SP_DOSPUNTOS, TOKEN_SP_PUNTOCOMA,TOKEN_SP_PARENTESIS_IZQ,TOKEN_SP_PARENTESIS_DER,TOKEN_SP_TRIPLEPUNTO,TOKEN_NUM,TOKEN_ID,EoF]
VN=[TCode, Body, DecVarList,DecVar,DecVarBody,Statement,StatementList,StatementBody,Goto,Assignment,Op,MatOp,BoolOp,Lvalue,Rvalue,Conditional,CompExpr,CompOp,DecVarList0,StatementList0,Rbody,A0,B0,C0,Bool0]



def parser(tokens):
    def procesar(cuerpo_produccion):
        for simbolo in cuerpo_produccion:
            caracter_actual = datos_locales['lista_tokens'][datos_locales['index']]
            datos_locales['error'] = False
            if simbolo in VT:
                if simbolo == caracter_actual:
                    datos_locales['index'] += 1

                else:
                    datos_locales['error'] = True
                    datos_locales['comentarios'].append(f'Error, se esperaba {simbolo}, y se encontro, {caracter_actual}')
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
            datos_locales['comentarios'].append(f'Error, no hay regla para {datos_locales['lista_tokens'][datos_locales['index']]}, con {no_terminal}')
            datos_locales['error'] = True

    datos_locales = {
        'lista_tokens' : [],
        'error' : False,
        'index': 0,
        'derivaciones':[],
        'comentarios' : []
    }


    for token_lexema in tokens:
        datos_locales['lista_tokens'].append(token_lexema[0]) # El tokenizer devuelve lista de tuplas (token, lexema), nos interesa el token
    datos_locales['lista_tokens'].append(EoF)

    pni(TCode)

    caracter_actual = datos_locales['lista_tokens'][datos_locales['index']]
    if caracter_actual != EoF or datos_locales['error']:
        datos_locales['comentarios'].append('La cadena no pertenece al lenguaje')
        datos_locales['error'] = True
    else:
        datos_locales['comentarios'].append('La cadena pertenece al lenguaje')

    return datos_locales['comentarios'], datos_locales['derivaciones']
