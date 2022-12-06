

import io
from Arquivos import tabCat
#importando a classe tabCat do arquivo denominado Arquivos.py
from Arquivos import tabProd

cat = tabCat() #instanciando o objeto da classe
prod = tabProd() #instanciando o objeto da classe

dicCategoria = cat.dicCat()#chamando a função/metodo do objeto
listadeprodutos = prod.listProd()#chamando a função/metodo do objeto

relatorio = open("relatorio.txt", mode="w", encoding='utf-8')
#open metodo que no modo 'w' ele edita escreve cria um arquivo
for item in dicCategoria:#percorrando(loop) no dicionario de categoria
    titulo = f'{dicCategoria[item][0]}\n{dicCategoria[item][1]}\n\nprodutos\n'

    prod = []
    #lista vazia paa armazenar todos os produtos por categoria
    for itemP in listadeprodutos:#percorrer a listaProdutos do arquivo
        if str(itemP[2]) == item:#compara a coluna 2 com o valor de item
            valor = f'{itemP[8]:.2f}' #pego valor e formato
            produto = '{:<60} | R$ {:>8}' . format(str(itemP[1].capitalize() + ' ' + itemP[3])[0:60],valor)
            #pego a descrição e embalagem e formato a frase
            prod.append(produto)
            #adiciona produto na lista prod
    prod.sort()   
    #ordeno a lista por ordem alfa numerica
    lista = ''
    i = 1
    #indice para ordem 'codigo' do relatorio
    for p in prod:#percorre a lista de produtos
        lista += '{:>4}. {}\n' . format(i,p)
        i +=1#incrementa mais 1 na posição do item no relatorio

    divisor = 'categoria' . center(80,'*')
    #divisor do relatorio
    relatorio.write(divisor + '\n' + titulo + lista +'\n\n')
    #escrever no artigo texto
categorias = ' total de categorias: {:>4}' . format(len(dicCategoria))   
produtos = 'total de produtos: {:>4}' . format(len(listadeprodutos))
resumo = 'resumo' .center(80, '*')
final = '{}\n\n{:>80}\n{:>80}' . format(resumo, categorias, produtos)
relatorio.write(final)
relatorio.close()


