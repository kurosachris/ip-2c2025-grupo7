# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0      # elemento que queremos insertar
j = None   # cursor de desplazamiento hacia la izquierda (None = empezar)

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # Controla que elemento se inserta
    j = None #Se mueve a al izquierda para utilizar el elemento en su lugar

def step():
        global items, n, i, j
        if i>=n:#Si i ya llego al final de la lista, significa que el algoritmo termino
            return{"a": -1, "b": i-1, "swap":False, "done": True}#Devuelve un diccionario con done:True lo que significa que termino y a,b=-1 es un Marcador que indica que no ahi indice activos
        if j ==None:#Al iniciar cada insercion  j todavia no tiene ningun valor es por eso que decimos que J==None(esta vacio)
            j=i#Es el iniciador del curso interno correspondiendo a la  poscion del elemento que se desea insertar, por lo que J empieza a estar listo para hacer la comparacion hacia la izquierda
            return{"a":i, "b":i, "swap":False, "done": False}#Tanto "a" y "b" son i porque todavia no se hizo ninguna comparacion o swap, solo se marca el elemento que se va a insertar, el "swap" en false indica que no se realizo ningun Swap, el "done" en false indica que el algoritmo sigue
        if j>0 and items[j-1] > items[j]:#Si el elemento al izquierda(items[j-1]) es mayor que el actual (items[j]) se realiza un swap
                items[j-1], items[j] = items[j], items[j-1]
                ret={"a": j-1, "b": j, "swap": True, "done": False}#Se devuelve el estado con los items que realizaron el swap(a=j-1 y b=j), como se realizo el swap, "swap"se coloca en true 
                j=j-1#Indica que J se mueve una posicion hacia la izquierda para seguir comparando
                return ret
        else:#Si no se realiza un swap significa que items estan en su poscion correspondiente 
              i=i+1#Avanza a i al siguiente elemento
              j=None#Se resetea 
        return {"a": -1, "b": i-1, "swap": False, "done": False}
   
