#14----------------------------------------------------------------------------------------------------------------
animals= ["leon","Tigre","Jaguar"]
for animal in animals:
    print(animal)
#a)
for animal in animals:
    print(f"un {animal} seria una gran mascota")
#b)
animal2= input("ingresa otro animal:  ")
animals.append(animal2)
print("Todos estos animales seran una gran mascota")
print(animals)