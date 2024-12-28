"""""
lista = [1,1,1,3,3,4,3,2,4,2]
boli= False
for i in range(0, len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] == lista[j]:
            boli=True
print(boli)
"""
boli= False
lista = [1,1,1,3,3,4,3,2,4,2]
seteo = set(lista)
if len(seteo) < len(lista):
    boli= True
print(boli)