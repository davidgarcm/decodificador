lista = list(range(1000))
print(sum(list(set().union(lista[::3],lista[::5]))))
