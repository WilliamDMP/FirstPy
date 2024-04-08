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