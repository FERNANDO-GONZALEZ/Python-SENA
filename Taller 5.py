#TALLER 5 PYTHON
# AUTOR (A) : Luis Fernando González
# FECHA: 12 de agosto de 2022
from datetime import date
hoy = date.today()
print ("Hoy ca el dia: ", hoy)
print ()
print("TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA FOR")
print ()
num1=int (input ("digite el primer numero: "))
num2=int (input ("digite el segundo numero (mayor): "))
print ("ciclo para el primer numero")
for i in range (num1):
    print (i)
print('fin del ciclo')

print ()
print ("ciclo desde el primer numero hasta el segundo numero")
for i in range (num1, num2):
    print(i)
print('fin del ciclo')
print ()

print("ciclo desde el primero hasta el segundo numero con incrementos de 2")
for i in range (num1, num2, 2):
    print (i)
print ('fin del Ciclo')
print ()

empresa=input("digite nombre de una emprepa: ")
empresa = empresa.lower()
for character in empresa:
    print (character)
print("Fin del ciclo")
print ()
print("FIN")