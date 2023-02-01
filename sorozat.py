"""2. feladat:    összesen 14p szerezhető, a modul neve: sorozat.py
minta:
II/A, B, C:
           	23; 46; 10; 1; 6
II/D, E:
           	Az egyjegyűek száma : 2.
A szamok.txt tartalma:
II/F:
A fejek száma: 2.

A.	Írasson ki a konzolra kötőjellel (-) elválasztva 5 lottószámot véletlen számsorozat alapján a mintának megfelelően! (4p)
B.	A generált értékeket tárolja lista adatszerkezetben! (1p)
C.	A „;” jel csak az értékek között szerepeljen (a végén ne)! (2p)
D.	Írjon függvényt egyjegyuek_szama néven, amiben számolja meg, hogy hány olyan elem van, ami egyjegyű (1). A visszatérési érték legyen egy egész szám! (3p)
E.	A egyjegyuek _szama függvény eredményét írassa ki a mintának megfelelően a konzolra, amit konzol_kiir nevű metódusban fogalmazzon meg! (2p)
F.	A egyjegyuek _szama függvény eredményét írassa ki a mintának megfelelően a szamok.txt nevű fájlba, amit file_kiir nevű metódusban fogalmazzon meg! (2p)
"""
import random

lotto_lista=[]
def feldolgoz():
    i=0
    while i<5:
        lotto_lista.append(random.randint(1,55))
        i+=1
    print("-".join(str(szamok)for szamok in lotto_lista))
def egyjegyu():
    i=0
    egyjegyu_db=0
    while i < len(lotto_lista):
        if lotto_lista[i]<10 :
            egyjegyu_db+=1
        i+=1
    return egyjegyu_db
    konzol_kiir(egyjegyu_db)
    fajl_kiir(egyjegyu_db)

def konzol_kiir(egyjegyu_db):
    print(f"Az egyjegyűek száma : {egyjegyu_db} ")
def fajl_kiir(egyjegyu_db):
    fajlom=open("szamok.txt","w", encoding="utf-8")
    fajlom.write(f"Az egyjegyűek száma : {egyjegyu_db} ")
