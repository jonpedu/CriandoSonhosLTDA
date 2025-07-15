import time
import sys
from pathlib import Path

# Necessário para realizar import em python
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controler.itemControler import ItemControler

class Janela4:
    @staticmethod
    def mostrar_janela4(database_name: str) -> None:
        while True:
            # Mostra o menu de itens para que o usuário possa ver os IDs
            menu = ItemControler.mostrar_itens_menu(database_name)

            # Interface do menu
            print('\n' + '=' * 105)
            print(f'{"MENU DE ITENS ATUAIS":^105}')
            print('=' * 105)
            print(f'| {"Nº":^4} | {"Nome":^22} | {"Tipo":^9} | {"Preço":^9} | {"Descrição":^45} |')
            print('-' * 105)
            if not menu:
                print(f'| {"":^103} |')
                print(f'| {"Nenhum item cadastrado no menu.":^103} |')
                print(f'| {"":^103} |')
            else:
                for item in menu:
                    print(f'| {item[0]:^4} | {item[1]:<22.22} | {item[3]:<9.9} | R${item[2]:>7.2f} | {item[4]:<45.45} |')
            print('-' * 105 + '\n')

            # Título da seção de exclusão
            print("\n" + "="*50)
            print(f"{'EXCLUIR ITEM DO MENU':^50}")
            print("="*50)

            try:
                id_str = input("Digite o ID do item que deseja EXCLUIR (ou 'cancelar' para sair): ").strip()
                
                if id_str.lower() == 'cancelar':
                    print("\n---------------------------------------------------")
                    print("       Operação de exclusão cancelada.              ")
                    print("       Retornando ao menu principal...              ")
                    print("---------------------------------------------------\n")
                    time.sleep(1)
                    break

                item_id = int(id_str)
                
                # Opcional: Confirmar exclusão para evitar acidentes
                confirmacao = input(f"Tem certeza que deseja excluir o item com ID {item_id}? (sim/não): ").strip().lower()
                if confirmacao != 'sim':
                    print("Exclusão cancelada pelo usuário.")
                    time.sleep(0.5)
                    continue # Volta para pedir outro ID ou sair

                resultado = ItemControler.delete_item(database_name, item_id)
                
                if resultado == True:
                    print(f"\n✅ Item com ID {item_id} EXCLUÍDO com sucesso!\n")
                else:
                    print(f"\n❌ Erro ao excluir item: {resultado}\n")
            
            except ValueError:
                print("\n❗ ID inválido. Por favor, digite um número inteiro válido.\n")
            except Exception as e:
                print(f"\n❗ Ocorreu um erro inesperado: {e}\n")

            # Pergunta se quer excluir outro item
            opcao = input("Deseja excluir outro item? (Sim/Não) ou 'cancelar' para sair: ").strip().lower()
            while opcao not in ['sim', 'não', 'nao', 'cancelar']:
                print("[!] Opção inválida. Digite 'Sim' para continuar ou 'Não' para sair.")
                opcao = input("Deseja excluir outro item? (Sim/Não) ou 'cancelar' para sair: ").strip().lower()
            
            if opcao in ['não', 'nao', 'cancelar']:
                print("Voltando ao menu principal...\n")
                time.sleep(1)
                break