def main():
    #escribe tu código abajo de esta línea
import math
palabras=int(input("Dame el número de palabras:"))
pagi=(math.ceil(palabras/475))
total=pagi*50
descuento=total*.10
totalN=total-descuento
totalN=round(totalN,1)
print("El costo de la publicación es:"str(totalN))
pass
if __name__ == '__main__':
    main()
