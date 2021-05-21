

def fruta(contador):  
    print("\nIngrese el color de la fruta en el que estoy pensado ;)")
    color = input()
     
    if contador > 0:
        if color == "naranja":
            print("\nHas acertado!")
            print("Has ganado!")
        else: 
            print("\nTe has equivocado, vuelve a intentarlo.")
            contador -= 1
            fruta(contador)
    else:
        print("\nHas perdido, suerte la próxima!")

fruta(2)
