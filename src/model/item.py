#import de model
from model.database import Database

#Necessário para realizar import em python
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


class Item:

    def __init__(self, nome: str, preco: float, tipo: str, descricao: str) -> None:
        """
        Construtor da classe Item.

        :param nome: Nome do item (string).
        :param preco: Preço do item (float).
        :param tipo: Tipo do item (string).
        :param descricao: Descrição do item (string).
        """
        self.nome = nome
        self.preco = preco
        self.tipo = tipo
        self.descricao = descricao
    
    #exibir todos os itens do menu
    @staticmethod
    def mostrar_itens_menu(database_name: str)-> object:
        """
        Exibe todos os itens do menu, consultando a tabela 'Itens' no banco de dados.

        :param database_name: Nome do banco de dados a ser consultado (string).
        :return: Lista de tuplas contendo os itens, ou código de erro caso ocorra um erro
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                SELECT * FROM Itens;
                ''')
                rows = cursor.fetchall()
                return(rows)

        except OSError as e:
            #criar código de erro
            print(e)
            return 'I1'    
        
    
    
    #inserindo um item no banco de dados
    @staticmethod
    def insert_into_item(database_name: str, data: list) -> bool:
        """
        Insere um novo item na tabela de Itens no banco de dados 

        :param database_name: nome do banco de dados (string)
        :param data: lista com os valores a serem inseridos para um item (list)
        :return: True se tudo acontecer como esperado, código de erro em caso de erro
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO Itens (Nome, Preco, Tipo, Descricao) VALUES (?,?,?,?);
                    ''', (data.nome,data.preco,data.tipo,data.descricao))
                conn.commit()
                return True
        except OSError as e:
            print(e)
            return 'I2'
    
    
    #tabela que liga cada pedido ao menu
    @staticmethod
    def insert_into_itens_pedidos(database_name: str, data: list) -> bool:
        """
        Insere na tabela ItensPedidos a relação entre os [0-N] itens por pedido

        :param database_name: nome do banco de dados (string)
        :param data: lista com IdPedido e IdItem a serem inseridos (list)
        :return: True se tudo acontecer como esperado, código de erro em caso de erro
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO ItensPedidos (IdPedido, IdItem) VALUES (?,?);
                    ''', (data[0],data[1]))
                conn.commit()
                return True
            
        except OSError as e:
            print(e)
            return 'I3'
    
    #tabela que liga cada pedido ao menu pesquisando
    @staticmethod
    def search_into_itens_pedidos_id(database_name: str, indice: int) -> object:
        """
        Pesquisa a lista de itens dentro da tabelea itens_pedido, informando o IdPedido

        :param database_name: nome do banco de dados (string)
        :param indice: Id do pedido que será utilizado para consulta dos itens (int)
        :return: Lista de itens relacionados à pesquisa ou o código de erro (object||string)
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute(f'''
                    SELECT REPLACE(i.Nome, '-', ' ') AS Nome, i.Preco, i.Tipo, i.Descricao
                    FROM Pedidos p
                    LEFT JOIN ItensPedidos ip ON ip.IdPedido = p.IdPedido
                    LEFT JOIN Itens i on ip.IdItem = i.IdItens
                    WHERE p.IdPedido = {indice};
                    ''')
                rows = cursor.fetchall()
                return(rows)
    
        except OSError as e:
            print(e)
            return 'I4'
        
    #valor de um item informado pelo seu indice
    @staticmethod
    def valor_item(database_name: str, indice: int)-> object:
        """
        Pesquisa o valor de um item de acordo com o identificador único informado

        :param database_name: nome do banco de dados (string)
        :param indice: Id do pedido que será utilizado para consulta (int)
        :return: Lista de itens relacionados à pesquisa ou o código de erro (object||string)
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute(f'''
                SELECT Preco FROM Itens WHERE IdItens = {indice};
                ''')
                rows = cursor.fetchall()
                return(rows)

        except OSError as e:
            print(e)
            return 'I5'
    
    @staticmethod
    def search_item_id(database_name: str, indice:int) -> object:
        """
        Pesquisa as informações de um item utilizando o Id do item

        :param database_name: nome do banco de dados (string)
        :param indice: Id do pedido que será utilizado para consulta (int)
        :return: Lista de itens relacionados à pesquisa ou o código de erro (object||string)
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute(f'''
                SELECT Nome,Tipo,Descricao,Preco FROM Itens WHERE IdItens = {indice};
                ''')
                rows = cursor.fetchall()
                return(rows)

        except OSError as e:
            print(e)
            return 'I6'
        
    @staticmethod
    def delete_item(database_name: str, item_id: int) -> bool:
        """
        Exclui um item do banco de dados pelo seu IdItens.

        :param database_name: Nome do banco de dados (string).
        :param item_id: ID do item a ser excluído (int).
        :return: True se a exclusão for bem-sucedida, ou código de erro (string).
        """
        try:
            with Database.conect_database(database_name) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM Itens WHERE IdItens = ?;', (item_id,))
                conn.commit()
                # Verifica se algum registro foi excluído
                if cursor.rowcount == 0:
                    return 'Item não encontrado'
                return True
        except OSError as e:
            print(e)
            return 'I7'  # Código de erro para exclusão


'''
Códigos de Erro

mostrar_itens_menu - I1
insert_into_item - I2
insert_into_itens_pedido - I3
search_into_itens_pedidos_id - I4
valor_item - I5
search_item_id - I6
delete_item - I7

'''
 
 