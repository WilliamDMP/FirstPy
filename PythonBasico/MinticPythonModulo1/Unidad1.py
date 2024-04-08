#Variables

edad = 17
nombre = "William"

#Estructuras de control

if edad > 18:
    print(nombre, ",", "es mayor de edad")
else: 
    print(nombre, ",", "no es mayor de edad")
    
#Condición multiple

if edad > 18:
    print(nombre, ",", "es mayor de edad")
elif edad < 18:
    print("No puede entrar al bar")
else: 
    print(nombre, ",", "no es mayor de edad")
    
#While

contador = 1

while contador <= 5:
    print(contador)
    contador += 1
    
#for para iterar un elemento

frutas = ["manzana", "pera", "banano"]

for fruta in frutas:
    print(fruta)
    
#for para un rango numerico

for i in range(1, 6):
    print(i)
    
    


