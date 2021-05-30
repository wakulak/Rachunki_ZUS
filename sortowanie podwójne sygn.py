lista = ['KM 0570/21', 'KM 0585/21', 'KM 0674/21', 'KM 0560/21', 'KM 0516/21', 'KM 0559/21', 'KM 0561/21',
         'KM 0569/21', 'KM 0602/21', 'KM 0285/20', 'KM 0602/21', 'KM 0599/21', 'KM 0587/21', 'KM 0588/21',
         'KM 0534/21', 'GKM0094/21', 'KM 0389/21', 'KM 0179/21', 'KM 0180/21', 'KM 0178/21', 'GKM0022/21',
         'KM 0110/21', 'GKM0027/21', 'KM 0028/21', 'KM 0033/21', 'KM 0032/21', 'GKM0011/21', 'KM 0584/20',
         'KM 0011/21', 'KM 0497/20', 'KM 0360/20']


def sortowanie(lista, repertorium, ):  # Pierwszy argument (zam_na_10(lista_spraw(miasto))),
    # drugi argument to jedno z repertorium (GKM,KMN,KM, albo rep[0],rep[2],rep[5]),
    # wychodzi lista posegregowanych rosnąco spraw
    # wskazanego jako argument repertorium
    # format:  GKM0001/21, GKM0002/21
    tablica =[[0 for col in range(10000)] for row in range(30)]


    lista_duble=[]
    if repertorium == "KM":
        repertorium = "KM "
    for i in lista:
        if (i[0:3]) == repertorium:
            rok_int = int(i[-2:])
            syg_int = int(i[3:7])
            if not tablica[rok_int][syg_int]:
                tablica[rok_int][syg_int] = i
            else:
                lista_duble.append(i)
        elif (i[0:3]) != repertorium:
            continue
        else:
            print("Błąd nr 1 w sortowanie")

    for j in lista_duble: # dodawanie powielonych sygnatur do tablicy
        rok_int = int(j[-2:])
        tablica[rok_int].insert(tablica[rok_int].index(j), j)
        print (tablica[rok_int].index(j))


    for k in range(0, 30):
        while 0 in tablica[k]:
            tablica[k].remove(0)  # usuwa z listy zagnieżdżonnej elementy [0]
    while ([]) in tablica:
        tablica.remove([])  # usuwa puste listy zanieżdżone
    if len(tablica) >= 2:
        while len(tablica) != 1:
            tablica[0] = tablica[0] + tablica[1]  # łączy listy zagnieżdżone (pozostają dwie listy zagnieżdżone)
            del tablica[1]  # ksuje niepotrzebą listę zagnieżdżoną,
    if not tablica:
        return tablica
    else:
        return tablica[0]