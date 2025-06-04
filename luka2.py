# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=5665

### Operadores Aritméticos ###

# Operaciones con enteros
print(2 + 4)
print(2 - 4)
print(2 * 4)
print(2 / 4)
print(10 % 2)
print(10 // 2)
print(2 ** 2)
print(2 ** 2 + 2 - 7 / 1 // 4)

# Operaciones con cadenas de texto
print("Holi " + "Python " + "¿Qué tal?")
print("Holi " + str(5))

# Operaciones mixtas
print("Holi " * 5)
print("Holi " * (2 ** 2))

my_float = 2.5 * 2
print("Holi " * int(my_float))

### Operadores Comparativos ###

# Operaciones con enteros
print(2 > 4)
print(2 < 4)
print(2 >= 4)
print(4 <= 4)
print(2 == 4)
print(2 != 4)

# Operaciones con cadenas de texto
print("Holi" > "Python")
print("Holi" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Holi" <= "Python")
print("Holi" == "Holi")
print("Holi" != "Python")

### Operadores Lógicos ###

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(2 > 4 and "Holi" > "Python")
print(2 > 4 or "Holi" > "Python")
print(2 < 4 and "Holi" < "Python")
print(2 < 4 or "Holi" > "Python")
print(2 < 4 or ("Holi" > "Python" and 4 == 4))
print(not (2 > 4))
