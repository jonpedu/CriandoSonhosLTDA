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
            
            if a == 'y':
                print('\n' + '=' * 40)
                print(f'{"CADASTRAR NOVO PEDIDO":^40}')
                print('=' * 40)
                adicionar = 'y'
                pedidos = PedidoControler.search_in_pedidos_all(database_name)
                numero_pedido = len(pedidos) + 1
                item_count = 1
                while adicionar == 'y':
                    print(f'\nInsira o número do {item_count}º item desejado:')
                    try:
                        item = int(input('  > Número do item: '))
                        quantidade = int(input('  > Quantidade: '))
                    except ValueError:
                        print('  [!] Por favor, insira valores numéricos válidos.')
                        continue
                    item_count += 1

                    # Calculando o valor do pedido em tempo real
                    valor_item = ItemControler.valor_item(database_name, item)
                    if not valor_item or not valor_item[0]:
                        print('  [!] Item não encontrado. Tente novamente.')
                        continue
                    subtotal = valor_item[0][0] * quantidade
                    print(f'  > Subtotal deste item: R${subtotal:.2f}')
                    valor_total += subtotal

                    for _ in range(quantidade):
                        lista_itens.append((numero_pedido, item))

                    adicionar = input('\nAdicionar outro item? (y-Sim, n-Não): ').strip().lower()
                    while adicionar not in ['y', 'n']:
                        adicionar = input('  [!] Opção inválida. Digite "y" para Sim ou "n" para Não: ').strip().lower()

                print('\n' + '=' * 40)
                print(f'{"FINALIZAR PEDIDO":^40}')
                print('=' * 40)
                print(f'Número do pedido: {numero_pedido}')
                print(f'Itens selecionados: {len(lista_itens)}')
                print(f'Valor parcial do pedido: R${valor_total:.2f}')

                delivery = input('\nO pedido é para delivery? (s-Sim, n-Não): ').strip().lower()
                while delivery not in ['s', 'n']:
                    delivery = input('  [!] Opção inválida. Digite "s" para Sim ou "n" para Não: ').strip().lower()
                delivery_bool = True if delivery == 's' else False

                endereco = ''
                if delivery_bool:
                    endereco = input('Informe o endereço de entrega: ').strip()
                    while not endereco:
                        endereco = input('  [!] Endereço não pode ser vazio. Informe o endereço de entrega: ').strip()

                print('\nStatus do pedido:')
                print('  1 - Preparo')
                print('  2 - Pronto')
                print('  3 - Entregue')
                try:
                    status_aux = int(input('Selecione o status (1/2/3): '))
                except ValueError:
                    status_aux = 1
                if status_aux == 1:
                    status = 'preparo'
                elif status_aux == 2:
                    status = 'pronto'
                else:
                    status = 'entregue'

                print('\n' + '-' * 40)
                print(f'Valor Final do Pedido: R${valor_total:.2f}')
                data_hoje = date.today()
                data_formatada = data_hoje.strftime('%d/%m/%Y')
                print(f'Data do pedido: {data_formatada}')
                if delivery_bool:
                    print(f'Endereço de entrega: {endereco}')
                print('-' * 40 + '\n')

                pedido = Pedido(status, str(delivery_bool), endereco, data_formatada, float(valor_total))
                PedidoControler.insert_into_pedidos(database_name, pedido)
                for elem in lista_itens:
                    ItemControler.insert_into_itens_pedidos(database_name, elem)

            elif a == 'n':
                print('\nVoltando ao Menu inicial...')
                time.sleep(2)
                break