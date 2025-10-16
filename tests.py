from parser import parser
from lexer import tokenizer

tests = [
# test_1 
'''
    program .
    var x : int(0...10) = 0;
    begin
        if x < 10
            goto label;
        else goto id;
    end
''',

# test_2 
'''
    program .
    var
    x : int(0...10) = 0;
    y : bool = true;
    z : int(-2...2) = -1;
    begin
        if x == 10 goto suma;

        if x < 10 goto asigna;
        else goto negacion;

        asigna:
        let v1 = x;
        goto fin;

        negacion:
        let v2 = not y;
        goto fin;

        suma:
        let v3 = x + z;
    fin: let termino = 1;
    end
''',

# test_3 
'''
    program .
    begin
    end

''',
# test_4 
'''
    program .
    begin
    let v = 1;
    end
''',
# test_5 
'''
    program .
    var
    begin
    if x > 10 goto bb; else goto dd;
    end
''',
# test_6 
'''
    program .
    var
    x : int(0...10) = 0;
    begin
    if x > 10 goto bb; else goto dd;
    else goto sigma;
    end
''',
# test_7 
'''
    program.
    begin
    goto b;
    b;
    end
''',
# test_8 
'''
    program .
    var
    lambda : int(0...2) = 1;
    begin
    goto b;
    let lambda = 0;
    b: let lambda = 2;
    if lambda == 2 goto sigma;
    else goto beta;
    beta: let gotoFunciona = True;
    goto fin;
    sigma: let gotoFunciona = True;
    fin: let a = 0;
    end
''',
# test_9 
'''
    program .
    begin
    if x = 10 goto alfa; else goto beta
    alfa: let y = True;
    beta: let z = False;
    end

''',
# test_10 
'''
'''
]

f = open("output.txt", "w")
for i in range(len(tests)):
        tkns = tokenizer(tests[i])
        print("", file=f)
        print(f'=========== TEST N:{i + 1} =========', file=f)
        print(tests[i], file=f)
        print("", file=f)
        print(f'----TOKENIZER----', file=f)
        print(tkns, file=f)
        print("", file=f)
        print(f'----PARSER----', file=f)
        valid, comentarios, derivaciones = parser(tkns)

        print("", file=f)
        for s in comentarios:
                print(s, file=f)
        print("", file=f)
        print(f'DERIVACIONES', file=f)
        print("", file=f)
        for der in derivaciones:
                print(f'{list(der.keys())[0]} -> {' '.join(map(str, list(der.values())[0]))}', file=f)
