lista=['KM 0431/21', 'KM 0456/21', 'KM 0487/21', 'KM 0470/21', 'KM 0157/20', 'GKM0068/21',
       'KM 0476/21', 'KM 0476/21', 'KM 0472/21', 'KM 0481/21', 'KM 0485/21', 'KM 0490/21',
       'KM 0486/21', 'KM 0484/21', 'KM 0469/21', 'KM 0494/21', 'KM 0471/21', 'KM 0495/21',
       'KM 0491/21', 'KM 0492/21', 'KM 0489/21', 'GKM0076/21', 'KM 0496/21', 'KM 0474/21',
       'KM 0468/21', 'KM 0475/21', 'KM 0473/21', 'KM 0493/21', 'KM 0497/21', 'KM 0483/21',
       'KM 0424/21', 'KM 0419/21', 'KM 0425/21', 'KM 0426/21', 'KM 0230/21', 'KM 0234/21',
       'KM 0220/21', 'KM 0231/21', 'KM 0228/21', 'KM 0226/21', 'KM 0219/21', 'KM 0221/21',
       'KM 0233/21', 'KM 0238/21', 'KM 0223/21', 'KM 0420/21', 'KM 0422/21', 'KM 0232/21',
       'KM 0213/21', 'KM 0210/21', 'KM 0215/21', 'KM 0211/21', 'KM 0212/21', 'KM 0214/21',
       'KM 0209/21', 'KM 0421/21', 'KM 0225/21', 'KM 0222/21', 'KM 0236/21', 'KM 0235/21',
       'KM 0227/21', 'KM 0224/21', 'KM 0237/21', 'KM 0423/21', 'KM 0403/21', 'KM 0404/21',
       'KM 0867/19', 'KM 0288/20', 'KM 0400/21', 'KM 0847/19', 'KM 0392/21', 'KM 0406/21',
       'KM 0391/21', 'KM 0862/19', 'KM 0393/21', 'KM 0407/21', 'KM 0402/21', 'KM 0405/21',
       'KM 0748/19', 'KM 2817/18', 'KM 0388/21', 'KM 0410/21', 'KM 0370/21', 'KM 0401/21',
       'KM 0408/21', 'KM 0394/21', 'KM 0384/21', 'KM 0389/19', 'GKM0052/21', 'KM 0322/20']

def sortowanie_new(lista):
       lista_sort = []
       for i in lista:
              print ('i=',i)
              rok_int = (i[-2:])
              sygn_int = int(i[3:7])
              if not lista_sort:
                     lista_sort.append(i)
              else:
                     if (rok_int < (lista_sort[0][-2:]))\
                             or (rok_int == (lista_sort[0][-2:]) and sygn_int <= int(lista_sort[0][3:7])):
                            lista_sort.insert(0,i)
                     elif (rok_int > (lista_sort[-1][-2:]))\
                             or (rok_int == (lista_sort[-1][-2:]) and sygn_int >= int(lista_sort[-1][3:7])):
                            lista_sort.append(i)
                     else:
                            licznik=0
                            while rok_int> lista_sort[licznik][-2:] or (rok_int== lista_sort[licznik][-2:] and sygn_int>=int(lista_sort[licznik][3:7])):
                                   licznik+=1
                                   print ('dupa =',licznik)

                            lista_sort.insert(licznik,i)

              print (lista_sort)
              #print (len(lista))
              #print (len(lista_sort))


              #and sygn_int - int(lista_tmp[-1][3:7]) == 1:
sortowanie_new(lista)