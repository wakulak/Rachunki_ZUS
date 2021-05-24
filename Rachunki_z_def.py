from openpyxl import load_workbook

wb = load_workbook('rachunki.xlsx')
sheet = wb.active
cena=37.79

rep=("GKM","GKM ","KMN","KMN ","KM ","KM ")

bydgoszcz=("Bydgoszcz","92 10205590 0000 0302 9040 0010","0010")
koszalin=("Koszalin","90 10205590 0000 0502 9130 0011", "0011")
jaslo=("Jasło","73 10205590 0000 0302 9110 0013", "0013")
zielona=("Zielona Góra", "66 10205590 0000 0602 9420 0015", "0015")
elblag=("Elbląg","69 10205590 0000 0202 9080 0016", "0016")
czestochowa=("Częstochowa","12 10205590 0000 0102 9070 0017","0017")
chrzanow=("Chrzanów","52 10205590 0000 0002 9060 0018", "0018")
radom=("Radom", "33 10205590 0000 0602 9270 0019", "0019")


def main():
    print ("TEST")
    print(lista_spraw(bydgoszcz))
    print(zam_na_10(lista_spraw(bydgoszcz)))
    print(sortowanie(zam_na_10(lista_spraw(bydgoszcz))))
    print ("Koniec testu")




def lista_spraw(miasto):
    wiersz=1
    lista_all=[]
    for row in sheet.iter_rows(min_row=2, min_col=3, max_col=3):
        wiersz += 1
        for cell in row:
            if cell.value[57:61] == miasto[2]:
                lista_all.append(sheet.cell(row=wiersz, column=1).value)
            else:
                break
    return lista_all

def zam_na_10(lista,):
    lista_10=[]
    for i in lista:
        if (i[0:3]) == rep[0]:
            liczba_zer = 11 - len(i)
            liczba_zer_str = ("0") * (liczba_zer)
            x = 4 - len(i)
            i = i[0:3] + liczba_zer_str + i[x:]
            lista_10.append(i)


        elif (i[0:3]) == rep[4]:
            liczba_zer = 11 - len(i)
            liczba_zer_str = ("0") * (liczba_zer - 1)
            x = 4 - len(i)
            i = i[0:3] + liczba_zer_str + i[x - 1:]
            lista_10.append(i)
        else:
            print("Błąd nr 1 w zam_na_10")
    return lista_10

def sortowanie(lista): ## teraz tutaj
    lista_GKM = [[0 for col in range(10000)] for row in range(30)]
    lista_KMN = [[0 for col in range(10000)] for row in range(30)]
    lista_KM = [[0 for col in range(10000)] for row in range(30)]


    for i in lista:
        print(i[0:3])
        print(rep[4])
        if (i[0:3]) == rep[4]:
            rok_int = int(i[-2:])
            print(rok_int)
            sygn_int = int(i[3:7])
            print(sygn_int)
            rok_str = str(rok_int)
            sygn_str = str(sygn_int)
            i = rep[1] + sygn_str + "/" + rok_str
            print (i)
            lista_KM[rok_int][sygn_int] = i

        else:
            print("Błąd nr 1 w sortowanie")
    print (lista_KM[rok_int][sygn_int])





if __name__ == "__main__":
    main()