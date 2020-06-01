#calcular o fatorial do numero digitado

numero = int(input('digite um numero'))
fatorial = numero
contador = 1

while (numero-contador)>1:
    fatorial = fatorial * (numero-contador)
    contador = contador + 1 # ou assim contador +=1
print ('{0}! = {1}'.format(numero,fatorial)) #0 é o valor q o usuario digitou e 1 é o resultado do fatorial
