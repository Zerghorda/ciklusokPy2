def szambeker(szam1, szam2):
    if szam1 <= szam2:
        while szam1 < szam2:
            print(szam1)
            szam1 += 1
    if szam2 <= szam1:
        while szam2 < szam1:
            print(szam2)
            szam2 += 1
