numero = int(input('pasame un numero: '))

cont = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        cont = cont + 1



cont = 0

if cont == 2:
    print('el numero: ', numero, ' es primo') 
else:
    print('el numero: ', numero, ' NO es primo') 

