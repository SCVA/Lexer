import ply.lex as lex

reservadas=['ALGORITMO','SI','ENTONCES','FIN','PARA','HASTA','CON','PASO','HACER']

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS', 'MAYOR',
           'MENOR','MAYORIGUAL','MENORIGUAL','DIFERENTE','EXACTO','RESERVADO']

def esReservado(t):
    if(t.upper() in reservadas):
        return True
    else:
        return False

t_ignore = ' \t\n'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'<-'
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_DIFERENTE = r'!='
t_EXACTO = r'==' 

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if(not(esReservado(t.value))):
        return t
    else:
        t.type = "RESERVADO"
        return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer
a = open("datos.txt")
lineas = a.readlines()

for i in lineas:    
    lex.input(i)
    while True:
        tok = lex.token()
        if not tok: break
        print str(tok.value) + " - " + str(tok.type)
