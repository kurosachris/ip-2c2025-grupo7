items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items) #Cantidad de elementos de la lista
    i = 0#Pasada actual (cuántos elementos ya están ordenados al final)
    j = 0#Indice de comparación dentro de esa pasada
def step():
    global items, n, i, j, swapped
    if i>=n-1:#Si ya hicimos todas las pasadas correspondientes el algoritmo termina
        return {"a": -1, "b": -1, "swap": False, "done": True}
            #-1 marcador que no tenemos indices activos
            #Done true representa que el programa termino
    
    if j<n-i-1:#Comparacion que se realiza dentro de la pasada actual
        if items[j]>items[j+1]:
            items[j], items[j+1]=items[j+1],items[j]
            swapped=True#La bandera funciona para indicar que si hubo un swapeo
            resultado= {"a":j, "b":j+1 ,"swap":True, "done":False}
            #A y B toman los valores de los elementos comparados y swapean
        else:
            #Si no hubo un swap se registra la comparacion 
            resultado= {"a":j, "b":j+1 ,"swap":False, "done":False}
        j=j+1#Aumentamos j para pasar al siguiente par de elementos
        return resultado
    else:
        if not swapped:
            #Si no se realizo ningun swap, significa que la lista esta ordenada
            return {"a": -1, "b": -1, "swap": False, "done": True}
        swapped=False #Reiniciamos la bandera de intercambio
        j=0           #Volvemos al inicio de la lista
        i=i+1         #Avanzamos a la siguiente pasada
        return step()
    

