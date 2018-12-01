#92510, Lucia Filipa Lopes da Silva

#========================================Celula=================================================

def cria_celula(v):
    """recebe o valor do estado de uma celula do qubit e devolve uma celula com esse valor"""
    if v==1 or v==0 or v==-1:
        return [v]
    else:
        raise ValueError ('cria_celula: argumento invalido.')
    
def obter_valor(c):
    """recebe uma celula e devolve o seu valor"""
    return c[0]

def inverte_estado(c):
    """recebe uma celula e devolve a celula resultante de inverter o seu estado"""
    c[0] = trocar(obter_valor(c))
    return c                        

def trocar(n):
    """funcao auxiliar que troca um elemento 0, 1 para 1,0"""
    if n == 1:
        n = 0
    elif n == 0:
        n = 1
    return n

def eh_celula(n):
    """recebe um argumento e devolve 'verdadeiro' ou falso consoante este seja uma celula"""
    return isinstance(n,list) and n!=[]
    
def celulas_iguais(c1, c2):
    """recebe duas celulas e devolve 'verdadeiro' ou 'falso' se estas sao iguais ou nao"""
    if eh_celula(c1) and eh_celula(c2):
        return obter_valor(c1)==obter_valor(c2)   
    
def celula_para_str(c):
    """recebe uma celula e devolve uma cadeia de caracteres"""
    if eh_celula(c):
        if c[0]==-1:
            return 'x'
        else:
            return str(c[0])


#=========================================Coordenada==============================================

def cria_coordenada(l,c):
    """devolve a coordenada correspondente a linha l e a coluna c, introduzidas como argumentos"""
    if l not in [0,1,2] or c not in [0,1,2]:
        raise ValueError ('cria_coordenada: argumentos invalidos.')
    else:
        return [l,c]

def coordenada_linha(c):
    """recebe uma coordenada e devolve a linha"""
    return c[0]                                                         

def coordenada_coluna(c):
    """recebe uma coordenada e devolve a coluna"""
    return c[1]

def eh_coordenada(coor):
    """recebe um argumento e devolve 'verdadeiro' ou 'falso',\
     consoante o argumento seja uma coordenada ou nao"""
    if isinstance(coor,list) and coor!=[]: 
        l=coordenada_linha(coor)
        c=coordenada_coluna(coor)
        return l in [0,1,2] and c in [0,1,2]
    else:
        return False

def coor_aux(coor):
    """funcao auxiliar que recebe uma coordenada do terceiro tuplo que representa o tabuleiro\
    e associa a cor«ordenada recebida a posicao correta da tabuleiro, por ex, (2,1) representa\
    o valor de (2,0) do tuplo que representa o tabuleiro"""
    if coordenada_linha(coor)==2:
        return [coordenada_linha(coor),coordenada_coluna(coor)-1]
    else:
        return coor

def coordenadas_iguais(c1,c2):
    """recebe duas coordendas e devolve 'verdadeiro' ou 'falso' se sao iguais ou nao"""
    return c1==c2

def coordenada_para_str(c):
    """recebe uma coordenada e devolve uma cadeia de caracteres"""
    return str((coordenada_linha(c),coordenada_coluna(c)))
    

#===============================================Tabuleiro=============================================

def tabuleiro_inicial():
    """devolve o tabuleiro que representa o seu estado inicial do jogo"""
    return [[-1,-1,-1],[0,0,-1],[0,-1]]  
    
def str_valida(s):
    """funcao auxiliar que avalia se o argumento e a representacao interna de um tabuleiro,\
    ou seja, uma cadeia de caracteres que representa um tabuleiro"""
    if isinstance(s,str):
        s=eval(s)
        if len([s])==tabuleiro_dimensao(tabuleiro_inicial()):           
            return eh_tabuleiro([list(s[0]),list(s[1]),list(s[2])])
    else:
        return False                                        

def str_para_tabuleiro(s):
    """recebe uma cadeia de caracteres e devolve o tabuleiro correspondente""" 
    if not str_valida(s):
        raise ValueError ('tabuleiro_str: argumento invalido.')
    else:
        s=eval(s)
        return [list(s[0]),list(s[1]),list(s[2])]

def tabuleiro_dimensao(t):
    """recebe um tabueiro e devolve o numero de linhas (e colunas) que possui"""
    return len(t)                                                                    

def tabuleiro_celula(t,coor):
    """recebe um tabuleiro e uma coordenada e devolve a celula dessa posicao"""
    coor=coor_aux(coor)
    return cria_celula(t[coordenada_linha(coor)][coordenada_coluna(coor)])

def tabuleiro_substitui_celula(t,cel,coor):
    """recebe um tabuleiro, uma celula e uma coordenada e devolve um tabuleiro que substitui a\
     celula na coordenada dada pela celula dada"""
    if not eh_tabuleiro(t) or not eh_celula(cel) or not eh_coordenada(coor):          
        raise ValueError ('tabuleiro_substitui_celula: argumentos invalidos.')
    else:
        t=substitui(t,coor,cel)
        return t
        
def substitui(t,coor,cel):
    """funcao auxiliar que troca uma celula por outra"""   
    coor=coor_aux(coor)   
    l=coordenada_linha(coor)
    c=coordenada_coluna(coor)
    t[l][c]=obter_valor(cel)
    return t

def tabuleiro_inverte_estado(t,coor):                 
    """recebe um tabuleiro e uma coordenada e devolve um tabuleiro com o estado da\
    celula dessa coordenada invertida"""
    if not eh_tabuleiro(t) or not eh_coordenada(coor): 
        raise ValueError ('tabuleiro_inverte_estado: argumentos invalidos.')
    else:
        t=substitui(t,coor,inverte_estado(tabuleiro_celula(t,coor)))
        return t

def eh_tabuleiro(arg):
    """recebe um argumento e avalia se e um tabuleiro"""
    if isinstance(arg,list) and len(arg)==3:
        for i in range(len(arg)):
            if not isinstance(arg[i],list) or len(arg[0])!=len(arg[1])!=3 or len(arg[2])!=2:
                return False
            else:           
                for e in range(len(arg[i])):
                    if not (arg[i][e]==0 or arg[i][e]==1 or arg[i][e]==-1):
                        return False
        return True
    return False

def tabuleiros_iguais(t1,t2):
    """recebe dois tabuleiros e avalia se sao iguais"""
    if eh_tabuleiro(t1) and eh_tabuleiro(t2):
        return t1==t2

def tabuleiro_para_str(t):
    """recebe um tabuleiro e devolve a cadeia de caracteres que o representa"""
    return'+-------+\n|...' + celula_para_str(tabuleiro_celula(t,[0,2])) + '...|\n|..' + \
    celula_para_str(tabuleiro_celula(t,[0,1])) + '.' + celula_para_str(tabuleiro_celula(t,[1,2]))\
    + '..|\n|.' + celula_para_str(tabuleiro_celula(t,[0,0])) + '.' + \
    celula_para_str(tabuleiro_celula(t,[1,1])) + '.' + celula_para_str(tabuleiro_celula(t,[2,2])) \
    + '.|\n|..' + celula_para_str(tabuleiro_celula(t,[1,0])) + '.' + \
    celula_para_str(tabuleiro_celula(t,[2,1])) + '..|\n+-------+' 


#================================================Portas===========================================

def porta_x(t,a):
    """devolve um novo tabuleiro resultante de aplicar a porta x, que dependendo/
    do lado(esquerdo ou direito),troca os elementos entre 1 e 0"""
    if not eh_tabuleiro(t) or (a!='E' and a!='D'):
        raise ValueError('porta_x: argumentos invalidos.')
    else:
        for i in range(tabuleiro_dimensao(t)):
            if a=='E':
                t=tabuleiro_inverte_estado(t,cria_coordenada(tabuleiro_dimensao(t)-2,i))
            else:
                t=tabuleiro_inverte_estado(t,cria_coordenada(i,tabuleiro_dimensao(t)-2))
        return t

def porta_z(t,a):
    """devolve um novo tabuleiro resultante de aplicar a porta z, que dependendo/
    do lado(esquerdo ou direito),troca os elementos entre 1 e 0"""
    if not eh_tabuleiro(t) or (a!='E' and a!='D'):
        raise ValueError('porta_z: argumentos invalidos.')
    else:
        for i in range(tabuleiro_dimensao(t)):
            if a=='E':
                t=tabuleiro_inverte_estado(t,cria_coordenada(tabuleiro_dimensao(t)-3,i))
            else:
                t=tabuleiro_inverte_estado(t,cria_coordenada(i,tabuleiro_dimensao(t)-1))
        return t

def porta_h(t,a):
    """devolve um novo tabuleiro resultante de aplicar a porta h, que dependendo/
    do lado(esquerdo ou direito),troca as colunas do tabuleiro"""
    if not eh_tabuleiro(t) or (a!='E' and a!='D'):
        raise ValueError('porta_h: argumentos invalidos.')
    else:
        for i in range(tabuleiro_dimensao(t)):
            if a=='E':
                celula_1=tabuleiro_celula(t,cria_coordenada(1,i))
                celula_2=tabuleiro_celula(t,cria_coordenada(0,i))
                t=tabuleiro_substitui_celula(t,celula_1,cria_coordenada(0,i))
                t=tabuleiro_substitui_celula(t,celula_2,cria_coordenada(1,i))
            else:
                celula_1=tabuleiro_celula(t,cria_coordenada(i,1))
                celula_2=tabuleiro_celula(t,cria_coordenada(0,2))
                t=tabuleiro_substitui_celula(t,celula_1,cria_coordenada(i,2))
                t=tabuleiro_substitui_celula(t,celula_2,cria_coordenada(i,1))
        return t

#==========================================Hello Quantum=======================================

def hello_quantum(s):
    """recebe uma cadeia de caracteres com o tabuleiro a que se qer chegar e o numero\
    de jogadas maximo que se pode fazer"""
    print('Bem-vindo ao Hello Quantum!\nO seu objetivo e chegar ao tabuleiro:')
    tab_str=''
    jogada,i=0,0
    t=()
    tentativa=0
    while s[i]!=':':
        tab_str=tab_str+s[i]
        i = i+1
    for e in range(i+1,len(s)):
        jogada= jogada+eval(s[e])
    print(tabuleiro_para_str(str_para_tabuleiro(tab_str)),'\nComecando com o tabuleiro que se segue:\
    \n'tabuleiro_para_str(tabuleiro_inicial()))
    t=tabuleiro_inicial()
    while jogada!=tentativa:
        porta=input('Escolha uma porta para aplicar (X, Z ou H): ')
        lado=input('Escolha um qubit para analisar (E ou D): ')

        if str(porta)=='X':
            t=porta_x(t,str(lado))
            print(tabuleiro_para_str(t))
            tentativa=tentativa+1
        elif str(porta)=='Z':
            t=porta_z(t,str(lado))
            print(tabuleiro_para_str(t))
            tentativa=tentativa+1
        else:
            t=porta_h(t,str(lado))
            print(tabuleiro_para_str(t))
            tentativa=tentativa+1

    if tabuleiros_iguais(t,tab_str):
        print('Parabens, conseguiu converter o tabuleiro em',tentativa,'jogadas!')
    else:
        return False    


     




