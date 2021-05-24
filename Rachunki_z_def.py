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
    print(sortowanie(zam_na_10(lista_spraw(bydgoszcz)),"KMN"))
    print(zamiana_10_na_syg(sortowanie(zam_na_10(lista_spraw(bydgoszcz)),"KMN")))
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

def zam_na_10(lista):
    lista_10=[]
    for i in lista:
        if (i[0:3]) == rep[0] or (i[0:3]) == rep[2]:
            liczba_zer = 11 - len(i)
            liczba_zer_str = "0" * (liczba_zer)
            x = 4 - len(i)
            i = i[0:3] + liczba_zer_str + i[x:]
            lista_10.append(i)


        elif (i[0:3]) == rep[4]:
            liczba_zer = 11 - len(i)
            liczba_zer_str = "0" * (liczba_zer - 1)
            x = 4 - len(i)
            i = i[0:3] + liczba_zer_str + i[x - 1:]
            lista_10.append(i)
        else:
            print("Błąd nr 1 w zam_na_10")
    return lista_10

def sortowanie(lista,a): ## lista z 10 cyfrowymi sygnaturami do posortowania oraz repertorium (GKM, KMN, KM ,)
    tablica = [[0 for col in range(10000)] for row in range(30)]
    if a =="KM":
        a="KM "
    for i in lista:
        if (i[0:3]) == a:
            rok_int = int(i[-2:])
            syg_int = int(i[3:7])
            tablica[rok_int][syg_int] = i
        elif (i[0:3]) != a:
            continue
        else:
            print("Błąd nr 1 w sortowanie")

    for j in range(0, 30):
        while (0) in tablica[j]:
            tablica[j].remove(0)  ##usuwa z listy zagnieżdżonnej elementy [0]
    while ([]) in tablica:
        tablica.remove([])  ##usuwa puste listy zanieżdżone
    if len(tablica) >= 2:
        while len(tablica) != 1:
            tablica[0] = tablica[0] + tablica[1]  ##łączy listy zagnieżdżone (pozostają dwie listy zagnieżdżone)
            del tablica[1]  ## ksuje niepotrzebą listę zagnieżdżoną, pozostaje lista prosta

    if tablica !=[]:
       return tablica[0]
    else:
        return print ("Brak spraw z repretorium", a)

def zamiana_10_na_syg (lista):
    lista_syg=[]


    for i in (lista):
        rok_int = int(i[-2:])
        sygn_int = int(i[3:7])
        rok_str = str(rok_int)
        sygn_str = str(sygn_int)
        if (i[0:3])==rep[4]:
            i = i[0:3] + sygn_str + "/" + rok_str
        elif i[0:3]==rep[0] or rep[2]:
            i = i[0:3] + " " + sygn_str + "/" + rok_str
        lista_syg.append(i)
    return lista_syg






if __name__ == "__main__":
    main()