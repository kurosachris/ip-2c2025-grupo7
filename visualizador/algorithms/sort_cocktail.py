# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
j = 0
izq = 0
der = 0
tecla = True

def init(vals):
    global items, n, i, j, izq, der, tecla
    items = list(vals)
    n = len(items)
    j = 0
    izq = 0
    der = n - 1
    tecla = True

def step():
    global items, n, j, izq, der, tecla
    
    if izq >= der:
        return {"done": True}
    
    swap = False
    a = j
    b = j + 1
    
    if tecla:
        if j >= der:
            der -= 1
            tecla = False
            j = der
            if izq >= der:
                return {"done": True}
            a = j
            b = j - 1
            if items[a] < items[b]:
                items[a], items[b] = items[b], items[a]
                swap = True
            j -= 1
            if j <= izq:
                izq += 1
                tecla = True
                j = izq
                if izq >= der:
                    return {"done": True}
        else:
            a = j
            b = j + 1
            if items[a] > items[b]:
                items[a], items[b] = items[b], items[a]
                swap = True
            j += 1
            if j >= der:
                der -= 1
                tecla = False
                j = der
                if izq >= der:
                    return {"done": True}
    
    else:
        a = j
        b = j - 1
        if j <= izq:
            izq += 1
            tecla = True
            j = izq
            if izq >= der:
                return {"done": True}
            a = j
            b = j + 1
            if items[a] > items[b]:
                items[a], items[b] = items[b], items[a]
                swap = True
            j += 1
            if j >= der:
                der -= 1
                tecla = False
                j = der
                if izq >= der:
                    return {"done": True}
        else:
            if items[a] < items[b]:
                items[a], items[b] = items[b], items[a]
                swap = True
            j -= 1
            if j <= izq:
                izq += 1
                tecla = True
                j = izq
                if izq >= der:
                    return {"done": True}
    return {"a":a, "b":b, "swap": swap, "done":False}