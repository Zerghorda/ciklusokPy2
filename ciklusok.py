def szambeker(szam1, szam2):
    if szam1 <= szam2:
        while szam1 < szam2:
            if szam1 == szam2-1:
                print(f"{szam1:.0f}", end="")
            else:
                print(f"{szam1}", end=",")
            szam1 += 1
    if szam2 <= szam1:
        while szam2 < szam1:
            if szam2 == szam1-1:
                print(f"{szam2:.0f}", end="")
            else:
                print(f"{szam2:.0f}", end=",")
            szam2 += 1
    '''
    if szam1 == szam2:
       print("A számok meg egyeznek !")
       return 
    if szam1 > szam2:
        csere:float = szam1 
        szam1 = szam2
        szam2 = csere
           
    '''