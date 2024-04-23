# El famoso "FIZZ BUZZ"
"""Escribe un programa que muestre por consola(con un print) los numeros de uno a 100 (ambos incluidos) y 
con un salto de linea entre cada impresion sustituyendo los siguientes:
- multiplos de 3 por la palabra fizz
- multiplos de 5 por la palabra buzz
- multiplos de tres y de 5 por la palabra fizzbuzz"""

def fizz_buzz ():
    lista = []
    for i in range (0, 101):
        lista.append(i)
    for i in range (0, len(lista)):
        if lista[i] % 3 == 0 and lista[i] % 5 == 0:
            lista[i] = "FIZZBUZZ"
        elif lista[i] % 3 == 0:
            lista[i] = "FIZZ"
        elif lista[i] % 5 == 0:
            lista[i] = "BUZZ"
        print(lista[i])
        
print(fizz_buzz())