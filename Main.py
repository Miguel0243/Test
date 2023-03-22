print("Hola Mundo")
# Tipos de variables
x = 2
print(x)
print(type("Soy un dato srt")) #Tipo srt
print(type(5)) #Tipo int
print(type(10.2)) #Tipo float
print(type(3+1j)) #Tipo complex
print (type(True)) #Tipo boolean

strvariable = "mi variable cadena de texto"
print(strvariable)

intvariable = 15
print(intvariable)

boolvariable = False
print(boolvariable)

#Concatenacion de variables en print
print(type(print(strvariable,intvariable,boolvariable))) #Tipo nonetype

#Variables en una sola linea
name, lastname, alias, age = "Miguel","Espinosa","Maiki",23
print("Mi nombre es: ",name,lastname,". Mi edad es: ",age,", y mi alias es: ",alias)

first_name = input ('What is your name?')
age = input("How old are you?")

print(first_name)
print(age)
