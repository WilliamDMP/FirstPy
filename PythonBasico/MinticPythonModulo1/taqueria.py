


menu= {
        "BAJA TACO": 4.00,
        "BURRITO": 7.50,
        "BOWL": 8.50,
        "NACHOS": 11.00,
        "QUESADILLA": 8.50,
        "SUPER BURRITO": 9.50,  
        "TACO": 3.00,
        "TORTILLA SALAD": 8.00 
      }

valorOrden = 0
while True:
    try: 
        nombrePedido = input("Digite el pedido que desea: ")
    except EOFError:
        break
    nombrePedido = nombrePedido.upper()
    if nombrePedido in menu:
        valorOrden += menu[nombrePedido]
        print("El valor de su orden es", valorOrden)
    elif nombrePedido == "CONTROL-D":
        print("Adios")
        break
    else:
        print("Pedido no encontrado")
        
    
