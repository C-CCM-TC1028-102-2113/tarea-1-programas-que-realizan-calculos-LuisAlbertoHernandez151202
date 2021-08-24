def main():
    #escribe tu código abajo de esta línea
    #Leer los datos
    pass
mensaje=int(input("Dame el número de mensajes:"))
megas=float(input("Dame el número de megas:"))
minutos=(input("Dame el número de minutos:"))
mens=mensaje*.80
meg=megas*.80
min=minutos*.80
total=mens+meg+min
total=round(total,2)
print(El costo total del mes es:"+srt(total))
      


if __name__ == '__main__':
    main()
