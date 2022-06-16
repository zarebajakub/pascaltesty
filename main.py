from ply import lex
from ply import yacc


reserved = {
        'and': 'AND',
        'array': 'ARRAY',
        'begin': 'BEGIN',
        'case': 'CASE',
        'const': 'CONST',
        'div': 'DIV',
        'do': 'DO',
        'downto': 'DOWNTO',
        'else': 'ELSE',
        'end': 'END',
        'file': 'FILE',
        'for': 'FOR',
        'function': 'FUNCTION',
        'goto': 'GOTO',
        'if': 'IF',
        'in': 'IN',
        'label': 'LABEL',
        'mod': 'MOD',
        'nil': 'NIL',
        'not': 'NOT',
        'of': 'OF',
        'or': 'OR',
        'procedure': 'PROCEDURE',
        'program': 'PROGRAM',
        'record': 'RECORD',
        'repeat': 'REPEAT',
        'set': 'SET',
        'then': 'THEN',
        'to': 'TO',
        'type': 'TYPE',
        'until': 'UNTIL',
        'var': 'VAR',
        'while': 'WHILE',
        'with': 'WITH',
        'eof': 'EOF',
        'eoln': 'EOLN',
        'false': 'FALSE',
        'true': 'TRUE',
        'input': 'INPUT',
        'output': 'OUTPUT',
        'get': 'GET',
        'put': 'PUT',
        'readln': 'READLN',
        'read': 'READ',
        'write': 'WRITE',
        'writeln': 'WRITELN',
        'lineend': 'LINEEND',
        'sqrt': 'SQRT',
        'text': 'TEXT',
        'dispose': 'DISPOSE',
        'integer': 'INTEGER',
        'char': 'CHAR',
        'real': 'REAL',
        'boolean': 'BOOLEAN',

}
tokens = [
        'EMPTY',
        'ID',
        'PLUS',
        'MINUS',
        'MULTIPLY',
        'DIVIDE',
        'EQ',
        'LT',
        'GT',
        'DOT',
        'COMA',
        'REF',
        'DOLLAR',
        'HASH',
        'BINLSO',
        'BINRSO',
        'ISDIFF',
        'SYMMDIFF',
        'LOREQ',
        'GOREQ',
        'ASSIG',
        'INCRBY',
        'DECRBY',
        'MULTBY',
        'DIVBY',
        'LP',
        'RP',
        'LBR',
        'RBR',
        'SEMICOL',
        'COL',
        'LCURLBR',
        'RCURLBR',

] + list(reserved.values())

#'LCOMM', 'RCOMM', 'LGROUP', 'RGROUP',
#, 'EXPON'
# Operators

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_COMA = r','
t_DOT = r'\.'
t_BINLSO = r'<<'
t_BINRSO = r'>>'
# t_EXPON = r'\**'
t_HASH = r'\#'
t_DOLLAR = r'\$'
t_LT = r'<'
t_GT = r'>'
t_LOREQ = r'<='
t_GOREQ = r'>='
t_EQ = r'='
t_ISDIFF = r'<>'
t_SYMMDIFF = r'><'
t_ASSIG = r':='
t_INCRBY = r'\+='
t_DECRBY = r'\-='
t_MULTBY = r'\*='
t_DIVBY = r'\\='
t_REF = r'@'

# delimeters
t_LP = r'\('
t_RP = r'\)'
t_LBR = r'\['
t_RBR = r'\]'
t_SEMICOL = r';'
t_COL = r':'
t_LCURLBR = r'\{'
t_RCURLBR = r'\}'
# t_LCOMM = r'\(*'
# t_RCOMM = r'\*)'
# t_LGROUP = r'\(.'
# t_RGROUP = r'\.)'


t_INTEGER = r'^[1-9][0-9]*|0$'
t_CHAR= r'(L)?\'([^\\\n]|(\\.))*?\''
t_REAL = r'((\+|-)?([0-9]+)(\.[0-9]+)?)|((\+|-)?\.?[0-9]+)'
t_BOOLEAN = r'(true|false)'
t_EMPTY = r'""'

def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += len(t.value)

def t_ID(t):
    r"""[a-zA-Z][a-zA-Z0-9]*"""
    t.type = reserved.get(t.value, 'ID')
    return t

t_ignore = '  \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()



c_Code = ""
ID_list = []
declar = []
subprogram_decl = []
comp_stats = []


# def p_empty(p):
#     '''empty :'''
#     pass

def p_pascal_program(p):
    '''
    pascal_program : PROGRAM
    '''
    print("ok")

def p_program_id(p):
    '''
    program_id : PROGRAM ID
     '''
    global outputstr
    outputstr += "//Program: " + p[2] + "\n"
    outputstr += "#include <stdio.h>\n"




def p_id_list(p):
    '''
    id_list : id_list COMA ID
    | ID
    '''
    global output
    if(p.length == 3):
        for id in [p[1]]:
            ID_list.append(id)
            if [p[len(p) - 1]] == id:
                output += id
            else:
                output += id + ","


    elif(p.length == 1):
        ID_list.append(p[1])
        output += p[1]



def p_error(p):
    raise Exception("Syntax error at '{}' at line: {}.\n".format(p.value,p.lexer.lineno))


global output
output = ""
with open('test1_correct_syntax') as f:
    lines = f.readlines()
code = "".join(lines)
parser = yacc.yacc()
parser.parse(code)
with open('test1_out.txt', 'w') as file:
    file.write(c_Code)

