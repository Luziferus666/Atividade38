#Inicialize uma lista de 20 números inteiros. Armazene os números pares em uma lista PAR e os números ímpares em uma lista IMPAR. Imprima as listas PAR e IMPAR.
numeros = [int(input(f"Digite o número {i + 1}: ")) for i in range(20)]
par = [num for num in numeros if num % 2 == 0]
impar = [num for num in numeros if num % 2 != 0]
print("Lista PAR:", par)
print("Lista IMPAR:", impar)