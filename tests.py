from tokens import *
tokens_validos = [
    TOKEN_PR_PROGRAMA, TOKEN_SP_PUNTO,               # programa .
    TOKEN_PR_VAR,                                   # var
    TOKEN_ID, TOKEN_SP_DOSPUNTOS,                   # x :
    TOKEN_PR_INT, TOKEN_SP_PARENTESIS_IZQ, TOKEN_NUM, TOKEN_SP_TRIPLEPUNTO, TOKEN_NUM,
    TOKEN_SP_PARENTESIS_DER, TOKEN_ASIGNACION, TOKEN_NUM, TOKEN_SP_PUNTOCOMA,  # int(0...10)=0;
    TOKEN_PR_BEGIN,                                 # begin
    TOKEN_PR_IF, TOKEN_ID, TOKEN_OPERADOR_RELACIONAL, TOKEN_NUM,               # if x < 10
    TOKEN_PR_GOTO, TOKEN_ID, TOKEN_SP_PUNTOCOMA,                             # goto label;
    TOKEN_PR_ELSE, TOKEN_PR_GOTO, TOKEN_ID, TOKEN_SP_PUNTOCOMA,              # else goto id;
    TOKEN_PR_END,                                   # end
    'Eof'
]
tokens_invalidos = [
    TOKEN_PR_PROGRAMA, TOKEN_SP_PUNTO,             # programa .
    TOKEN_PR_VAR,                                   # var
    TOKEN_ID,                   # x :
    TOKEN_PR_INT, TOKEN_SP_PARENTESIS_IZQ, TOKEN_NUM, TOKEN_SP_TRIPLEPUNTO, TOKEN_NUM,
    TOKEN_SP_PARENTESIS_DER, TOKEN_ASIGNACION, TOKEN_NUM, TOKEN_SP_PUNTOCOMA,  # int(0...10)=0;
    TOKEN_PR_BEGIN,                                 # begin
    TOKEN_PR_IF, TOKEN_ID, TOKEN_OPERADOR_RELACIONAL, TOKEN_NUM,               # if x < 10
    TOKEN_PR_GOTO, TOKEN_ID, TOKEN_SP_PUNTOCOMA,                             # goto label;
    TOKEN_PR_ELSE, TOKEN_PR_GOTO, TOKEN_ID, TOKEN_SP_PUNTOCOMA,              # else goto end;
    TOKEN_PR_END,                                   # end
    'Eof'
]

tokens_invalidos2 = [
    TOKEN_SP_PUNTO,         # program .
                                 # var
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

cadena_valida_1 = '''
    programa .
    var x : int(0...10) = 0;
    begin
        if x < 10
            goto label;
        else goto id;
        end
'''
