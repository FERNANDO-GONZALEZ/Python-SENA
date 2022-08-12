#TALLER 6 PYTHON
# AUTOR (A) : XXXXXX
# FECHA:
from datetime import date
hoy=date.today()
print ("Hoy es el dia: ", hoy)
print ()
print ("TALLER 6 CICLOS ITERATIVOS CON LA SENTENCIA WHILE")
print ()
numl=int (input ("digite un numero: "))
print ("***Ciclo controlado por contador")
i = 1
while i <= numl:
    print (i)
    i += 1
print ('fin del ciclo')

print ()
print("Ciclo controlado por evento")
i=1
numero1= 5
numero2= int (input ("Digite un numero de 1 a 10: "))
while numero2 != numero1:
    i += 1
    numero2 = int (input ("Digite un numero de 1 a 10: "))
print ("Acertaste en el intento No.", i)
print('fin del ciclo')

print()
print("***Ciclo abortado en la sentencia break")
amistad=input("Digite el nombre de la amistad: ")
amistad=amistad.upper()
for character in amistad:
    print(character)
    if character=="A":
        break
    print("Fin del ciclo")
    print()
    print("FIN")
