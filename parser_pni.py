from producciones import *

VT=[TOKEN_OPERADOR_RELACIONAL,TOKEN_PR_PROGRAM,TOKEN_PR_VAR,TOKEN_PR_BEGIN,TOKEN_PR_END, TOKEN_PR_IF,TOKEN_PR_ELSE,TOKEN_PR_INT,TOKEN_PR_BOOL,TOKEN_PR_TRUE,TOKEN_PR_FALSE,TOKEN_PR_NOT,TOKEN_PR_AND,TOKEN_PR_OR,TOKEN_PR_GOTO,TOKEN_PR_LET,TOKEN_ASIGNACION,TOKEN_OM_MAS, TOKEN_OM_GUION, TOKEN_OM_ASTERISCO, TOKEN_SP_PUNTO,TOKEN_SP_COMA,TOKEN_SP_DOSPUNTOS, TOKEN_SP_PUNTOCOMA,TOKEN_SP_PARENTESIS_IZQ,TOKEN_SP_PARENTESIS_DER,TOKEN_SP_TRIPLEPUNTO,TOKEN_NUM,TOKEN_ID,'Eof']
VN=[TCode, Body, DecVarList,DecVar,DecVarBody,Statement,StatementList,StatementBody,Goto,Assignment,Op,MatOp,BoolOp,Lvalue,Rvalue,Conditional,CompExpr,CompOp,DecVarList0,StatementList0,Rbody,A0,B0,C0,Bool0]

def desc_rec_proc(codigo_fuente):
    datos_locales= {
        'lista_tokens' : codigo_fuente,
        'error' : False,
        'index': 0
    }
    

    def pni(no_terminal):
        if datos_locales['lista_tokens'][datos_locales['index']] in P[no_terminal].keys():
            produccion = P[no_terminal][datos_locales['lista_tokens'][datos_locales['index']]]
            procesar(produccion)
            

            

    def procesar(cuerpo_produccion): 
        for simbolo in cuerpo_produccion:
            caracter_actual = datos_locales['lista_tokens'][datos_locales['index']]
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

    def principal(): 
        pni(TCode)
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']]
        if caracter_actual != 'Eof' or datos_locales['error']:
            print('La cadena no pertenece al lenguaje')
            return False
        print('La cadena pertenece al lenguaje') 
        return True
    
    return principal()

programa=[TOKEN_PR_PROGRAM, TOKEN_SP_PUNTO, TOKEN_PR_BEGIN,TOKEN_PR_END,'Eof']
desc_rec_proc(programa)
