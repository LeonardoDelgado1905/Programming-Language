#Alfabeto caracterizado

#Minusculas
chars_min_almost_complete = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
char_n = ['n']
chars_min = chars_min_almost_complete
chars_min.insert(chars_min.index('m') + 1, char_n[0])

#Mayusculas
chars_may =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Caracteres completos
chars = chars_min + chars_may

#Números
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Símbolos
symbol_point = ['.']
symbol_asterisk = ['*']
symbol_slash = ['/']
symbols_almost_complete = ['+', '-', '%', '=', '<', '>', '<=', '>=', '==', '&&', '||', '!=', '!', ':', ';', ',', '(', ')', '&', '|']
symbols = symbols_almost_complete
symbols.insert(symbols.index('-') + 1, symbol_asterisk[0])
symbols.insert(symbols.index('*') + 1, symbol_slash[0])
symbols.insert(symbols.index(',') + 1, symbol_point[0])

#Símbolos especiales
char_qsimple = ['\'']
char_blank  = [' ']
char_underscore = ['_']
char_backslash = ['\\']
char_quote = ['"']
special_symbols = char_qsimple + char_blank + char_underscore + char_backslash + char_quote

alphabet = chars + numbers + symbols + special_symbols

#------------------------------------------------------------------------------

#Tipos de token

#Palabras reservadas
data_types = ['booleano', 'caracter', 'entero', 'real', 'cadena']
boolean_options = ['verdadero', 'falso']
reserved_words = data_types + boolean_options + ['funcion_principal', 'fin_principal', 'leer', 'imprimir', 'si', 'entonces', 'fin_si', 'si_no', 'mientras', 'hacer', 'fin_mientras', 'para', 'fin_para', 'seleccionar', 'entre', 'caso', 'romper', 'defecto', 'fin_seleccionar', 'estructura', 'fin_estructura', 'funcion', 'retornar', 'fin_funcion']


#Token Símbolos
token_symbols = ['tk_mas', 'tk_menos', 'tk_mult', 'tk_div', 'tk_mod', 'tk_asig', 'tk_menor', 'tk_mayor', 'tk_menor_igual', 'tk_mayor_igual', 'tk_igual', 'tk_y', 'tk_o', 'tk_dif', 'tk_neg', 'tk_dosp', 'tk_pyc', 'tk_coma', 'tk_punto', 'tk_par_izq', 'tk_par_der']

#Token típo de datos
token_data = ['tk_' + x for x in data_types]

#Token palabras reservadas sin opciones de booleano es la identidad por eso no se crea un arreglo.

possible_token_names = token_symbols + token_data + reserved_words + ['id']

#----------------------------------------------------------------


trans_lex = [{} for i in range(16)]

def createRules(trans_lex):
        
    #REGLAS
    
    
    # for j in range (13):
    #     print("-------------" + str(j))
    #     for i in trans_lex[j]:
    #         print (i, trans_lex[j][i])
    
    
    # trans_lex[0]['c']  = 'prro'
    
    # trans_lex[1]['p'] = ([], 0)
    # print(trans_lex)
    
    
    # print(trans_lex)
    ## q0
    
    #palabras
    for x in chars:
        trans_lex[0][x] = ([], 6)
    #numeros
    for x in numbers:
        trans_lex[0][x] = ([], 7)
    #caracter
    trans_lex[0][char_qsimple[0]] = ([], 1)
    # 
    trans_lex[0][char_blank[0]] = ([], 0)
    
    #cadena
    trans_lex[0][char_quote[0]] = ([], 4)
    
    #comentario
    trans_lex[0][symbol_slash[0]] = ([], 5)
    
    #símbolos
    for x in list(set(symbols) - set(symbol_slash)):
        trans_lex[0][x] = ([], 10)
    
    #posible = logico
    trans_lex[0]['|'] = ([], 14)
    
    #posible Y logico
    trans_lex[0]['&'] = ([], 15)
    
    
    
    
    ##q1 caracter
    
    
    #Careacteres válidos
    for x in list(chars + numbers + char_blank + char_underscore + symbols):
        trans_lex[1][x] = ([], 2)
        
    #BackSlash
    trans_lex[1][char_backslash[0]] = ([], 3)
    # trans_lex[1][char_qsimple[0]] = (['tk_caracter'], 0)
    
    
    
    ##q2 terminaCaracter
    trans_lex[2][char_qsimple[0]] = (['tk_caracter'], 0)
    
    ##q3 para hacer \n 
    trans_lex[3][char_n[0]] = ([], 2)
    
    ##q4 trasnCadenas (caracteres validos)
    
    for x in list(chars + numbers + char_blank + char_underscore):
        trans_lex[4][x] = ([], 4)
    
    #Backsalsh    
    trans_lex[4][char_backslash[0]] = ([], 13)
    
    #Termina cadena
    trans_lex[4][char_quote[0]] = (["tk_cadena"], 0)
    
    
    ##q13 para \n en caracteres
    trans_lex[13][char_n[0]] = ([], 4)
    
    ##q5 Comentarios
    
    #Palabras
    for x in chars:
        trans_lex[5][x] = (["tk_div"], 6)
    
    #Numeros
    for x in numbers:
        trans_lex[5][x] = (["tk_div"], 7)
    
    #Simbolos
    for x in list(set(symbols) - set(symbol_asterisk) - set(symbol_slash)):
        trans_lex[5][x] = (["tk_div"], 10)
        
    #posible = logico
    trans_lex[5]['|'] = ([], 14)
    
    #posible Y logico
    trans_lex[5]['&'] = ([], 15)
    
    #Caracter
    trans_lex[5][char_qsimple[0]] = (["tk_div"], 1)
    
    #Espacio
    trans_lex[5][char_blank[0]] = (["tk_div"], 0)
    
    #Cadena
    trans_lex[5][char_quote[0]] = (["tk_div"], 4)
    
    #Commentario en linea
    trans_lex[5][symbol_slash[0]] = (["IgnorarLinea"], 0)
    
    #Commentario en bloque
    trans_lex[5][symbol_asterisk[0]] = ([], 11)
    
    
    ##q11 
    for x in list(set(alphabet) - set(symbol_asterisk)):
        trans_lex[11][x] = ([], 11)
        
    
    #asterisco
    trans_lex[11][symbol_asterisk[0]] = ([], 12)
    # print(trans_lex[11])
    
    ##q12 
    
    for x in list(set(alphabet) - set(symbol_slash)):
        trans_lex[12][x] = ([], 11)
    #Termina el comentario
    trans_lex[12][symbol_slash[0]] = ([], 0)
    
    
    ##q6 Palabras
    
    #Caracteres validos
    for x in list(chars + numbers + char_underscore):
        trans_lex[6][x] =([], 6)
        
    #Simbolos
    for x in list(set(symbols) - set(symbol_slash)):
        trans_lex[6][x] = (["palabra"], 10)
    
    #posible = logico
    trans_lex[6]['|'] = (["palabra"], 14)
    
    #posible Y logico
    trans_lex[6]['&'] = (["palabra"], 15)
    
    #posible slahs
    trans_lex[6][symbol_slash[0]] = (["palabra"], 5)
    #Caracter
    trans_lex[6][char_qsimple[0]] = (["palabra"], 1)
    
    #Espacio
    trans_lex[6][char_blank[0]] = (["palabra"], 0)
    
    #Cadena
    trans_lex[6][char_quote[0]] = (["palabra"], 4)
    
    
    ## q7 Números
    
    #empieza palabra
    for x in chars:
        trans_lex[7][x] = (["tk_entero"], 6)
        
    #Sigue entero
    for x in numbers:
        trans_lex[7][x] = ([], 7)
        
    #simbolos
    for x in list(set(symbols) - set(symbol_point) - set(symbol_slash)):
        trans_lex[7][x] = (["tk_entero"], 10)

    #posible = logico
    trans_lex[7]['|'] = (["tk_entero"], 14)
    
    #posible Y logico
    trans_lex[7]['&'] = (["tk_entero"], 15)
    
    #posible slahs
    trans_lex[7][symbol_slash[0]] = (["tk_entero"], 5)
    
    #posible decimal
    trans_lex[7][symbol_point[0]] = ([], 8)
    
    #empieza Cadena
    trans_lex[7][char_quote[0]] = (["tk_entero"], 4)
    
    #empieza caracter
    trans_lex[7][char_qsimple[0]] = (["tk_entero"], 1)
    
    #espacio
    trans_lex[7][char_blank[0]] = (["tk_entero"], 0)
    
    
    ## q8 Posible decimal
    
    #empieza palabra
    for x in chars:
        trans_lex[8][x] = (["tk_entero", "tk_punto"], 6)
        
    #Efectivamente decimal
    for x in numbers:
        trans_lex[8][x] = ([], 9)
        
    #Simbolos
    for x in list(set(symbols) - set(symbol_slash)):
        trans_lex[8][x] = (["tk_entero", "tk_punto"], 10)
    
    #posible = logico
    trans_lex[8]['|'] = (["tk_entero", "tk_punto"], 14)
    
    #posible Y logico
    trans_lex[8]['&'] = (["tk_entero", "tk_punto"], 15)
    
    #posible slahs
    trans_lex[8][symbol_slash[0]] = (["tk_entero", "tk_punto"], 5)
    
    
    #empieza Cadena
    trans_lex[8][char_quote[0]] = (["tk_entero", "tk_punto"], 4)
    
    #empieza caracter
    trans_lex[8][char_qsimple[0]] = (["tk_entero", "tk_punto"], 1)
    
    #espacio
    trans_lex[8][char_blank[0]] = (["tk_entero", "tk_punto"], 0)
    
    
    ## q9 Decimal
    
    #empeiza palabra
    for x in chars:
        trans_lex[9][x] = (["tk_real"], 6)
        
    #Sigue entero
    for x in numbers:
        trans_lex[9][x] = ([], 7)
        
    #Simbolos
    for x in list(set(symbols) - set(symbol_slash)):
        trans_lex[9][x] = (["tk_real"], 10)
    
    #posible = logico
    trans_lex[9]['|'] = (["tk_real"], 14)
    
    #posible Y logico
    trans_lex[9]['&'] = (["tk_real"], 15)
    
    #posible slahs
    trans_lex[9][symbol_slash[0]] = (["tk_real"], 5)
    
    #empieza Cadena
    trans_lex[9][char_quote[0]] = (["tk_real"], 4)
    
    #empieza caracter
    trans_lex[9][char_qsimple[0]] = (["tk_real"], 1)
    
    #espacio
    trans_lex[9][char_blank[0]] = (["tk_real"], 0)
    
    
    ## q10 Símbolos
    
    #empeiza palabra
    for x in chars:
        trans_lex[10][x] = (["simbolo"], 6)
        
    #Sigue entero
    for x in numbers:
        trans_lex[10][x] = (["simbolo"], 7)
        
    #simbolos
    for x in list(set(symbols) - set(['|', '&', '/'])):
        trans_lex[10][x] = ([], 10)
        
    #posible slahs
    trans_lex[10][symbol_slash[0]] = (["palabra"], 5)
    
    #es un posible ||
    trans_lex[10]['|'] = ([], 14)
    
    #es un posible &&
    trans_lex[10]['&'] = ([], 15)
    
    #empieza Cadena
    trans_lex[10][char_quote[0]] = (["simbolo"], 4)
    
    #empieza caracter
    trans_lex[10][char_qsimple[0]] = (["simbolo"], 1)
    
    #espacio
    trans_lex[10][char_blank[0]] = (["simbolo"], 0)
    
    
    ##q14 ||
    trans_lex[14]['|'] = (["simbolo"], 0)
    
    
    ##q15 &&
    trans_lex[15]['&'] = (["simbolo"], 0)


#Si termina en estos estados, es probable que su toquen sea el respectivo
potential_tokens = [[]]*16

potential_tokens[1] = ['error']
potential_tokens[2] = ['tk_caracter']
potential_tokens[3] = ['error']
potential_tokens[4] = ['tk_cadena']
potential_tokens[5] = ['tk_div']
potential_tokens[13] = ['error']
potential_tokens[11] = ['error']
potential_tokens[12] = ['error']
potential_tokens[6] = ['palabra']
potential_tokens[7] = ['tk_entero']
potential_tokens[8] = ['tk_entero', 'tk_punto']
potential_tokens[9] = ['tk_real']
potential_tokens[10] = ['simbolo']
potential_tokens[14] = ['simbolo']
potential_tokens[15] = ['simbolo']


def decodificarToken(token, lexema): #Decodificar cuando tenemos: simbolo, palabra
    if(token == "palabra"):
        if(lexema in list(reserved_words)):
            return lexema
        else:
            return "id"
    elif(token == "simbolo"):
        return token_symbols[symbols.index(lexema)]

def decodingSymbols(buffer): #Cuantos simbolos hemos leido hasta el momento?
    symbol_lexeme = []
    pure_symbols = list(set(symbols) - set(['&', '|']))
    # print("me pidieron decodificar el *" + buffer + "*" )
    doble = False
    last_viewd = -1
    for sidx in range (len(buffer)-1):
        if doble:
            doble = False
            continue
        if(buffer[sidx:sidx+2] in pure_symbols):
            symbol_lexeme.append(("simbolo", buffer[sidx:sidx+2]))
            last_viewd = sidx+1
            doble = True
        elif(buffer[sidx] in pure_symbols):
            symbol_lexeme.append(("simbolo", buffer[sidx]))
            last_viewd = sidx
        else:
            symbol_lexeme.append(("Error", buffer[sidx]))
            break
        
    if(last_viewd < len(buffer)-1):        
        if(buffer[-1] in pure_symbols):
              symbol_lexeme.append(("simbolo", buffer[-1]))
        else:
            symbol_lexeme.append(("Error", buffer[-1]))
  
    return symbol_lexeme

def printToken(tk, lexema, fil, col):
    if(lexema != -1):    
        print("<" + tk + "," + lexema + "," + str(fil+1) + "," + str(col+1) + ">")
    else:
        print("<" + tk + "," + str(fil+1) + "," + str(col+1) + ">")
    
def printError(fil, col):
    print(">>> Error lexico (linea: " + str(fil+1) + ", posicion: " + str(col+1)+")")

def manageToken(tk, lexeme, fil, col):
    if tk in possible_token_names:
        if(tk in reserved_words or tk in token_symbols):
            lexeme = -1
        printToken(tk, lexeme, fil, col)
        return True
    elif(tk == 'simbolo' or tk == 'palabra'): #los únicos dos válidos, no mira errores
        # print("añlskdjfhsd fa-s-------------------------------------")
        if tk == 'simbolo':
            
            # print("ey simbolo ", tk, lexeme)
            dec_sym = decodingSymbols(lexeme)
            error = False
            # print("########" + lexeme)
            # print("decode = ", dec_sym)
            for tks, lexeme in dec_sym:
                error = (tks == "Error")
                if error:
                    printError(fil, col + len(lexeme))
                    return False
                t = decodificarToken(tks, lexeme)
                
                printToken(t, -1, fil, col)
                col += len(lexeme)                    
        elif tk == 'palabra':
            t = decodificarToken(tk, lexeme)
            lexeme = lexeme if t == 'id' else -1                      
            # print("mi lexe es: " + lexeme)
            printToken(t, lexeme, fil, col)
        return True
    return True

def printTokens(tokens, buffer, fil, col):
    # print(tokens, buffer)
        
    if len(tokens) == 2:
        return manageToken(tokens[0], buffer[:-1], fil, col) and manageToken(tokens[1], buffer[-1], fil, col + len(buffer)-1)
    elif len(tokens) == 1:
        return manageToken(tokens[0], buffer, fil, col)
    return True


import sys, os


# orig_stdout = sys.stdout

createRules(trans_lex)
readInFile = 1
# print(orig_stdout)
#for line in sys.stdin.read():
if(readInFile):
    # with open('miSalida.txt', 'w') as fout:
    #     sys.stdout = fout
    os.chdir(r'C:\Users\LeonardoDelgado\Desktop\Lenguajes\Programming-language\lexico')
    f = open('prueba.txt', "r")
    lines = f.readlines()
else:    
    lines = sys.stdin.readlines() 
current_state = 0
error = False


saveFila = 0
saveCol = 0
for fila in range(len(lines)):
    buffer = ""
    line = lines[fila]
    col_start_token = 0
    if(current_state != 11 and current_state != 12):
        current_state = 0    
    
    for col in range (len(line)): 
        # print(current_state)
        if(current_state == 0): #siempre que vaya al estado inicial debe limpiar el buffer
            buffer = ""
            col_start_token = col
        current_character = line[col]
        if(ord(current_character) == 13 or current_character == '\n'): #Saltos de linea en diferentes codificaciones
            continue
        if(ord(current_character) == 9): #Codificación de un tab
            col_start_token += 1
            continue
        buffer += current_character
        if(current_state == 11 and current_character != '*'): #Si estoy en modo comentario multilinea ignoro todo lo que leo
            continue
        elif(current_state == 12 and current_character != '/'):
            current_state = 12 if current_character == '*' else 11
            continue
        # print(current_character + " -> " + buffer)
        # if(current_state == 11 or current_state == 12): #Si está en comentario debe ignorarlo que lee
            # col_start_token = col
            # print("mira toy en " + str(current_state) + " y recibi " + current_character)
            
            
        # print("estoy en " + str(current_state) + " y me voy para " + str(current_character))
        # if(buffer == ' '):
        #     buffer = ""
        #     col_start_token += 1
            # continue
        # print(buffer)
        #//ignorar comentarios#
        if(trans_lex[current_state].get(current_character)  is None): #No encuentra el siguiente caracter
            # print("no encontrado *"+current_character+"* desde " + str(current_state))
            # print("Buscare en *" + buffer[:-1] +"¨*")
            # if(current_state == 3)
            # print(ord(current_character))
            printTokens(potential_tokens[current_state], buffer[:-1], fila, col_start_token)    
            printError(fila, col)
            error = True
            break
        else:            
            tokens, next_state = trans_lex[current_state][current_character]
            # print(next_state)
            if(next_state == 11):
                saveFila = fila
                saveCol = col-1
            current_state = next_state
            if(tokens and tokens[0] == 'IgnorarLinea'):
                break
            
            # print("PERO MIRA QUE MI CARACTER ES: " + current_character)
            # buffer_real = buffer if (current_character == char_qsimple[0] or current_character == char_quote[0] or current_character == '&' or current_character == '|')  else buffer[:-1]
            
            buffer_real = buffer if (next_state == 0 and current_character != ' ') else buffer[:-1]
            # print("*" + buffer_real + "*")
            # buffer_real = buffer_real.replace(' ', '')
            error = not printTokens(tokens, buffer_real, fila, col_start_token)
            # print(buffer)
            if(tokens):
                col_start_token += len(buffer_real)
                buffer = buffer[len(buffer_real):]
                # if(buffer == ' '):
                #     buffer = ''
                #     col_start_token += 1
                # print("obvi quedamos con : " + buffer, (len(buffer_real) == len(buffer)))
    # print(error)
    if error == True:
        break   
    if(current_state != 11 and current_state != 12 and potential_tokens[current_state] == ['error']):
        printError(fila, col)
        break
    else:
        printTokens(potential_tokens[current_state], buffer, fila, col_start_token)    
    
if(current_state == 11 or current_state == 12):
    printError(saveFila, saveCol)
#sys.stdout = orig_stdout