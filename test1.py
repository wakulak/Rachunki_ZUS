lista_IN=['GKM 1/21', 'GKM 22/21', 'GKM 123/21', 'GKM 9999/18','KM 1/21', 'KMN 1/21', 'GKM 29/21', 'GKM 38/21', 'GKM 39/20', 'GKM 59/20',
               'GKM 70/21', 'GKM 77/20', 'KMN 100/18', 'KMN 23/19', 'GKM 134/20', 'GKM 1111/19',
               'KMN 1234/21','GKM 84/20', 'GKM 91/20', 'GKM 94/20', 'KM 1169/19', 'KM 131/21', 'KM 132/21',
               'KM 133/21', 'KM 138/21', 'KM 152/21', 'KM 161/21', 'KM 174/21', 'KM 206/21',
               'KM 207/21', 'KM 208/21', 'KM 216/21', 'KM 217/21', 'KM 218/21', 'KM 231/18',
               'KM 27/21', 'KM 282/21', 'KM 378/21', 'KM 38/20', 'KM 390/21', 'KM 414/21',
               'KM 430/20', 'KM 444/21', 'KM 459/20', 'KM 460/20', 'KM 461/20', 'KM 462/20',
               'KM 467/20', 'KM 468/20', 'KM 469/20', 'KM 470/20', 'KM 472/20', 'KM 476/20',
               'KM 498/21', 'KM 515/20', 'KM 517/20', 'KM 52/20', 'KM 526/20', 'KM 538/20',
               'KM 574/20', 'KM 575/20', 'KM 576/20', 'KM 577/20', 'KM 599/20', 'KM 600/20',
               'KM 608/20', 'KM 62/21', 'KM 63/21', 'KM 66/20', 'KM 864/19', 'KM 891/19', 'KM 92/21']


lista_GKM=[[0 for col in range(10000)] for row in range(30)]
lista_KMN=[[0 for col in range(10000)] for row in range(30)]
lista_KM=[[0 for col in range(10000)] for row in range(30)]


GKM=("GKM","GKM ")
KMN=("KMN", "KMN ")
KM=("KM ", "KM ")



def sortowanie(lista_IN,rep,rep1,rep2,lista, lista1, lista2):

    def sortowanie_(i,rep,lista):
        if (i[0:3])==rep[0]:
            rok_int=int (i[-2:])                
            sygn_int=int(i[3:7])              
            rok_str=str(rok_int)              
            sygn_str=str(sygn_int)              
            i=rep[1]+sygn_str+"/"+rok_str               
            lista[rok_int][sygn_int]=i
            #print (lista[rok_int][sygn_int],)
        else:
            print ("Błąd 1")

    def usuwanie_0 (lista):
        for j in range(0,30):
            while (0) in lista[j]:
                lista[j].remove(0)
        while ([]) in lista:
            lista.remove([])
        while len(lista)!=2:
            lista[0]=lista[0]+lista[1]
            del lista[1]
        lista=lista[0]+lista[1]
        x=", ".join(lista)
        print ("\n",x)

               
                    
        

    for i in lista_IN:
        if(i[0:3])==rep[0] or (i[0:3])==rep1[0]:
            liczba_zer=11-len(i)
            liczba_zer_str=("0")*liczba_zer
            x=4-len(i)
            i=i[0:3]+liczba_zer_str+i[x:]
            #print (i)
            if(i[0:3])==rep[0]:
                sortowanie_(i,rep,lista)
            elif(i[0:3])==rep1[0]:
                sortowanie_(i,rep1,lista1)
            else:
                print ("Błąd 2")
            
        elif(i[0:3])==rep2[0]:
            liczba_zer=11-len(i)
            liczba_zer_str=("0")*(liczba_zer-1)
            x=4-len(i)
            i=i[0:3]+liczba_zer_str+i[x-1:]
            #print (i)
            sortowanie_(i,rep2,lista2)

        else:
            print ("Błąd 3")
    usuwanie_0(lista)
    usuwanie_0(lista1)
    usuwanie_0(lista2)
        

    
         
    
sortowanie (lista_IN, GKM, KMN, KM,lista_GKM, lista_KMN, lista_KM)


