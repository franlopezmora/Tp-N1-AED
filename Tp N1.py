print('Trabajo Práctico 01: Gestión de Cabinas de Peaje.')

patente = input('ingrese le numero de patente:')
pais_del_vehiculo = None

vehiculo = int(input("Ingrese el tipo de vehiculo (motocicleta, automovil o camion) desde 0-2, respectivamente: "))

importe_urug_para_arg = 300
importe_brasil = 400
importe_bolivia = 200
pago = None

metodo_pago = int(input("Ingrese el metodo de pago, manual(1) o telepeaje (2): "))
pago_con_descuento = None

pais = int(input("Ingrese el pais de la cabina atravesada, Argentina(0), Bolivia(1), Brasil(2), Paraguay(3), "
                 "Uruguay(4): "))

distancia = float(input("Ingrese la distancia recorrida desde la ultima cabina: "))
promedio = None

if len(patente) == 7:
    if (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (48 <= ord(patente[2]) <= 57) and (
            48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[4]) <= 57) and (65 <= ord(patente[5]) <= 90) and (
            65 <= ord(patente[6]) <= 90) \
            or (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (48 <= ord(patente[2]) <= 57) and (
            48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[4]) <= 57) and (48 <= ord(patente[5]) <= 57) and (
            48 <= ord(patente[6]) <= 57) \
            or (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (65 <= ord(patente[2]) <= 90) and (
            48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[5]) <= 57) and (48 <= ord(patente[6]) <= 57) and (
            65 <= ord(patente[4]) <= 90) \
            or (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (65 <= ord(patente[2]) <= 90) and (
            65 <= ord(patente[3]) <= 90) and (48 <= ord(patente[4]) <= 57) and (48 <= ord(patente[5]) <= 57) and (
            48 <= ord(patente[6]) <= 57) \
            or (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (65 <= ord(patente[2]) <= 90) and (
            48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[4]) <= 57) and (48 <= ord(patente[5]) <= 57) and (
            48 <= ord(patente[6]) <= 57):
        print("La patente pertenece a uno de los 5 paises analizados")
    else:
        print("La patente no pertenece a uno de los 5 paises analizados")
        quit()
else:
    print("La patente ingresada no es valida")
    quit()

if (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (48 <= ord(patente[2]) <= 57) and (
        48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[4]) <= 57) and (65 <= ord(patente[5]) <= 90) and (
        65 <= ord(patente[6]) <= 90):
    pais_del_vehiculo = 'Argentina'

if (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (48 <= ord(patente[2]) <= 57) and (
        48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[4]) <= 57) and (48 <= ord(patente[5]) <= 57) and (
        48 <= ord(patente[6]) <= 57):
    pais_del_vehiculo = 'Bolivia'

if (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (65 <= ord(patente[2]) <= 90) and (
        48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[5]) <= 57) and (48 <= ord(patente[6]) <= 57) and (
        65 <= ord(patente[4]) <= 90):
    pais_del_vehiculo = 'Brasil'

if (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (65 <= ord(patente[2]) <= 90) and (
        65 <= ord(patente[3]) <= 90) and (48 <= ord(patente[4]) <= 57) and (48 <= ord(patente[5]) <= 57) and (
        48 <= ord(patente[6]) <= 57):
    pais_del_vehiculo = 'Paraguay'

if (65 <= ord(patente[0]) <= 90) and (65 <= ord(patente[1]) <= 90) and (65 <= ord(patente[2]) <= 90) and (
        48 <= ord(patente[3]) <= 57) and (48 <= ord(patente[4]) <= 57) and (48 <= ord(patente[5]) <= 57) and (
        48 <= ord(patente[6]) <= 57):
    pais_del_vehiculo = 'Uruguay'

print("La patente es de: ", pais_del_vehiculo)

print("*" * 64)

# SEGUNDA CONSIGNA

if vehiculo == 0 or vehiculo == 1 or vehiculo == 2:
    if (pais_del_vehiculo == 'Argentina') or (pais_del_vehiculo == 'Paraguay') or (pais_del_vehiculo == 'Uruguay'):
        if vehiculo == 0:
            descuento = (importe_urug_para_arg * 50) / 100
            pago = 300 - descuento

        if vehiculo == 2:
            pago = importe_urug_para_arg * ((100 + 60) / 100)

        if vehiculo == 1:
            pago = importe_urug_para_arg

    if pais_del_vehiculo == 'Brasil':
        if vehiculo == 0:
            descuento = (importe_brasil * 50) / 100
            pago = 400 - descuento

        if vehiculo == 2:
            pago = importe_brasil * ((100 + 60) / 100)

        if vehiculo == 1:
            pago = importe_brasil

    if pais_del_vehiculo == 'Bolivia':
        if vehiculo == 0:
            descuento = (importe_bolivia * 50) / 100
            pago = 200 - descuento
        if vehiculo == 2:
            pago = importe_bolivia * ((100 + 60) / 100)
        if vehiculo == 1:
            pago = importe_bolivia

else:
    print('OPCION INCORRECTA')
    quit()

print(64 * '*')

# PARTE TRES

if (metodo_pago == 1) or (metodo_pago == 2):
    if metodo_pago == 1:
        pago_con_descuento = pago
        print("El precio a pagar es: ", pago_con_descuento)
    if metodo_pago == 2:
        pago_con_descuento = pago * 0.9

    print("El pago a realizar es: ", pago_con_descuento)
else:
    print("El metodo de pago solo puede ser 1 o 2")
    quit()

# PARTE 4

if pais == 0 or pais == 3 or pais == 4:
    promedio = distancia/importe_urug_para_arg
if pais == 1:
    promedio = distancia/importe_bolivia
if pais == 2:
    promedio = distancia/importe_brasil

print("El valor promedio pagado por cada kilometro desde la ultima cabina es: ", round(promedio, 2))
