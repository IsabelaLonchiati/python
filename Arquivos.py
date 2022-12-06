import os.path
class tabCat:
    def dicCat(self):
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
        return dicCategorias

class tabProd:
    def listProd(self):
        arquivo = 'produtos.csv'

        if os.path.isfile(arquivo):
            produtos = open(arquivo, 'r', encoding='utf-8')

            listadeprodutos = []
            for linha in produtos:
                colunas = linha.strip().split(";")
                colunas[0] = int(colunas[0])
                colunas[2] = int(colunas[2])
                colunas[4] = int(colunas[4])
                colunas[5] = int(colunas[5])
                colunas[6] = int(colunas[6])
                colunas[7] = int(colunas[7])
                colunas[8] = float(colunas[8])
                colunas[9] = float(colunas[9])
                listadeprodutos.append(colunas)
            produtos.close()
            return listadeprodutos       