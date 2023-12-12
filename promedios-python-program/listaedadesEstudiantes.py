my_list = []

print("Ingrese las Edades de los 10 estudiantes, seguido de un enter cada edad: ")

for i in range(10):
    my_list.append(int(input()))

print("Desea saber la Edad mayor?: ")

print(max(my_list))

print("Desea saber la Edad menor?: ")

print(min(my_list))

print("Desea saber el promedio de Edad?: ")

print(sum(my_list) / 10)

print("Desea saber la mediana de las Edades?: ")

my_list.sort()

print(my_list[5])

print("La lista completa de Edades es: ")

print(my_list)
print("Gracias!!")
