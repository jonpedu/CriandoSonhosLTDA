#Necessário para realizar import em python
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controler.pedidoControler import PedidoControler
from controler.itemControler import ItemControler

class Janela2:
    def mostrar_janela2(database_name: str):
        faturamento = 0
        print('\n====== PESQUISAR PEDIDO ======')
        print('1 - Único')
        print('2 - Todos')
        print('3 - Atualizar Estado')
        q = int(input('Selecione uma opção: '))

        # Opção para mostrar um pedido em específico
        if q == 1:
            indice = int(input('\nDigite o índice do pedido: '))
            resume = ItemControler.search_into_itens_pedidos_id(database_name, indice)
            informacoes_pedido = PedidoControler.search_in_pedidos_id(database_name, indice)[0]
            quantidade_itens = len(resume)
            print(f'\n===== RESUMO DO PEDIDO Nº {indice} =====')
            print('-' * 40)
            for elem in resume:
                print(f"Tipo      : {elem[2]}")
                print(f"Sabor     : {elem[0]}")
                print(f"Descrição : {elem[3]}")
                print(f"Valor     : R$ {elem[1]:.2f}")
                print('-' * 40)
            print(f"Total de itens: {quantidade_itens}\n")
            if len(informacoes_pedido) > 0:
                print("=== INFORMAÇÕES DO PEDIDO ===")
                print(f"Status   : {informacoes_pedido[1]}")
                print(f"Delivery : {'Sim' if informacoes_pedido[2] else 'Não'}")
                print(f"Endereço : {informacoes_pedido[3]}")
                print(f"Data     : {informacoes_pedido[4]}")
                print(f"Valor    : R$ {informacoes_pedido[5]:.2f}")
            print('\nVoltando ao menu inicial...\n')

        # Opção para mostrar toda a lista de pedidos
        elif q == 2:
            row = PedidoControler.search_in_pedidos_all(database_name)
            faturamento = 0
            print('\n========== LISTA DE PEDIDOS ==========')
            print(f"{'Nº':<4} {'Estado':<10} {'Delivery':<10} {'Endereço':<25} {'Valor':>10}")
            print('-' * 65)
            endereco = ''
            i = 1
            for elem in row:
                endereco_raw = elem.endereco
                if isinstance(endereco_raw, (tuple, list)):
                    endereco_raw = endereco_raw[0]
                faturamento += elem.valor_total
                endereco = endereco_raw or 'Não informado'
                print(f"{i:<4} {elem.status:<10} {'Sim' if elem.delivery else 'Não':<10} {endereco:<25} R$ {elem.valor_total:>8.2f}")
                i += 1
            print('-' * 65)
            print(f'Faturamento total: R$ {faturamento:.2f}\n')


        #corrigir logica de atualização de status (mudar dentro do elif de '3' para 3)
        elif q == '3':
            indice = int(input('\nDigite o índice do pedido: '))
            resume = ItemControler.search_into_itens_pedidos_id(database_name, indice)
            quantidade_itens = len(resume)
            if quantidade_itens > 0:
                informacoes_pedido = PedidoControler.search_in_pedidos_id(database_name, indice)[0]
                print(f'\n===== RESUMO DO PEDIDO Nº {indice} =====')
                print('-' * 40)
                for elem in resume:
                    print(f"Tipo      : {elem[2]}")
                    print(f"Sabor     : {elem[0]}")
                    print(f"Descrição : {elem[3]}")
                    print(f"Valor     : R$ {elem[1]:.2f}")
                    print('-' * 40)
                print(f"Total de itens: {quantidade_itens}\n")
                print("=== INFORMAÇÕES DO PEDIDO ===")
                print(f"Status   : {informacoes_pedido[1]}")
                print(f"Delivery : {informacoes_pedido[2]}")
                print(f"Endereço : {informacoes_pedido[3]}")
                print(f"Data     : {informacoes_pedido[4]}")
                print(f"Valor    : R$ {informacoes_pedido[5]:.2f}")
                print('\nAtualize o status do pedido:')
                print('1 - Preparo')
                print('2 - Pronto')
                print('3 - Entregue')
                novo_status = int(input('Digite o novo status: '))
                if novo_status / novo_status != 1:
                    print('\nEntrada inválida, retornando...\n')
                else:
                    result = PedidoControler.update_pedido_status_id(database_name, indice, novo_status)
                    
                    if result:
                        print(f'\nStatus do Pedido {indice} atualizado com sucesso!')
                    else:
                        print('\nErro ao atualizar.')
            else:
                print('\nÍndice inválido.')
        else:
            print('\nEntrada inválida, retornando...\n')