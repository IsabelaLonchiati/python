from os import system
import os.path, datetime
system('cls')

arquivo = 'produtos.csv'

if os.path.isfile(arquivo):
    produtos = open(arquivo, 'r', encoding='utf-8')
    tamanho = os.path.getsize(arquivo)
    dataModificação = os.path.getmtime(arquivo)
    print(f'data de modificação: {datetime.datetime.fromtimestamp(dataModificação)}')
    print(f'tamanho do arquivo(bytes):{tamanho}')

    listadeprodutos = []
    for linha in produtos:
        colunas = linha.strip().split(";")
        print(colunas)
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
    for prod in listadeprodutos:
        print(prod)  

        #Calculando total de custo
        totalcusto = 0
        for prod in listadeprodutos:
            totalcusto += prod[9]
        print(f'total do custo: {totalcusto}')          


        #calcular valor total de vendas apenas das cervejas

        totalvenda = 0
        for prod in listadeprodutos:
            if 'cerveja' in str(prod[1]).lower():
                totalvenda += prod[8]
        print(f'total de vendas: {totalvenda}')

        #Exibe apenas os produtos inativos

        for prod in listadeprodutos:
            if prod[7] == 1:
                print(prod)