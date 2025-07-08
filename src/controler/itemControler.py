from model.item import Item

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

class ItemControler:
    
    # exibir todos os itens do menu
    @staticmethod
    def mostrar_itens_menu(database_name: str) -> object:
        """
        Chama a função que exibe todos os itens do menu no banco de dados.

        :param database_name: Nome do banco de dados a ser consultado (string).
        :return: Lista de itens (list) ou código de erro (string).
        """
        result = Item.mostrar_itens_menu(database_name)
        return result
    
    
    # inserindo um item no banco de dados
    @staticmethod
    def insert_into_item(database_name: str, data: list) -> bool:
        """
        Insere um novo item na tabela de Itens no banco de dados.

        :param database_name: Nome do banco de dados (string).
        :param data: Lista com os valores [nome, descricao, preco, categoria].
        :return: True se a inserção for bem-sucedida, ou código de erro (string).
        """
        nome = data[0]
        descricao = data[1]
        preco = data[2]
        tipo = data[3]

        # Cria o objeto Item
        item_obj = Item(nome, preco, tipo, descricao)

        # Chama o model passando o objeto
        result = Item.insert_into_item(database_name, item_obj)
        return result
    
    
    # tabela que liga cada pedido ao menu
    @staticmethod
    def insert_into_itens_pedidos(database_name: str, data: list) -> bool:
        """
        Insere a relação entre os itens e os pedidos na tabela ItensPedidos.

        :param database_name: Nome do banco de dados (string).
        :param data: Lista com o `IdPedido` e `IdItem` a serem inseridos (list).
        :return: True se a inserção for bem-sucedida, ou código de erro (string).
        """
        result = Item.insert_into_itens_pedidos(database_name, data)
        return result
    
    # tabela que liga cada pedido ao menu pesquisando
    @staticmethod
    def search_into_itens_pedidos_id(database_name: str, indice: int) -> list:
        """
        Pesquisa a lista de itens associados a um pedido, fornecendo o `IdPedido`.

        :param database_name: Nome do banco de dados (string).
        :param indice: ID do pedido para o qual os itens serão consultados (int).
        :return: Lista de itens relacionados ao pedido (list) ou código de erro (string).
        """
        result = Item.search_into_itens_pedidos_id(database_name, indice)
        return result
        
    # valor de um item informado pelo seu indice
    @staticmethod
    def valor_item(database_name: str, indice: int) -> object:
        """
        Retorna o valor (preço) de um item a partir do seu `IdItens`.

        :param database_name: Nome do banco de dados (string).
        :param indice: ID do item para o qual o preço será consultado (int).
        :return: Lista com o valor do item pesquisado ou código de erro (string).
        """
        result = Item.valor_item(database_name, indice)
        return result
    
    @staticmethod
    def search_item_id(database_name: str, indice: int) -> list:
        """
        Pesquisa as informações de um item (Nome, Tipo, Descrição, Preço) pelo seu `IdItens`.

        :param database_name: Nome do banco de dados (string).
        :param indice: ID do item para o qual as informações serão consultadas (int).
        :return: Informações do item (tuple) ou código de erro (string).
        """
    
        result = Item.search_item_id(database_name, indice)
        return result

    @staticmethod
    def delete_item(database_name: str, item_id: int) -> bool:
        result = Item.delete_item(database_name, item_id)
        return result
