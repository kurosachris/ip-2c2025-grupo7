# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # común: arrancar en el segundo elemento
    j = None

def step():
        global items, n, i, j
        if i>=n:
            return{"a": -1, "b": i-1, "swap":False, "done": True}
        if j ==None:
            j=i
            return{"a":i, "b":i, "swap":False, "done": False}
        if j>0 and items[j-1] > items[j]:
                items[j-1], items[j] = items[j], items[j-1]
                ret={"a": j-1, "b": j, "swap": True, "done": False}
                j=j-1
                return ret
        else:
              i=i+1
              j=None
        return {"a": -1, "b": i-1, "swap": False, "done": False}
#cosas a arreglar, el codigo todavia no funciona, queda termianr de darle una vuelta de tuerca a insertion, si no estoy mal la gran mayoria deberia de estar bien, aunque falta lo mas importante


    
    # TODO:
    # - Si i >= n: devolver {"done": True}.
    # - Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
    # - Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.
    # - Si ya no hay que desplazar: avanzar i y setear j=None.
   
