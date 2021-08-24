def main():
    #escribe tu código abajo de esta línea
    mesanterior=float(input("Dame el saldo del mes anterior:"))
    ingreso=float(input("Dime tus ingresos:"))
    egreso=float(input("Dime tus egresos:"))
    cheque=float(input("Dame el número de cheques:"))
    chequeN=cheque*13
    total=(mesanterior(ingreso-egreso))-chequeN
    interes=total*.075
    totalN=total-interes
    print("El saldo final es:"+srt(total1))
    pass

if __name__ == '__main__':
    main()
