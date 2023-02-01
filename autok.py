"""Az auto.txt forrásállomány, autók adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
Készítsen programot autom.py néven. Olvassa be auto.txt fájlból az auto adatait, tárolja Auto osztály típusú kocsi nevű listában a példányokat.
A megoldás mintája:
III/Flotta:
               Autók száma: 7.
III/Legfiatalabb
               A legfiatalabb autó: Seat Ibiza(2011))


A.	Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a auto.txt fájlból a autók adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
B.	Készíts függvényt flotta néven, amely visszaadja az autók számát a mintának megfelelően, majd írasd ki  a konzolra a mintának megfelelően! (2p)
C.	Add meg az legfiatalabb autó nevét a mintának megfelelően a konzolra írva!! (4p)
D.	Írassa ki konzolra a mintának megfelelően a legöregebb épület (ha több is van, akkor az első legöregebb adatait) országát. (4p)
"""
from Autoclass import  Auto
autok_lista=[]
def beolvas():
    fajlom=open("auto.txt","r", encoding="utf-8")
    fajlom.readline()
    fajltartalom=fajlom.readlines()
    i=0
    while i<len(fajltartalom):
        sor=fajltartalom[i].strip().split("$")
        autok_lista.append(Auto(sor))
        i+=1

def flotta():
    return len(autok_lista)
def legfiatalabb():
    i=0
    legfiatalabb_auto=0
    while i<len(autok_lista):
        if autok_lista[legfiatalabb_auto].ev > autok_lista[i].ev:
            legfiatalabb_auto=i
        i+=1
    print(f"A legfiatalabb autó: {autok_lista[legfiatalabb_auto]}")

def legoregebb():
    i=0
    legoregebb_auto=0
    while i < len(autok_lista):
        if autok_lista[legoregebb_auto].ev < autok_lista[i].ev:
            legoregebb_auto=i
        i+=1
    print(f"A legöregebb Autó: {autok_lista[legoregebb_auto]}")