lista = [['GKM 9999/18'], ['GKM 1111/19'], ['GKM 39/20', 'GKM 59/20', 'GKM 77/20', 'GKM 84/20', 'GKM 91/20',
                                            'GKM 94/20', 'GKM 134/20'], ['GKM 1/21', 'GKM 22/21', 'GKM 29/21',
                                                                         'GKM 38/21', 'GKM 70/21', 'GKM 123/21']]
while len(lista)!=2:
    lista[0]=lista[0]+lista[1]
    del lista[1]
lista=lista[0]+lista[1]
print (lista)


