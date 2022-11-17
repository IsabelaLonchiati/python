num1 = input('informe o valor 1:')
divisor = input('informe valor div:')


if num1.isalpha():
    print('não é um numero')

if num1.isdecimal():
    print('é um numero:')

if int(divisor) > 0:
    print('posso dividir')
    divisão = int(num1) / int(divisor)
    print(f'resultado da divisão é {divisão}')
else:
    print('valor 0, não pode ser dividido')
