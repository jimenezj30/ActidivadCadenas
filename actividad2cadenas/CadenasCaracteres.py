#Actividad 1
#1
name = "luis"
age = 19
favouriteFood = "carne y pollo"
text = f"Hola! Mi nombre es {name}. Yo tengo {age} años, y mi comida favorita es {favouriteFood}"
print(text)

#2
FullName = "Luis Jimenez"
lengthUsuario = len(FullName.strip())
print(f"Hola, {FullName}! Tu nombre tienen {lengthUsuario} letras, excluyendo los espacios")

#3
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078
print( f"Las ventas de la empresa lactea aumentaron un {round(increaseSalesPercent,2)}% y los ingresos crecieron un {round(revenueGrowthPercent,2)}%")

#4
Titulo4 = "4 punto"
print(Titulo4.center(20, "_"))
secretMessage = "aS!Ir waQm VL!eDafrcnXin=gS .P,yytahgoln.!"
omitircaracteres = secretMessage [3:]
indicees = [0, 2, 4, 6, 7, 9, 11, 13, 15, 17, 19, 21, 23,25, 27,29, 31, 33, 35, 37, 39]

#crea mensaje a traves de los indices
omitircaracteres = ''.join(omitircaracteres[i] for i in indicees)
print(omitircaracteres)


#5
text = "El nombre 'Python' viene dado por la aficion de Van Rossum al grupo Monty Python"
palabra = text.split()
numero_palabras = len(palabra)
print(f"Numero de palabras de la frase: {numero_palabras}")

#6
word = "camila"
cambioletra =word.replace('a','e')
print(cambioletra)

#7
sentence = "la historia del lenguaje de programación Python"
palabras = sentence.split()
inversa = palabras[::-1]
sentence_invertir = " ".join(inversa)
print(sentence_invertir)



