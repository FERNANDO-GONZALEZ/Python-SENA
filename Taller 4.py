#TALLER 4 PYTHON
#AUTOR (A): Luis Fernando González
# FECHA: 12 de agosto de 2022
from datetime import date
hoy = date.today()
print ("Hoy es el dia: ", hoy)
print ()
print ("EJERCICIO DE LAS CLASES DE TRIANGULOS")
a=int (input ("digite el valor de A: "))
b=int (input ("digite el valor de B: "))
c=int (input ("digite el valor de C: "))
if a==b and a--c and b==c:
    print("EL TRIANGULO ES EQUILATERO")
else:    
    if a==b or b==c or a==c:
        print ("EL TRIANGULO ES ISOCELES")  
    else:
        print ("EL TRIANGULO ES ESCALENO")
print ()
animal=input ("digite un animal: ")
animal= animal.upper ()
if animal=="PERRO":
    print ("Este animal es el menor amigo del hombre:", animal)
if animal=="GATO":
    print ("Este animal persigue los ratones: ", animal)
if animal=="OSO":
    print ("Este animal vive en el polonorte: ", animal)
else:
   print ("No es PERRO,no es GATO, ni es OSO... es: ", animal)
print ()
print ("FIN")