from tokens import *

P = {
    TCode:{
        TOKEN_PR_PROGRAM: [TOKEN_PR_PROGRAM,TOKEN_SP_PUNTO, Body]
    },
    Body : {
        TOKEN_PR_VAR: [TOKEN_PR_VAR, DecVar ,DecVarList , TOKEN_PR_BEGIN,StatementList , TOKEN_PR_END ],
        TOKEN_PR_BEGIN: [TOKEN_PR_BEGIN, StatementList, TOKEN_PR_END]
    },
    DecVarList : {
        TOKEN_ID: [DecVar, DecVarList],
        TOKEN_PR_BEGIN: []  # fin
    },
    DecVarList0:{
        TOKEN_ID: [DecVar, DecVarList],
        TOKEN_PR_BEGIN: []
    },
    DecVar: {
        TOKEN_ID:[TOKEN_ID, TOKEN_SP_DOSPUNTOS, DecVarBody]
    },
    DecVarBody:{
        TOKEN_PR_INT:[TOKEN_PR_INT, TOKEN_SP_PARENTESIS_IZQ, TOKEN_NUM, TOKEN_SP_TRIPLEPUNTO, TOKEN_NUM, TOKEN_SP_PARENTESIS_DER, TOKEN_ASIGNACION, TOKEN_NUM, TOKEN_SP_PUNTOCOMA ]
    },
    Bool0:{
        TOKEN_PR_BOOL:[TOKEN_PR_BOOL, TOKEN_OPERADOR_RELACIONAL,C0]
    } ,
    C0:{
        TOKEN_PR_TRUE:[TOKEN_PR_TRUE],
        TOKEN_PR_FALSE:[TOKEN_PR_FALSE]
    },
    Statement:{
        TOKEN_PR_IF:[StatementBody],
        TOKEN_PR_GOTO: [StatementBody],
        TOKEN_PR_LET: [StatementBody],
        TOKEN_ID: [TOKEN_ID,TOKEN_SP_DOSPUNTOS,StatementBody]
    },
    StatementList :{
        TOKEN_ID: [Statement, StatementList],
        TOKEN_PR_IF: [Statement, StatementList],
        TOKEN_PR_GOTO: [Statement, StatementList],
        TOKEN_PR_LET: [Statement, StatementList],
        TOKEN_PR_END: []  # fin
    },
    StatementBody:{
        TOKEN_PR_IF:[Conditional],
        TOKEN_PR_GOTO:[Goto],
        TOKEN_PR_LET:[Assignment]
    },
    Goto:{
        TOKEN_PR_GOTO:[TOKEN_PR_GOTO,TOKEN_ID,TOKEN_SP_PUNTOCOMA]
    },
    Assignment:{
        TOKEN_PR_LET:[Lvalue, TOKEN_ASIGNACION, Rbody, TOKEN_SP_PUNTOCOMA]
    },
    Rbody:{
        TOKEN_PR_NOT:[TOKEN_PR_NOT,Rvalue]
    },
    B0:{
        TOKEN_PR_END:[],
        TOKEN_PR_TRUE:[Rvalue, Op, Rvalue],
        TOKEN_PR_FALSE:[Rvalue, Op, Rvalue],
        TOKEN_NUM:[Rvalue, Op, Rvalue],
        TOKEN_ID:[Rvalue, Op, Rvalue]
    },
    Op:{
        TOKEN_PR_AND:[BoolOp],
        TOKEN_PR_OR:[BoolOp],
        TOKEN_OM_MAS:[MatOp],
        TOKEN_OM_GUION:[MatOp],
        TOKEN_OM_ASTERISCO:[MatOp]
    },
    MatOp:{
        TOKEN_OM_MAS:[TOKEN_OM_MAS],
        TOKEN_OM_ASTERISCO:[TOKEN_OM_ASTERISCO],
        TOKEN_OM_GUION:[TOKEN_OM_GUION]
    },
    BoolOp:{
        TOKEN_PR_AND:[TOKEN_PR_AND],
        TOKEN_PR_OR:[TOKEN_PR_OR]
    },
    Lvalue:{
        TOKEN_ID:[TOKEN_ID]
    },
    Rvalue:{
        TOKEN_NUM:[TOKEN_NUM],
        TOKEN_ID:[TOKEN_ID],
        TOKEN_PR_TRUE:[TOKEN_PR_TRUE],
        TOKEN_PR_FALSE:[TOKEN_PR_FALSE]
    },
    Conditional:{
        TOKEN_PR_IF:[TOKEN_PR_IF, CompExpr, TOKEN_PR_GOTO, TOKEN_ID, TOKEN_SP_PUNTOCOMA, A0]
    },
    A0:{
        TOKEN_PR_END:[],
        TOKEN_PR_ELSE:[TOKEN_PR_ELSE, TOKEN_PR_GOTO, TOKEN_ID,TOKEN_SP_PUNTOCOMA]
    },
    CompExpr:{
        TOKEN_PR_TRUE:[Rvalue, CompOp, Rvalue],
        TOKEN_PR_FALSE:[Rvalue, CompOp, Rvalue],
        TOKEN_NUM:[Rvalue, CompOp, Rvalue],
        TOKEN_ID:[Rvalue, CompOp, Rvalue]
    },
    CompOp:{
        TOKEN_OPERADOR_RELACIONAL:[TOKEN_OPERADOR_RELACIONAL]
    }
}

