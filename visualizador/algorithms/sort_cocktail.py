items = []     
n = 0   
j = 0
izq = 0    #define el límite izquierdo               
der = 0    #define el límite derecho
tecla = True    #es el "switch" que controla la dirección del recorrido

def init(vals):
    global items, n, j, izq, der, tecla
    items = list(vals)
    n = len(items)
    j = 0
    izq = 0    #el límite izquierdo inicia en el primer elemento de la lista
    der = n - 1    #el límite derecho inicia en el último elemento de la lista
    tecla = True    

def step():
    global items, n, j, izq, der, tecla

    if izq >= der:         #si los límites del recorrido se cruzan, el programa termina
        return {"done": True}

    swap = False
    
    if tecla:    #recorrido de izquierda a derecha
        a = j 
        b = j + 1

        if items[a] > items[b]:
            items[a], items[b] = items[b], items[a]
            swap = True
        j += 1 

        if j >= der:
            tecla = False
            der -= 1   #establece el nuevo límite derecho

    else:     #recorrido de derecha a izquierda
        a = j
        b = j - 1
        if items[a] < items[b]:
            items[a], items[b] = items[b], items[a]
            swap = True
        j -= 1    

        if j<=izq:
            tecla = True
            izq += 1     #establece el nuevo límite izquierdo

    return {"a": a, "b": b, "swap": swap, "done": False}          