#Faça um programa que pergunte em que turno você estuda? peça para
# digitar M - matutino/ V- vespertino / N - noturno e imprima a mensagem''bom dia'', ''boa tarde'', '' boa noite''.

turno = input('Qual turno você estuda? M - matutino/ V- vespertino / N - noturno ')
if turno.lower() == 'm':
    print('bom dia')
elif turno.lower()=='v':
    print('boa tarde')
elif turno.lower()=='n':
    print('boa tarde')
else: 
    print('turno não existe')

        


