#16----------------------------------------------------------------------------------------------------------------
num_factorial=int(input("ingrese un numero:  "))
factorial = 1
for i in range(1, num_factorial +1):
    factorial*=i
print(factorial)