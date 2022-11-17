# Faça um programa que receba 2 numeros e informe qual numero é o maior.


import random
num1 = int(input('Informe um numero '))
num2 = random.randint(0,100)

if num1  > num2:
    print(f'{num1} é maior que {num2}')
else:
    print(f'{num2} é maior que {num1}')