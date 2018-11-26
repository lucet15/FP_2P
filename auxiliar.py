def numero_cel(n):
    """funcao auxiliar que recebe uma lista e confirma se o primeiro elemento e 0, 1 ou -1"""
    return n[0]==0 or n[0]==1 or n[0]==-1   

def numero_coor(c):
    """funcao auxiliar que recebe uma lista e confirma se os elementos sao 0, 1 ou 2"""    
    for i in range(len(c)):
        if c[i]!=0 or c[i]!=1 or c[i]!=2:
            return False
    return True