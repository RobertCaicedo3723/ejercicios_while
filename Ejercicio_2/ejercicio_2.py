print()
print("-------------------------------------------------------------------")
print("----------------------------CENTNELA-------------------------------")
print("-----------------NUMEROS ENTEROS PARES E IMPARES-------------------")
print()

#Input

n = int(input("Ingrese un numero: "))

par = 0
impar = 0  



while n !=0:
    r = n % 2
    if r ==0:
        par = par + 1 
    else: 
        impar = impar + 1 
    n = int(input("Digite un numero "))

print("La canbtida de numeros pares es " ,par, "e impares es " , impar)