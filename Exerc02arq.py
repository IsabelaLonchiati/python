from os import system
import os.path, datetime
system('cls')


arquivo = 'categorias.csv'#caminho do arquivo
categorias = open(arquivo,'r', encoding='utf-8')
#abre somente leitura o caminho do arquivo e armazena em uma variavel
dicCategorias = {} #instanciar uma varivel do tipo dicionario

if os.path.isfile(arquivo):
    for line in categorias:
        colunas = line.strip().split(';')
        #retira os aspectos e separa em lista as colunas
        dados =[colunas[1], colunas[2]]
        #armazena em dados uma lista com os valores de coluna 1 e 2
        dicCategorias[colunas[0]] = dados
        #cria uma chave com o valor da coluna 0 e associa o valor com os dados

    categorias.close() #fecha o arquivo   
    print(dicCategorias) #exibe o dicionario