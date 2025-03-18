#19-----------------------------------------------------------------------------------------------------------------
num = int(input("Ingrese un numero:  "))

for n in range(2,num):
    if num % n==0:
        print("no es primo")
        break
else:
    print("es primo")


