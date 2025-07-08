import sys
import time
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# models
from model.pedido import Pedido
from model.item import Item
from model.database import Database

# controllers
from controler.pedidoControler import PedidoControler
from controler.itemControler import ItemControler
from controler.databaseControler import DatabaseControler
from controler.relatorioController import RelatorioControler

# views
from view.janela1 import Janela1
from view.janela2 import Janela2
from view.janela3 import Janela3  

# report
from report.relatorio1 import PDF

database = Database('TESTE.db') 
cursor = DatabaseControler.conect_database(database.name)

DatabaseControler.create_table_itens(cursor)
DatabaseControler.create_table_pedidos(cursor)
DatabaseControler.create_table_itens_pedidos(cursor)

a = 'y'
print("""
╔════════════════════════════════════════════════════════════╗
║                   Bem-vindo ao Software                    ║
║                       Pizza Mais                           ║
║                  - Criando Sonhos LTDA -                   ║
╠════════════════════════════════════════════════════════════╣
║              Estabelecimento: Pizza Ciclano                ║
║            "Seus sonhos têm formato e borda!"              ║
╚════════════════════════════════════════════════════════════╝
""")

while a == 'y':
    print("Selecione uma opção:\n")
    print("  1 - Cadastrar Pedido")
    print("  2 - Pesquisar Pedido")
    print("  3 - Gerar Relatório")
    print("  4 - Inserir Itens no Menu")
    print("  5 - Excluir Item do Menu")
    print("  6 - Encerrar")
    opcao = str(input("Digite o número da opção desejada: "))

    if opcao == '1':
        print("\n--- Cadastro de Pedido ---")
        Janela1.mostrar_janela1(database.name)
    elif opcao == '2':
        print("\n--- Pesquisa de Pedido ---")
        Janela2.mostrar_janela2(database.name)
    elif opcao == '3':
        print("\n--- Gerando Relatório ---")
        timestamp_atual = str(time.time())
        dados_relatorio = RelatorioControler.preparar_dados_relatorio(database.name)
        relatorio = PDF.gerar_pdf(f'Relatorio{timestamp_atual}.pdf', dados_relatorio["pedidos"], dados_relatorio["faturamento_total"])
        if relatorio:
            print("Relatório gerado com sucesso em 'Relatorio.pdf'.")
        else:
            print("Erro ao gerar o relatório.")
    elif opcao == '4':
        print("\n--- Inserir Itens no Menu ---")
        Janela3.mostrar_janela3(database.name)
    elif opcao == '5':
        print("\n--- Excluir Item do Menu ---")
        try:
            id_str = input("Digite o ID do item que deseja excluir: ").strip()
            item_id = int(id_str)
            resultado = ItemControler.delete_item(database.name, item_id)
            if resultado == True:
                print(f"Item com ID {item_id} excluído com sucesso!")
            else:
                print(f"Erro ao excluir item: {resultado}")
        except ValueError:
            print("ID inválido. Digite um número inteiro válido.")
    elif opcao == '6':
        print("\nEncerrando o sistema. Até logo!")
        a = 'n'
        break
    else:
        print("\n[!] Opção inválida. Tente novamente.")

exit()



#manutenções em: itemControler.py, janela1.py, pedidoControler.py