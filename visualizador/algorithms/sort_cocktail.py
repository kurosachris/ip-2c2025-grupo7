# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0
izq = 0
der = 0
tecla = True

def init(vals):
    global items, n, i, j, izq, der, tecla
    items = list(vals)
    n = len(items)
    i = 0
    j = 0
    izq = 0
    der = n - 1
    tecla = True

def step():
    global items, n, i, j, izq, der, tecla
    
    if izq >= der:
        return {"done": True}
    
    if tecla:
        swap = False
        a = j
        b = j + 1
        if items[a] > items[b]:
            items[a], items[b] = items[b], items[a]
            swap = True
            j += 1
            if j >= der:
                j = der - 1
                der -= 1
                tecla = False
                i =+ 1
    
    else:
        a = j
        b = j - 1
        if items[a] < items[b]:
            items[a], items[b] = items[b], items[a]
            swap = True
            j -= 1
            if j <= izq:
                j = izq
                izq += 1
                tecla = True
                i += 1
    return {"a":a, "b":b, "swap": swap, "done":False}


    


    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # TODO:
    # 1) Elegir índices a y b a comparar en este micro-paso (según tu Bubble).
    # 2) Si corresponde, hacer el intercambio real en items[a], items[b] y marcar swap=True.
    # 3) Avanzar punteros (preparar el próximo paso).
    # 4) Devolver {"a": a, "b": b, "swap": swap, "done": False}.
    #
    # Cuando no queden pasos, devolvé {"done": True}.
    return {"done": True}