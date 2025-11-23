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
        #Tanto "a" como "b"son los indices que utilizamos para comparar(el -1 que se encuentra en a y b es un marcador que demuestra que no tenenemos indices activos)
        #Swap:Indica si hubo un intercambio, en este caso swap es false por lo que no se realizo ningun intercambio
        #Done:Es el que controla cuando termina el programa, como Done esta en True significa que el programa termino

    if j<n-i-1:#Comparacion que se realiza dentro de la pasada actual
        if items[j]>items[j+1]:
            #Si el elemento con el indice j es mayor que el elemento con el indice j+1 se realiza un swap
            items[j], items[j+1]=items[j+1],items[j]
            swapped=True#La bandera funciona para indicar que si hubo un swapeo
            resultado= {"a":j, "b":j+1 ,"swap":True, "done":False}
            #A y B toman los valores de los elementos comparados, A es el primer elemento que se compara y B el segundo
            #En este caso swap es True porque si hubo un intercambio
            #Done siguien siendo false porque todavia la lista no queda ordenada
        else:
            #Si no hubo un swap tambien registramos la comparacion que se realizo
            resultado= {"a":j, "b":j+1 ,"swap":False, "done":False}
        j=j+1#Aumentamos j para pasar al siguiente par de elementos(j y j+1) que se encuentran en la pasada actual
        return resultado
    else:
        #Se ejecuta cuando se llega al final de la pasada 
        if not swapped:
            #Si no se realizo ningun swap, significa que la lista esta ordenada
            return {"a": -1, "b": -1, "swap": False, "done": True}
        swapped=False #Reiniciamos la bandera de intercambio
        j=0           #Volvemos al inicio de la lista
        i=i+1         #Avanzamos a la siguiente pasada
        return step()
    

