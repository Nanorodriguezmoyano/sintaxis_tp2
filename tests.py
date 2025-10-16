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
''',
# test_5 
'''
''',
# test_6 
'''
''',
# test_7 
'''
''',
# test_8 
'''
''',
# test_9 
'''
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
        comentarios, derivaciones = parser(tkns)
        print(comentarios, file=f)
        print("", file=f)
        print(derivaciones, file=f)
