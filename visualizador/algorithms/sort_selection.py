# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # marcador de pasadas
j = 0          # recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    global items, n, i, j, min_idx, fase
    
    if i >= n-1:    #comprobamos si ya recorrimos toda la lista y termina el algoritmo
        return {"done": True}
    
    if fase == "buscar":    #buscamos el mínimo en la pasada actual
        if items[j] < items[min_idx]:
            min_idx = j
        j += 1
        
        if j >= n:    #si recorre toda la lista, pasa a la fase de swap
            fase = "swap"
            return {"a": min_idx, "b": j-1, "swap": False, "done": False}
        
        return {"a": min_idx, "b": j, "swap": False, "done": False}
    
    elif fase == "swap":    #
        swap = False
        a = i
        b = min_idx
        
        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]
            swap = True
        
        i += 1
        j = i + 1
        min_idx = i
        fase = "buscar"
        
        if i >= n-1:
            return {"done": True}
        
        return {"a": a, "b": b, "swap": swap, "done": False}