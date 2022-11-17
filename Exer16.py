
import random 
num1 = random.randint(0,100)
num2 = random.randint(0,100)
num3 = random.randint(0,100)



if num1 > num2 and num1 > num3:
    print(f'{num1} é o maior')
elif num2 > num1  and num2 > num3:
    print(f'{num2} é o maior') 
else:
    print(f'{num3} é maior')       