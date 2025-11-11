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
    global items, n, i, j, swapped
    if i>=n-1:
        return {"a": -1, "b": -1, "swap": False, "done": True}
    if j < n - i - 1:
        if items[j]<items[j+1]:
            items[j], items[j+1]=items[j+1],items[j]
            swapped=True
            resultado= {"a":j, "b":j+1 ,"swap":True, "done":False}
        else:
            resultado= {"a":j, "b":j+1 ,"swap":False, "done":False}
        j=j+1
        return resultado
    else:
        if not swapped:
            return {"a": -1, "b": -1, "swap": False, "done": True}
        swapped=False
        j=0
        i=i+1
        return step