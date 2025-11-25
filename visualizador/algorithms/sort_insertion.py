

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
            #-1 es un marcador que no tenemos indices activos 
            
        
        if j ==None:#Inicializador de j para empezar una nueva insercion
            j=i#J empieza en la poscion del elemento que se desea insertar
            return{"a":i, "b":i, "swap":False, "done": False}
            #Tanto "a" como "b" funcionan para marcar el elemento que se va a insertar
            
        
        if j>0 and items[j-1] > items[j]:#Condicion donde se realiza el swap
                items[j-1], items[j] = items[j], items[j-1]
                ret={"a": j-1, "b": j, "swap": True, "done": False}
                #"a"y "b" son los indices de los elementos que se compararon e intercambiaron
                j=j-1#J retrocede una posicion para continuar la comparativa hacia la izquierda
                return ret
        
        else:#Si no se realizo un swap significa que el elemento esta en su posicion
              i=i+1 
              j=None #Reiniciamos j para que se pueda dar la proxima insercion
            
            #No se realizo ningun swap pero el algoritmo aun no termina
        return {"a": -1, "b": i-1, "swap": False, "done": False}
                
