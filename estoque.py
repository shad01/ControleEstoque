import dbm
import os
import sys


class Estoque(object):

    def cadastro(self, produto):
        '''
        Faz o cadastro dos produtos no banco de dados

        Parametros:
            cadastro(str): Nome do produto a ser adicionado no 
            banco de dados
        '''
        with dbm.open('estoqueProdutos', 'c') as f:
            f[produto] = produto       
    
    def ver(self):
        '''
        Retorna todos os produtos que foram cadastrados
        '''
        try:
            with dbm.open('estoqueProdutos', 'r') as f:
                for p in f:
                    print(p.decode('utf-8'))
        except FileNotFoundError:
            print('Arquivo ainda não foi criado')

    def remover(self, removido):
        '''
        Exclui o produto especificado do banco de dados

        Parametros:
            removido(str): Nome do produto a ser removido do
            banco de dados
        '''
        try:
            with dbm.open('estoqueProdutos', 'w') as f:
                del f[removido]
        except Exception:
            pass


if __name__ == '__main__':
    estoque = Estoque()

    while True:
        opcao = int(input('''Cadastrar Produto: 1 
        \rVerificar Estoque: 2 
        \rRemover Produto: 3
        \rSair: 4\n>>> '''))
        
        os.system('cls') 
        if opcao == 1 or opcao == 3:
            nome_produto = str(input('Nome do produto: '))
            if opcao == 1:
                estoque.cadastro(nome_produto)
            elif opcao == 3:
                estoque.remover(nome_produto)
        elif opcao == 2:
            estoque.ver()
        elif opcao == 4:
            sys.exit()