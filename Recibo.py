class Recibo:

    def _init_(self , nome):
        self.nome = nome


    def descriçao (self, valor):
        self._descricao = valor

    @property
    def valor(self):
        return(self._valor) 

    @valor.setter
    def valor(self,_valor):
        self._valor = _valor


    def _str_(self):
    
        texto = f'recebemos de {self.nome} a quantia de R$ {self. _valor}'    
        descricao = f'\nreferente{self._descricao}'     
        titulo = 'Recibo'.center(len(texto), '*')
        dados = f'{titulo}\n{texto}{descricao}'
        return(dados)  