#PROGRAMA PARA CALCULAR EL VALOR A PAGAR DE UN RESTAURANTE X

while True:
    total_pagar = input("Ingrese el valor a pagar")
    try:
        total_pagar=float(total_pagar)
        if total_pagar>=0:
            break
        else:
            print("No se permiten valores menores que cero, por favor ingrese un número mayor que cero")

    except KeyboardInterrupt:
        break
    except ValueError as e:
        print("El valor que ingresaste no es un numero, por favor ingresa el total a pagar: ",e)
        if total_pagar == '':
            break
    
while True:
    personas = input("Entre cuántas personas se dividirá la cuenta")
    try:
        personas=float(personas)
        if personas>=0:
            break
        else:
            print("No se permiten valores menores que cero, por favor ingrese un número mayor que cero")
    except KeyboardInterrupt:
        break
    except ValueError as e:
        print("El valor que ingresaste no es ún numero, por favor ingresa entre cuántas personas se dividirá la cuenta : ",e)
        if personas == '':
            break

while True:
    propina = input("Indique el porcentaje de propina a incluir. Nota: Por favor ingrese un numero de 0-100")
    try:
        propina=float(propina)
        if propina>=0:
            break
        else:
            print("No se permiten valores menores que cero, por favor ingrese un número mayor que cero")
    except KeyboardInterrupt:
        break
    except ValueError as e:
        print("El valor que ingresaste no es un número, por favor ingresa un número de 0-100 : ",e)
        if propina == '':
            break

while True:
    impuestos = input("Indique el porcentaje de impuestos. Nota: Por favor ingrese un número de 0-100")
    try:
        impuestos=float(impuestos)
        if impuestos>=0:
            break
        else:
            print("No se permiten valores menores que cero, por favor ingrese un número mayor que cero")
    except KeyboardInterrupt:
        break
    except ValueError as e:
        print("El valor que ingresaste no es un numero, por favor ingresa un numero de 0-100 : ",e)
        if impuestos == '':
            break

#CALCULOS

if impuestos ==0 and propina ==0:
    print("El valor a pagar es ", total_pagar)
    print("El valor a pagar por persona es: ", (total_pagar/personas))
elif impuestos ==0 and propina > 0:
    propina=propina/100
    print("El total a pagar es ", total_pagar + total_pagar*(propina+1))
    print("El valor a pagar por persona es: ", (total_pagar + total_pagar*(propina+1))/personas)
elif impuestos > 0 and propina ==0:
    impuestos=impuestos/100
    print("El valor a pagar es ", total_pagar + total_pagar*(impuestos+1))
    print("El valor a pagar por persona es: ", (total_pagar + total_pagar*(impuestos+1))/personas)
else:
    impuestos=impuestos/100
    propina=propina/100
    print("El valor a pagar es ", total_pagar + total_pagar*(impuestos+1)+total_pagar*(propina+1))
    print("El valor a pagar por persona es: ", (total_pagar + total_pagar*(impuestos+1)+total_pagar*(propina+1))/personas)