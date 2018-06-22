numeros_ingresados = input()
lista = (list(numeros_ingresados.split(',')))
while '' in lista:    
    lista.remove('')
lista2 = list(map(int, lista))
print(lista2)