#13--------------------------------------------------------------------------------------------------------------
pizzas = ["Peperoni","hawaiana","mexicana"]
#a)
for pizza in pizzas:
    print(f"Me gusta la pizza de {pizza}")
#b)
new_pizza = input("ingresa otra pizza:  ")
pizzas.append(new_pizza)
print("me gusta la pizza")
print(pizzas)