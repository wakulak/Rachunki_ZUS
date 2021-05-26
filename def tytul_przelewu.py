lista_testowa = ['GKM0001/19', 'GKM0005/20', 'GKM0007/20', 'GKM0008/20', 'GKM0009/20',
                 'GKM8596/21', 'GKM0023/20', 'GKM0024/20', 'GKM0025/20',]

# później jeszcze trzeba zrobić żeby sprawy z takimi sygnaturami zapisywał jako GKM 9/21x2, GKM 456/19 x 3
def tytul_przelewu(lista):
    sygn_model = "XXX0000/00"
    lista_przel = []
    lista_temp = []
    a = ""
    lista.append('GKM9999/99')
    for i in lista:
        rok_int = int(i[-2:])
        sygn_int = int(i[3:7])
        rok_str = str(rok_int)
        sygn_str = str(sygn_int)
        print("Test f tytul_przelewu")
        if not lista_przel:
            if not lista_temp:
                sygn_model=i
                i = i[0:3] + " " + sygn_str + "/" + rok_str
                lista_przel.append(i)
                i = i[0:3] + " " + sygn_str + "-"
                lista_temp.append(i)
                print(lista_temp)
                print(lista_przel)
            else:
                ("Bład nr 1")
        elif rok_int == int(sygn_model[-2:]) and sygn_int - int(sygn_model[3:7]) == 1:
            sygn_model=i

            lista_przel[-1]=lista_temp[0]
            i = sygn_str + "/" + rok_str
            lista_temp.append(i)


            print(lista_temp)
            print(lista_przel)
        else:
            sygn_model = i
            i = i[0:3] + " " + sygn_str + "/" + rok_str
            lista_przel.append(i)
            lista_temp.clear()
            i = i[0:3] + " " + sygn_str + "-"
            lista_temp.append(i)



            print (lista_temp)
            print (lista_przel)





        # lista_przel.append(i)
        # lista_temp.append(i)
        # if rok_int == int(sygn_model[-2:]) and sygn_int - int(sygn_model[3:7]) == 1:
        #     if not lista_temp:
        #         lista_temp.
        #
        #         lista_temp.append(i)
        #
        # if rok_int == int(sygn_model[-2:]) and sygn_int - int(sygn_model[3:7]) == 1:
        #     lista_temp.append(i)
        #
        #     print("Warunek = true")
        #     lista_temp.append(i)
        #     print(lista_temp)
        #     a = i
        #     i = i[0:3] + " " + str(
        #         int(sygn_model[3:7])) + "-" + sygn_str + "/" + rok_str  # nie działa jeżeli są więcej niż
        #     # dwie sąsiadujące sygnatury - wpisuje tylko dwie ostatnie
        #     # a wcześniejsze nie są dodawna do listy
        #     lista_przel[-1] = i
        #     print(i)
        # else:
        #     if (i[0:3]) == rep[4]:
        #         a = i
        #         i = i[0:3] + sygn_str + "/" + rok_str
        #         lista_przel.append(i)
        #     elif i[0:3] == rep[0] or rep[2]:
        #         a = i
        #         i = i[0:3] + " " + sygn_str + "/" + rok_str
        #         lista_przel.append(i)
        # sygn_model = a
        # print(lista_przel)



tytul_przelewu(lista_testowa)