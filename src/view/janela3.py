from datetime import date
import time

# Necessário para realizar import em python
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controler.itemControler import ItemControler
import time

# Janela 3 responsável pela funcionalidade de fazer o cadastro de novos itens no cardapio

class Janela3:

    @staticmethod
    def mostrar_janela3(database_name: str) -> None:

        menu = ItemControler.mostrar_itens_menu(database_name)

        # Interface do menu
        print('\n' + '=' * 105)
        print(f'{"MENU DE ITENS":^105}')
        print('=' * 105)
        print(f'| {"Nº":^4} | {"Nome":^22} | {"Tipo":^9} | {"Preço":^9} | {"Descrição":^45} |')
        print('-' * 105)
        for item in menu:
            print(f'| {item[0]:^4} | {item[1]:<22.22} | {item[3]:<9.9} | R${item[2]:>7.2f} | {item[4]:<45.45} |')
        print('-' * 105 + '\n')

        # Formulário de cadastro de novos itens
        print("\n" + "="*50)
        print(f"{'CADASTRO DE NOVOS ITENS':^50}")
        print("="*50)

        while True:
            try:
                # Nome do item
                nome = input("Nome do item (obrigatório) ou 'cancelar' para sair: ").strip()
                if nome.lower() == 'cancelar':
                    print("Cadastro cancelado. Voltando ao menu principal...")
                    time.sleep(1)
                    break
                if not nome:
                    print("[!] O nome é obrigatório. Tente novamente.")
                    continue

                # Tipo do item (Tipo do item)
                categorias = ["Pizza", "Bebida", "Sobremesa", "Outro"]
                print("Tipo (digite o número correspondente) ou 'cancelar' para sair:")
                for i, cat in enumerate(categorias, start=1):
                    print(f" {i} - {cat}")
                cat_choice = input("Tipo: ").strip()
                if cat_choice.lower() == 'cancelar':
                    print("Cadastro cancelado. Voltando ao menu principal...")
                    time.sleep(1)
                    break

                if cat_choice not in ['1', '2', '3', '4']:
                    print("[!] Tipo inválido. Tente novamente.")
                    continue

                # Preço do item
                preco_str = input("Preço (obrigatório, número positivo) ou 'cancelar' para sair: ").strip()
                if preco_str.lower() == 'cancelar':
                    print("Cadastro cancelado. Voltando ao menu principal...")
                    time.sleep(1)
                    break
                try:
                    preco = float(preco_str)
                    if preco <= 0:
                        print("[!] Preço deve ser um número positivo. Tente novamente.")
                        continue
                except ValueError:
                    print("[!] Preço inválido. Digite um número válido.")
                    continue

                # Descrição do item
                descricao = input("Descrição do item ou 'cancelar' para sair: ").strip()
                if descricao.lower() == 'cancelar':
                    print("Cadastro cancelado. Voltando ao menu principal...")
                    time.sleep(1)
                    break

                categoria = categorias[int(cat_choice)-1]

                dados = [nome, descricao, preco, categoria]

                resultado = ItemControler.insert_into_item(database_name, dados)

                if resultado == True:
                    print("\n[+] Item cadastrado com sucesso!\n")
                else:
                    print(f"\n[!] Falha ao cadastrar item: {resultado}\n")

                opcao = input("Cadastrar outro item? (Sim/Não) ou 'cancelar' para sair: ").strip().lower()
                while opcao not in ['sim', 'não', 'nao', 'cancelar']:
                    opcao = input("Digite 'Sim' para continuar ou 'Não' para sair: ").strip().lower()
                if opcao in ['não', 'nao', 'cancelar']:
                    print("Voltando ao menu principal...")
                    time.sleep(1)
                    break

            except KeyboardInterrupt:
                print("\nCadastro cancelado pelo usuário.")
                break
