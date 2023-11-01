#Írj programot, mely beolvas egy pozitív egész számot, és megmondja, hogy tökéletes szám-e! (A tökéletes számok azok, melyek osztóinak összege egyenlő a szám kétszeresével. Ilyen szám pl. a 6, mert 2*6 = 1 + 2 + 3 + 6.)


def feladat1():
    def tokeletes_szam(szam):
        return szam == sum(i for i in range(1, szam) if szam % i == 0)

    try:
        szam = int(input("Kérem, adjon meg egy pozitív egész számot: "))
        if szam > 0:
            if tokeletes_szam(szam):
                print(f"{szam} egy tökéletes szám!")
            else:
                print(f"{szam} nem egy tökéletes szám.")
        else:
            print("Hibás bemenet. Kérem, adjon meg egy pozitív egész számot.")
    except ValueError:
        print("Hibás bemenet. Kérem, adjon meg egy pozitív egész számot.")


#.	A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!


def feladat2():
    import math
    try:
        szam = float(input("Kérlek adj meg egy  számot"))
        if szam>=0:
            negyzetgyok = math.sqrt(szam)
            print(f"Az{szam} négyzetgyöke:{negyzetgyok} ")
        else:
            print("Hiba: negatív számból nem lehet gyököt vonni")
    except  ValueError:
        print("hibás bemenet  adjon meg egy másik számot")

#8.	Írj programot, ami kiírja a 10x10-es alapú szorzótáblát! 10-esével egymás alá! használj hozzá formázott kiiratást!
def feladat3():
    sor = 1
    while sor <= 10:
        oszlop = 1
        while oszlop <= 10:
            eredmeny = sor * oszlop
            print(f"{sor} * {oszlop} = {eredmeny}\t", end="")
            oszlop += 1
        print()  # Az új sorra lépéshez
        sor += 1

#Írj eljárást, mely paraméterében kap egy számot, majd összeadja a számjegyeket és kiírja a számjegyek összegét a képernyőre.
def feladat4(szam):
    osszeg = 0
    for szamjegy in str(szam):
        osszeg+= int(szamjegy)
        print(f"{szam} számjegyeinek összege: {osszeg}")



def feladat5():
    szam = int(input("Kérem, adjon meg egy [200, 920] intervallumban lévő egész számot: "))

    if 200 <= szam <= 920:
        elso_szamjegy = int(str(szam)[0])
        print(f"A megadott szám első számjegye: {elso_szamjegy}")
    else:
        print("Hibás bemenet. A szám nem felel meg az intervallumnak.")





