#para pegar a data de hoje
from datetime import date
import time

#Necessário para realizar import em python
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

#importando os módulos de model
from model.pedido import Pedido

#importando os módulos de controle
from controler.pedidoControler import PedidoControler
from controler.itemControler import ItemControler

#criação da classe janela
class Janela1:
    
    @staticmethod
    def mostrar_janela1(database_name: str) -> None:
        """
        View para o usuário utilizar o software
        
        return None
        """
        
        a = 'y'
        
        menu = ItemControler.mostrar_itens_menu(database_name)

        print('\n' + '=' * 105)
        print(f'{"MENU DE ITENS":^105}')
        print('=' * 105)
        print(f'| {"Nº":^4} | {"Nome":^22} | {"Tipo":^9} | {"Preço":^9} | {"Descrição":^45} |')
        print('-' * 105)
        for item in menu:
            # Supondo que cada item seja uma tupla: (id, nome, preco, tipo, descricao)
            print(f'| {item[0]:^4} | {item[1]:<22.22} | {item[3]:<9.9} | R${item[2]:>7.2f} | {item[4]:<45.45} |')
        print('-' * 105 + '\n')

        while a=='y':
            lista_itens = []
            valor_total=0
            
            a = str(input('Cadastrar pedido (y-Sim, n-Nao): '))
            
            if a=='y':
                print('----------Cadastrar pedido----------\n')
                adicionar = 'y'
                pedidos = PedidoControler.search_in_pedidos_all(database_name)
                numero_pedido = len(pedidos)+1
                while adicionar == 'y':
                    item = int(input('Numero do item: '))
                    quantidade = int(input('Quantidade: '))
                    
                    #calculando em tempo de execução o valor do pedido
                    a = ItemControler.valor_item(database_name, item)
                    b = a[0][0]*quantidade
                    print(b)
                    valor_total+=b
                    
                    for x in range(0,quantidade):#acrescentado o mesmo item várias vezes, de acordo com a quantidade
                        lista_itens.append((numero_pedido,item))
                    
                    adicionar = str(input('Adicionar novo item? (y-Sim, n-Nao): '))
                
                print('\n----------Finalizar pedido----------\n')
                print(f'Numero do pedido: {numero_pedido}')
                delivery = str(input('Delivery (S/N): ')).lower()
                if delivery=='s':
                    delivery = True
                elif delivery=='n':
                    delivery = False
                else:
                    print('Valor incorreto, recomeçando')
                    break
                endereco = str(input('Endereco:'))
                status_aux = int(input('status: 1-preparo, 2-pronto, 3-entregue: '))
                if status_aux == 1:
                    status = 'preparo'
                if status_aux == 2:
                    status = 'pronto'
                else:
                    status = 'entregue'
 
                print(f'Valor Final: R${valor_total}')
                data_hoje = date.today()
                data_formatada = data_hoje.strftime('%d/%m/%Y')
                print(data_formatada)
                print(endereco)
                pedido = Pedido(status, str(delivery), endereco,data_formatada,float(valor_total))
                PedidoControler.insert_into_pedidos(database_name,pedido)
                for elem in lista_itens:
                    ItemControler.insert_into_itens_pedidos(database_name,elem)
                
            elif a=='n':
                print('Voltando ao Menu inicial')
                time.sleep(2)
                break