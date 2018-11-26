#92510, Lúcia Filipa Lopes da Silva

#CELULA

def cria_celula(v):
    """recebe o valor do estado de uma celula do qubit e devolve uma celula com esse valor"""
    if v==1 or v==0 or v==-1:
        return (v,)
    else:
        raise ValueError ('cria_celula: argumento invalido')
    
def obter_valor(c):
    """recebe uma celula e devolve o seu valor"""
    return c[0]

def inverte_estado(c):
    """recebe uma celula e devolve a celula resultante de inverter o seu estado"""
    c = cria_celula(trocar(obter_valor(c)))
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
    return isinstance(n,tuple) and n!=()
    
def celulas_iguais(c1, c2):
    """recebe duas celulas e devolve 'verdadeiro' ou 'falso' se estas sao iguais ou nao"""
    return c1==c2           
    
def celula_para_str(c):
    """recebe uma celula e devolve uma cadeia de caracteres"""
    if eh_celula(c):
        if c[0]==-1:
            return 'x'
        else:
            return str(c[0])


#COORDENADA

def cria_coordenada(l,c):
    """devolve a coordenada correspondente a linha l e a coluna c, introduzidas como argumentos"""
    if l not in (0,1,2) or c not in (0,1,2):
        raise ValueError ('cria_coordenada: argumentos invalidos')
    else:
        return (l,c)

def coordenada_linha(c):
    """recebe uma coordenada e devolve a linha"""
    return c[0]                                                         

def coordenada_coluna(c):
    """recebe uma coordenada e devolve a coluna"""
    return c[1]

def eh_coordenada(c):
    """recebe um argumento e devolve 'verdadeiro' ou 'falso', consoante o argumento seja uma coordenada ou nao"""
    return  isinstance(c,tuple) and c!=()
        
def coordenadas_iguais(c1,c2):
    """recebe duas coordendas e devolve 'verdadeiro' ou 'falso' se sao iguais ou nao"""
    return c1==c2

def coordenada_para_str(c):
    """recebe uma coordenada e devolve uma cadeia de caracteres"""
    return str((coordenada_linha(c),coordenada_coluna(c)))
    
    
#TABULEIRO

def tabuleiro_inicial():
    """devolve o tabuleiro que representa o seu estado inicial do jogo"""
    return ((-1,-1,-1),(0,0,-1),(0,-1))  
    
def eh_tabuleiro(t):
    """funcao auxiliar que avalia se o argumento e um tabuleiro ou nao"""
    if isinstance(t,tuple) and len(t)==3:
        for i in range(len(t)):
            if not isinstance(t[i],tuple) or len(t[0])!=len(t[1])!=3 or len(t[2])!=2:
                return False
            else:           
                for e in t[i]:
                    if (e!=0 and e!=1 and e!=-1): #unicos elementos possiveis dos tuplos 
                        return False
        return True
    return False


def tabuleiro_str(t):
    """devolve a cadeia de caracteres que representa o tabuleiro"""
    if not eh_tabuleiro(t):
        raise ValueError ('tabuleiro_str: argumento invalido')
    else:
        n=list(t)
        for i in range(len(n)):
            n[i]=list(n[i]) 
            for e in range(len(n[i])):
                if (n[i][e])== -1: 
                    n[i][e] = 'x'

    return'+-------+\n|...' + str(n[0][2]) + '...|\n|..' + str(n[0][1]) + '.' + \
          str(n[1][2]) + '..|\n|.' + str(n[0][0]) + '.' + str(n[1][1]) + '.' + \
          str(n[2][1]) + '.|\n|..' + str(n[1][0]) + '.' + str(n[2][0]) + '..|\n+-------+' 
    
    
    


