from os import system
import random
system('cls')

#print(random.randint(0,10)):

num = random.randint(0,100)

#o numero escolhido é par ou impar?:

resto = num % 2
if resto ==0:
    print('o numero escolhido é o par')
else:
    print('o numero escolhido é impar')    

#o numero escolhido é maior que 50 ou menor
# (mais perto do 100 ou do 0)

if num > 50:
    print('o numero escolhido esta mais perto de 100')
else:
    print('o numero escolhido está mais perto de 0')    

#o numero escolhido é primo







