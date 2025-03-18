#17-----------------------------------------------------------------------------------------------------------------
palabra1 = input("Ingrese una palabra:  ")
palabra2 = input("ingresa otra palabra:  ")

if sorted(palabra1.lower()) == sorted(palabra2.lower()):
    print("Son anagrama")
else:
    print("no son anagrama")