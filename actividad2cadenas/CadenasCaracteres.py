#Actividad 1
#declarar nombre, edad y comida favorita
name = "luis"
age = 19
favouriteFood = "carne y pollo"
text = f"Hola! Mi nombre es {name}. Yo tengo {age} años, y mi comida favorita es {favouriteFood}"
print(text)

#2 len sirve para contar las letras del nombre, .strip()
FullName = "Luis Jimenez"
lengthUsuario = len(FullName.strip())
print(f"Hola, {FullName}! Tu nombre tienen {lengthUsuario} letras, excluyendo los espacios")

#3 round sirve para redondear el resultado con su respectivo numero(2) al cual se quiere redondear
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078
print( f"Las ventas de la empresa lactea aumentaron un {round(increaseSalesPercent,2)}% y los ingresos crecieron un {round(revenueGrowthPercent,2)}%")

#4 modifiedMessage [:] omite el numero de carateres segun el numero y decodeMessage [::] lee el mensaje saltando de dos espacios en el texto
secretMessage = "aS!Ir waQm  VL!eDafrcnXi n=gS .P,yytahgoln.!"
modifiedMessage = secretMessage[3:]
decodedMessage = modifiedMessage[::2]
print(decodedMessage)

#5 split() separa el mensaje por palabras y len se encarga de contar las palabras
text = "El nombre 'Python' viene dado por la aficion de Van Rossum al grupo Monty Python"
palabra = text.split()
numero_palabras = len(palabra)
print(f"Numero de palabras de la frase: {numero_palabras}")

#6 wprd.replace(_old: 'letra', _new: 'letra')sirve para remplazar uun caracter por otro
word = "camila"
cambioletra =word.replace('a','e')
print(cambioletra)

#7 split separa las palabras y [::-1] " ".join(inversa) las invierte las palabras
sentence = "la historia del lenguaje de programación Python"
palabras = sentence.split()
inversa = palabras[::-1]
sentence_invertir = " ".join(inversa)
print(sentence_invertir)




