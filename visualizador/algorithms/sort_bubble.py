items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    global items, n, i, j, swapped#Ponemos el global en esta parte para no usar un for ya que si usamos el for se va a resolver todo de 1 y no se va poder apreciar a animacion
    if i>=n-1:
        return {"a": -1, "b": -1, "swap": False, "done": True}#lo que suecede aqui es que siempre se va a ir poniendo en la parte final el mas alto
    if j<n-i-1:
        if items[j]>items[j+1]:#aca sucede la comparativa de items donde al ponerle el indice j que va a ser que esta cambiando constante, para asi hacer que el item llegue a la derecha
            items[j], items[j+1]=items[j+1],items[j]#aca sucede el swapeo donde el item[j] y el item[j+1], su comparativa va a seguir hasta que todo el programa quede ordenado(falta hacer que lo mas pequenño quede a la izquierda y que vaya hasta la derecha)
            swapped=True
            resultado= {"a":j, "b":j+1 ,"swap":True, "done":False}#aca sucede si el swap es true se hace el cambio en hasta que termina
        else:
            resultado= {"a":j, "b":j+1 ,"swap":False, "done":False}#en cambio a la linea anterior este es el caso en donde no se lleve a cabo el cambio
        j=j+1#en esta parte es donde le aumentamos el valor a j para que puede seguir iterando 
        return resultado
    else:
        if not swapped:#si no hubo un intercambio en toda la lista,en su defecto la lista queda ordenada
            return {"a": -1, "b": -1, "swap": False, "done": True}
        swapped=False#esto indica el reinicio del indicador de intercambio 
        j=0#indica que se vuelve al inicio de la lista para que empiece la siguiente pasada
        i=i+1#se lleva a acabo la siguiente pasada de la lista 
        return step()
    

