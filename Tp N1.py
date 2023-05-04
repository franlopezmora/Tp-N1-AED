print('Trabajo Práctico 01: Gestión de Cabinas de Peaje.')
print()

pais = int(input("Ingrese el pais de la cabina atravesada, Argentina(0), Bolivia(1), Brasil(2), Paraguay(3), "
                 "Uruguay(4): "))

patente = input('Ingrese le numero de patente: ')
pais_del_vehiculo = None

importe_urug_para_arg = 300
importe_brasil = 400
importe_bolivia = 200
pago = None

promedio = None

print()
print("*" * 150)
print()

if len(patente) != 7:
    pais_del_vehiculo = "Desconocida"
else:
    if (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (48 <= ord(patente[2]) <= 57) and \
            (48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[4]) <= 57) and (65 <= ord(patente[5]) <= 90) and \
            (65 <= ord(patente[6]) <= 90):
        pais_del_vehiculo = 'Argentina'

    elif (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (48 <= ord(patente[2]) <= 57) and \
            (48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[4]) <= 57) and (48 <= ord(patente[5]) <= 57) and \
            (48 <= ord(patente[6]) <= 57):
        pais_del_vehiculo = 'Boliviana'

    elif (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (65 <= ord(patente[2]) <= 90) and \
            (48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[5]) <= 57) and (48 <= ord(patente[6]) <= 57) and \
            (65 <= ord(patente[4]) <= 90):
        pais_del_vehiculo = 'Brasileña'

    elif (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (65 <= ord(patente[2]) <= 90) and \
            (65 <= ord(patente[3]) <= 90) and (48 <= ord(patente[4]) <= 57) and (48 <= ord(patente[5]) <= 57) and \
            (48 <= ord(patente[6]) <= 57):
        pais_del_vehiculo = 'Paraguaya'

    elif (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (65 <= ord(patente[2]) <= 90) and \
            (48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[4]) <= 57) and (48 <= ord(patente[5]) <= 57) and \
            (48 <= ord(patente[6]) <= 57):
        pais_del_vehiculo = 'Uruguaya'
    else:
        pais_del_vehiculo = "Otro"

print("La patente es : ", pais_del_vehiculo)

print()
print("*" * 150)
print()

# SEGUNDA CONSIGNA

vehiculo = int(input("Ingrese el tipo de vehiculo, motocicleta(0), automovil(1), camion(2): "))

if (vehiculo != 0) and (vehiculo != 1) and (vehiculo != 2):
    print('OPCION INCORRECTA')
    quit()

else:
    if (pais != 0) and (pais != 1) and (pais != 2) and (pais != 3) and (pais != 4):
        print("El pais solo puede tomar valores entre 0-4")
        quit()
    else:
        if (pais == 3) or (pais == 0) or (pais == 4):
            if vehiculo == 0:
                descuento = (importe_urug_para_arg * 50) / 100
                pago = 300 - descuento

            elif vehiculo == 2:
                pago = importe_urug_para_arg * ((100 + 60) / 100)

            elif vehiculo == 1:
                pago = importe_urug_para_arg

        elif pais == 2:
            if vehiculo == 0:
                descuento = (importe_brasil * 50) / 100
                pago = 400 - descuento

            elif vehiculo == 2:
                pago = importe_brasil * ((100 + 60) / 100)

            elif vehiculo == 1:
                pago = importe_brasil

        elif pais == 1:
            if vehiculo == 0:
                descuento = (importe_bolivia * 50) / 100
                pago = 200 - descuento
            elif vehiculo == 2:
                pago = importe_bolivia * ((100 + 60) / 100)
            elif vehiculo == 1:
                pago = importe_bolivia

print()
print(150 * '*')
print()

# PARTE TRES
metodo_pago = int(input("Ingrese el metodo de pago, manual(1) o telepeaje (2): "))
pago_con_descuento = None

if (metodo_pago == 1) or (metodo_pago == 2):
    if metodo_pago == 1:
        pago_con_descuento = pago
    elif metodo_pago == 2:
        pago_con_descuento = (pago * 90) / 100
    print("El pago a realizar es: ", pago_con_descuento)
else:
    print("El metodo de pago solo puede ser 1 o 2")
    quit()

print()
print(150 * '*')
print()

# PARTE 4
distancia = float(input("Ingrese la distancia recorrida desde la ultima cabina: "))

if distancia < 0:
    print("La distancia no puede ser negativa")
    quit()
else:
    if distancia == 0:
        quit()
    elif pais == 0 or pais == 3 or pais == 4:
        promedio = distancia / pago_con_descuento
    elif pais == 1:
        promedio = distancia / pago_con_descuento
    elif pais == 2:
        promedio = distancia / pago_con_descuento

print("El valor promedio pagado por cada kilometro desde la ultima cabina es: ", round(promedio, 2))
