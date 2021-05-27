from openpyxl import load_workbook

wb = load_workbook('rachunki.xlsx')
sheet = wb.active

cena = 37.79

rep = ("GKM", "GKM ", "KMN", "KMN ", "KM ", "KM ")

bydgoszcz = ("Bydgoszcz", "92 10205590 0000 0302 9040 0010", "0010")
koszalin = ("Koszalin", "90 10205590 0000 0502 9130 0011", "0011")
jaslo = ("Jasło", "73 10205590 0000 0302 9110 0013", "0013")
zielona = ("Zielona Góra", "66 10205590 0000 0602 9420 0015", "0015")
elblag = ("Elbląg", "69 10205590 0000 0202 9080 0016", "0016")
czestochowa = ("Częstochowa", "12 10205590 0000 0102 9070 0017", "0017")
chrzanow = ("Chrzanów", "52 10205590 0000 0002 9060 0018", "0018")
radom = ("Radom", "33 10205590 0000 0602 9270 0019", "0019")


def main():

    zus(bydgoszcz)
    zus(koszalin)
    zus(jaslo)
    zus(zielona)
    zus(elblag)
    zus(czestochowa)
    zus(chrzanow)
    zus(radom)
    if suma_all() != 0:
        print("\nSuma wszystkich rachunków pobranych z pliku = %.2f złotych" % suma_all())
    else:
        print("\nBrak rachunków w pliku albo pliku nie można otworzyć")
    zamiana()
    wb.save("rachunki.xlsx")


def lista_spraw(miasto):  # Pobiera do lista_all wszyskie sprawy z pliku wystawione
    # przez wskazany ZUS w argumencie (miasto)
    wiersz = 1
    lista_all = []

    for row in sheet.iter_rows(min_row=2, min_col=3, max_col=3):
        wiersz += 1
        for cell in row:
            if cell.value[57:61] == miasto[2]:
                lista_all.append(sheet.cell(row=wiersz, column=1).value)
            else:
                break
    return lista_all


def zam_na_10(lista):  # Argument to lista_spraw(miasto), zwraca nieposegregowaną listę spraw z danego
    # ZUS-u, z sygnaturami w formacie np GKM0001/21, lub KM 0001/21
    lista_10 = []

    for i in lista:
        if (i[0:3]) == rep[0] or (i[0:3]) == rep[2]:
            liczba_zer = 11 - len(i)
            liczba_zer_str = "0" * liczba_zer
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


def sortowanie(lista, repertorium, ):  # Pierwszy argument (zam_na_10(lista_spraw(miasto))),
    # drugi argument to jedno z repertorium (GKM,KMN,KM, albo rep[0],rep[2],rep[4]),
    # wychodzi lista posegregowanych rosnąco spraw
    # wskazanego jako argument repertorium
    # format:  GKM0001/21, GKM0002/21
    tablica = [[0 for col in range(10000)] for row in range(30)]

    if repertorium == "KM":
        repertorium = "KM "
    for i in lista:
        if (i[0:3]) == repertorium:
            rok_int = int(i[-2:])
            syg_int = int(i[3:7])
            tablica[rok_int][syg_int] = i
        elif (i[0:3]) != repertorium:
            continue
        else:
            print("Błąd nr 1 w sortowanie")

    for j in range(0, 30):
        while 0 in tablica[j]:
            tablica[j].remove(0)  # usuwa z listy zagnieżdżonnej elementy [0]
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


def zamiana_10_na_syg(lista):  # Argument to lista
    # (sortowanie(zam_na_10(lista_spraw(miasto)),repertorium))
    # wyjście to posegregowana lista spraw z danego repertorium i danego ZUS-u
    # sygnarury spraw w formacie GKM 1/21, GKM 1999/18, KM 1/19, KMN 123/20
    lista_syg = []

    for i in lista:
        rok_int = int(i[-2:])
        sygn_int = int(i[3:7])
        rok_str = str(rok_int)
        sygn_str = str(sygn_int)
        if (i[0:3]) == rep[4]:
            i = i[0:3] + sygn_str + "/" + rok_str
        elif i[0:3] == rep[0] or rep[2]:
            i = i[0:3] + " " + sygn_str + "/" + rok_str
        lista_syg.append(i)
    return lista_syg


def suma_miasto(miasto):  # Zwraca koszt wszystkich rachunków wystawionych przez wskazany jako argument ZUS
    licznik = 0
    suma = 0

    for row in sheet.iter_rows(min_row=2, min_col=3, max_col=3):
        for cell in row:
            if cell.value[57:61] == miasto[2]:
                licznik += 1
                suma = +licznik * cena
    return suma


def suma_all():  # Zwraca koszt wszystkich rachunków pobranych z pliku
    licznik = 0
    suma = 0

    for row in sheet.iter_rows(min_row=2, min_col=3, max_col=3):
        for cell in row:
            if cell.value[57:61] == bydgoszcz[2] or koszalin[2] or jaslo[2] or zielona[2]\
                    or elblag[2] or czestochowa[2] or chrzanow[2] or radom[2]:
                licznik += 1
                suma = +licznik * cena
    return suma


def zamiana():
    wiersz = 1

    for row in sheet.iter_rows(min_row=2, min_col=1, max_col=1):
        wiersz += 1
        for cell in row:
            if cell.value[0:3] == rep[0]:
                sheet.cell(row=wiersz, column=11).value = cell.value[4:]
                sheet.cell(row=wiersz, column=10).value = rep[0]
            elif cell.value[0:3] == rep[2]:
                sheet.cell(row=wiersz, column=11).value = cell.value[4:]
                sheet.cell(row=wiersz, column=10).value = rep[2]
            elif cell.value[0:3] == rep[4]:
                sheet.cell(row=wiersz, column=11).value = cell.value[3:]
                sheet.cell(row=wiersz, column=10).value = rep[4]
            else:
                print("\nBłąd nr 1 w def zamiana")


def zus(miasto):
    print("\nZus %s, nr rachunku: %s" % (miasto[0], miasto[1]))
    print("\nRachunki do spraw z repertorium %s:" % rep[0])
    if not (zamiana_10_na_syg(sortowanie(zam_na_10(lista_spraw(miasto)), rep[0]))):
        print("Brak rachunków")
    else:
        x = ", ".join((zamiana_10_na_syg(sortowanie(zam_na_10(lista_spraw(miasto)), rep[0]))))
        print(x)
    print("\nRachunki do spraw z repertorium %s:" % rep[4])
    if not (zamiana_10_na_syg(sortowanie(zam_na_10(lista_spraw(miasto)), rep[4]))):
        print("Brak rachunków")
    else:
        x = ", ".join((zamiana_10_na_syg(sortowanie(zam_na_10(lista_spraw(miasto)), rep[4]))))
        print(x)
    print("\nRachunki do spraw z repertorium %s:" % rep[2])
    if not (zamiana_10_na_syg(sortowanie(zam_na_10(lista_spraw(miasto)), rep[2]))):
        print("Brak rachunków")
    else:
        x = ", ".join((zamiana_10_na_syg(sortowanie(zam_na_10(lista_spraw(miasto)), rep[2]))))
        print(x)
    if suma_miasto(miasto) != 0:
        print("\nSuma rachunków z ZUS %s = %.2f złotych, tj. %i x %.2f zł" % (
            miasto[0], suma_miasto(miasto), suma_miasto(miasto) / cena, cena))
    print("\n-----------------------------------------------------------------------")

# usun ten komentarz
if __name__ == "__main__":
    main()
