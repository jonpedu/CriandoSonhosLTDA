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
from view.janela4 import Janela4  

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
        Janela1.mostrar_janela1(database.name)
    elif opcao == '2':
        Janela2.mostrar_janela2(database.name)
    
    elif opcao == '3':
        print("\n╔═══════════════════════════════╗")
        print("║      GERANDO RELATÓRIO...     ║")
        print("╚═══════════════════════════════╝")
        print("Iniciando coleta de dados", end="")
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.4)
        print("\n") # New line after the dots
        
        timestamp_atual = str(time.time())
        dados_relatorio = RelatorioControler.preparar_dados_relatorio(database.name)
        relatorio = PDF.gerar_pdf(f'Relatorio{timestamp_atual}.pdf', dados_relatorio["pedidos"], dados_relatorio["faturamento_total"])
        
        if relatorio:
            print("✔ Relatório gerado com sucesso!")
            print(f"  Arquivo salvo como 'Relatorio{timestamp_atual}.pdf'.")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━") # Separator for success
        else:
            print("✖ Falha ao gerar o relatório.")
            print("  Por favor, verifique se há dados disponíveis ou tente novamente.")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━") # Separator for error

    elif opcao == '4':
        Janela3.mostrar_janela3(database.name)
    elif opcao == '5':
        Janela4.mostrar_janela4(database.name)
    elif opcao == '6':
        print("\n-------------------------------------")
        print("  Obrigado por usar nosso sistema!  ")
        for i in range(3):
            print(".", end="", flush=True) # Adiciona pontos a cada 0.5 segundos
            time.sleep(0.5)
        print("\n        Até a próxima! :)            ")
        print("-------------------------------------")
        a = 'n'
        break
    else:
        print("\n[!] Opção inválida. Tente novamente.")

exit()



#manutenções em: itemControler.py, janela1.py, pedidoControler.py