"""minta
(a stílus kialakítása nem része a feladatnak, de a sorszámok és betűjelek kiíratása igen):
I/A:
Autó  neve: Opel Corsa
Gyártási dátum: 2022

I/B:
Ez az Opel Corsa átlagos korú.
A.	Kérje be az alábbi adatokat a fenti mintának megfelelően:
Autó  neve és gyártás éve!  (2p)
B.	A program az adatbekérés után írasson ki egy szöveget az alábbiak alapján!
Amennyiben az autó gyártási éve ez évi, akkor írja ki, „friss gyártás”.
 Amennyiben 2000 előtt gyártották az autót, írja ki: „öreg autó”
Minden más esetben: „Átlagos korú”. (4p)
A mintának megfelelően jelenítette meg az eredményt, és kérte be az adatokat. (1p)
"""
def adatbeker():
    marka=input("Autó neve: ")
    gyartas=int(input("Gyártási dátuma: "))
    if gyartas>=2023:
        print("friss gyártás")
    elif gyartas <=2000:
        print("öreg autó")
    else:
        print("átlagos korú")
