from math import sqrt, ceil
def primos(num):
        raiz = sqrt(num)
        raiz = ceil(raiz)
        i = 3
        while i <= raiz + 3:
                if i == 3:
                        if(num%2 == 0 and num != 2):
                                break
                if ((num%i == 0 and num!=i)or(num==1)):
                        break
                elif i >= raiz:
                        return num
                        break
                elif num == 0:
                        break
                i += 2
print("Esse programa tem o intuito de imprimir N primos")
N = int(input("Informe quantos primos você deseja: "))
cont = 0
num = 1
while True:
        a = (primos(num))
        num += 1
        if a is not None:
                print(a,end=" ")
                cont += 1
        if cont == N:
                break
print()