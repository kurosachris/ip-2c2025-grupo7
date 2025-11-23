

items = []
n = 0
i = 0      
j = None   

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1      # Controla que elemento se inserta
    j = None #Se mueve a al izquierda para utilizar el elemento en su lugar

def step():
        global items, n, i, j
        if i>=n:#Si i ya llego al final de la lista, significa que el programa termino
            return{"a": -1, "b": i-1, "swap":False, "done": True}
            #Tanto "a" como "b"son los indices que utilizamos para comparar(el -1 que se encuentra en a y b es un marcador que demuestra que no tenenemos indices activos)
            #Swap False representa que no se realizo ningun intercambio
            #Done:Si Done esta en True significa que el programa termino
        
        if j ==None:#Inicializador de j para empezar una nueva insercion
            j=i#J empieza en la poscion del elemento que se desea insertar
            return{"a":i, "b":i, "swap":False, "done": False}
            #Tanto "a" como "b" funcionan para marcar el elemento que se va a insertar
            #Swap:es False porque no se realizo ningun swapeo
            #done: es False porque todavia el programa no termino 
        
        if j>0 and items[j-1] > items[j]:#Si el elemento que se encuentra a la izquierda (item[j-1]) es mayor que el actual (items[i]), se realiza el swap
                items[j-1], items[j] = items[j], items[j-1]#En esta linea de codigo se realiza el intercambio
                ret={"a": j-1, "b": j, "swap": True, "done": False}
                #"a"y "b" son los indices de los elementos que se compararon e intercambiaron
                #Swap true representa que si hubo un intercambio
                j=j-1#J retrocede una posicion para continuar la comparativa hacia la izquierda
                return ret
        
        else:#Si no se realizo un swap significa que el elemento esta en su posicion
              i=i+1 #Se avanza a la siguiente posicion de la insercion
              j=None #Reiniciamos j para que se pueda dar la proxima insercion
            
            #No se realizo ningun swap pero el algoritmo aun no termina
        return {"a": -1, "b": i-1, "swap": False, "done": False}
                
