import sqlite3
from sqlite3 import Error
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

class Database:

    #cria o banco de dados
    def __init__(self, name: str) -> None:
        """
        Criação do banco de dados, possui um único atributo nome.
        A estrutura do banco está em databaseControler
        try -> instancia o banco 
        except -> em caso de erro informa o erro
        
        :param name: string
        
        :return None
        """
        self.name = name
        try:
            conn = sqlite3.connect(self.name)
            conn.execute('''
            PRAGMA foreign_keys = ON;
            ''')
            
        except OSError as e:
            print(e)
            print('Erro')
            
    
    #conectando/criando o banco, caso ele não exista
    @staticmethod
    def conect_database(database_name: str) -> object:
        """
        Responsável por criar uma conexão com o banco de dados
        try -> estabelece uma conexão com o banco de dados
        except -> informa o erro em caso de erro na operação anterior
        
        :param database_name: string
        :return conn: object || código erro = D1

        """
        try:
            conn = sqlite3.connect(database_name)
            return conn
        except OSError as e:
            print(e)
            print('Erro na conexão')
            return 'D1'

    #criando a tabela dos produtos, caso não exista
    @staticmethod
    def create_table_itens(cursor: object) -> bool:
        """
        Caso não exista, cria uma tabela de chamados em um banco de dados sqlite3
        try -> query para criar a tabela Chamados, caso não exista no banco em questão
        except -> informa o erro em caso de erro na operação anterior

        :param cursor: object
        :return bool || código erro = D2
        """
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Itens (
                IdItens INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome VARHCAR(30),
                Preco REAL,
                Tipo VARCHAR(30),
                Descricao VARCHAR(255),
                CONSTRAINT Produto_Unique UNIQUE (Nome)
                );
            ''')
            return True
        except OSError as e:
            print(e)
            print('Erro ao criar a tabela')
            return 'D2'
    
    #criando a tabela dos pedidos, caso não exista
    @staticmethod
    def create_table_pedidos(cursor: object) -> bool:
        """
        Caso não exista, cria uma tabela de pedidos em um banco de dados sqlite3
        try -> query para criar a tabela Chamados, caso não exista no banco em questão
        except -> informa o erro em caso de erro na operação anterior

        :param cursor: obj
        :return bool || código erro = D3
        """
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Pedidos (
                IdPedido INTEGER PRIMARY KEY AUTOINCREMENT,
                Status VARCHAR(30) NOT NULL,
                Delivery BOLL,
				Endereco VARCHAR(100),
                Data TEXT,
                ValorTotal REAL NOT NULL
                );
            ''')
            return True
        except OSError as e:
            print(e)
            print('Erro ao criar a tabela')
            return 'D3'
    
    #criando a tabela dos itens_pedidos, caso não exista
    @staticmethod
    def create_table_itens_pedidos(cursor: object) -> bool:
        """
        Caso não exista, cria uma tabela de pedidos em um banco de dados sqlite3
        try -> query para criar a tabela Chamados, caso não exista no banco em questão
        except -> informa o erro em caso de erro na operação anterior

        :param cursor: obj
        :return bool || código erro = D4
        """
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ItensPedidos (
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                IdPedido INTEGER NOT NULL,
                IdItem INTEGER NOT NULL,
                FOREIGN KEY(IdPedido) REFERENCES Pedidos(IdPedido),
                FOREIGN KEY(IdItem) REFERENCES Produtos(IdItem)
                );
            ''')
            return True
        except OSError as e:
            print(e)
            print('Erro ao criar a tabela')
            return 'D4'


'''
Códigos de Erro

conect_database - D1
create_table_itens - D2
create_table_pedidos - D3
create_table_itens_pedido - D4

'''