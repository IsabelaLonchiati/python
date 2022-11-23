from os import system
system('cls')
titulo = 'calcular lista de compras'
print(titulo.center(60, '#'))

produtosdesc = []
produtospreco = []

numeroitens = int(input('informe o numero de itens desejados'))
for i in range(0,numeroitens):
    nomeproduto = input(f'nome do produto {i+1}: ')
    precoproduto = float(input(f'preco do {nomeproduto}'))
    produtosdesc.append(nomeproduto)
    produtospreco.append(precoproduto)
total = 0
for i in range(0,numeroitens):
    print(f'{produtosdesc[i]} - R${produtospreco[i]}')
    total += produtospreco[i]

print(f'total: R$ {total}')

print(produtosdesc) 
print(produtospreco)


