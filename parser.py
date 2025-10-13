from producciones import *
from lexer import *

VT=[TOKEN_OPERADOR_RELACIONAL,TOKEN_PR_PROGRAM,TOKEN_PR_VAR,TOKEN_PR_BEGIN,TOKEN_PR_END, TOKEN_PR_IF,TOKEN_PR_ELSE,TOKEN_PR_INT,TOKEN_PR_BOOL,TOKEN_PR_TRUE,TOKEN_PR_FALSE,TOKEN_PR_NOT,TOKEN_PR_AND,TOKEN_PR_OR,TOKEN_PR_GOTO,TOKEN_PR_LET,TOKEN_ASIGNACION,TOKEN_OM_MAS, TOKEN_OM_GUION, TOKEN_OM_ASTERISCO, TOKEN_SP_PUNTO,TOKEN_SP_COMA,TOKEN_SP_DOSPUNTOS, TOKEN_SP_PUNTOCOMA,TOKEN_SP_PARENTESIS_IZQ,TOKEN_SP_PARENTESIS_DER,TOKEN_SP_TRIPLEPUNTO,TOKEN_NUM,TOKEN_ID]
VN=[TCode, Body, DecVarList,DecVar,DecVarBody,Statement,StatementList,StatementBody,Goto,Assignment,Op,MatOp,BoolOp,Lvalue,Rvalue,Conditional,CompExpr,CompOp,DecVarList0,StatementList0,Rbody,A0,B0,C0,Bool0]

def parser_predictivo_por_tabla(codigo_fuente):
    datos_locales = {
        'lista_tokens': codigo_fuente,
        'index': 0,
        'error': False,
        'pila':['Eof','TCode'],
        'tope': 1
    }

    while datos_locales['pila'][-1] != 'Eof' and datos_locales['lista_tokens'][datos_locales['index']] != 'Eof' and not datos_locales['error']:  
        for simbolo in datos_locales['lista_tokens']:
            print(simbolo, '   ',datos_locales['pila'][-1])
         
            if datos_locales['pila'][-1] in VT:
                if datos_locales['pila'][-1] ==simbolo:
                    datos_locales['pila'].pop()
                    datos_locales['index']+=1
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
                    print('La cadena no pertenece al lenguaje1')
                    datos_locales['error']=True
                    break

str=[TOKEN_PR_PROGRAM, TOKEN_ID, TOKEN_SP_PUNTOCOMA, TOKEN_PR_VAR, DecVarList, TOKEN_PR_BEGIN, StatementList, TOKEN_PR_END, 'Eof']
parser_predictivo_por_tabla(str)
