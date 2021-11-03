import random

numeros = "0123456789"
simbolos = "?+*#()[]{},;:.-/"
mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
minusculas = "abcdefghijklmnñopqrstuvwxyz"

numeros_boolean = input(" ¿Quiere que su contraseña contenga numeros ? Conteste si o no: ")
if numeros_boolean == "si":
    numeros_boolean = True
elif numeros_boolean == "no":
    numeros_boolean = False

simbolos_boolean = input(" ¿Quiere que su contraseña contenga simbolos ? Conteste si o no: ")
if simbolos_boolean == "si":
    simbolos_boolean = True
elif simbolos_boolean == "no":
    simbolos_boolean = False

mayusculas_boolean = input(" ¿Quiere que su contraseña contenga letras mayusculas ? Conteste si o no: ")
if mayusculas_boolean == "si":
    mayusculas_boolean = True
elif mayusculas_boolean == "no":
    mayusculas_boolean = False

minusculas_boolean = input(" ¿Quiere que su contraseña contenga letras minusculas ? Conteste si o no: ")
if minusculas_boolean == "si":
    minusculas_boolean = True
elif minusculas_boolean == "no":
    minusculas_boolean = False

contraseña = []
longitud_contraseña = int(input("Ingrese la longitud de la contraseña que quiere generar ")) + 1
contraseña_string = ""
numeros_decision = 0
simbolos_decision = 0
mayusculas_decision = 0
minusculas_decision = 0
if numeros_boolean == True:
    numeros_decision = 1
if simbolos_boolean == True:
    simbolos_decision = 2
if minusculas_boolean == True:
    minusculas_decision = 3
if mayusculas_boolean == True:
    mayusculas_decision = 4
while longitud_contraseña > 0:
    numero_random = random.randrange(1,5)
    if numero_random == numeros_decision:
        contraseña.append(random.choice(numeros))
        longitud_contraseña = longitud_contraseña - 1
    if numero_random == simbolos_decision:
        contraseña.append(random.choice(simbolos))
        longitud_contraseña = longitud_contraseña - 1
    if numero_random == mayusculas_decision:
        contraseña.append(random.choice(mayusculas))
        longitud_contraseña = longitud_contraseña - 1
    if numero_random == minusculas_decision:
        contraseña.append(random.choice(minusculas))
        longitud_contraseña = longitud_contraseña - 1
for x in range(len(contraseña)):
    contraseña_string = contraseña_string + (contraseña[x])

print(contraseña_string)
print(mayusculas[4])
