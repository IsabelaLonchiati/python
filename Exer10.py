#Vamos trabalhar com dados de texto, usando varios metodos para verificar e modificar o valor de uma variavel de clss str

from os import system 
system('cls')
nomecompleto = input('informe seu nome completo')



#tamanho da minha string / total de caracteres

print('1. total de caracteres:', len(nomecompleto))

#acessando um caractere a partir da posição
print('2. o caractere da posição 2 é: ', (nomecompleto[2]))

#transformar string em maiuscula / minuscula
print('3. texto em maiuscula' , nomecompleto.upper())
print('3. texto em minuscula' , nomecompleto.lower())
print('3. texto em maiuscula' , nomecompleto.capitalize())

#procurar a posição de um determinado caractere , aqui procurou o espaço entre o nome
print('6. posição do caractere espaço: ' , nomecompleto. find(' '))

#fatiar uma string ate uma determinada posição, vai trazer somente até o ponto que ele contou, o espaço
espaco = nomecompleto.find(' ')
print('somente o primeiro nome:' , nomecompleto [0:espaco])

# substituir um caractere por outro, junta os espaços. trocou espaço por vazio.

print('nome sem espaço: ', nomecompleto.replace(' ' , ''))

# verificar somente letras e numeros, se ele é alfa ou alfanumericos

print('9. tem somente letras? ', nomecompleto.replace(' ', ''). isalpha())
print('10. é alfanumerico? ', nomecompleto.replace(' ','').isalnum())

#quebrar o texto em partes especificas retornando array, separa todas as palavras da lista

print('11. quebrar o texto a cada espaço em branco:' , nomecompleto.split(' '))

#centralizar o texto cruzando * para completar as laterais

print(' 12. centralizar o texto entre * ',)
print(nomecompleto.center(80,'*'))