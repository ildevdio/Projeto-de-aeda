import json
import os
from time import sleep
os.system('cls')

arquivo = os.path.join(os.path.dirname(__file__), 'storage.json')
mesa_qtde = 25

def carregarInfo():
    #Verifica se o arquivo existe, se não existir, cria o arquivo com uma lista vazia
    if not os.path.exists(arquivo):
        dados_iniciais = {
            "cardapio" : [],
            "mesas" : [],
            "pedidos" : []
        }
        with open(arquivo, 'w', encoding="utf-8") as f:
            json.dump(dados_iniciais, f, indent=4, ensure_ascii=False)
            
    #carrega o conteúdo
    with open(arquivo, 'r') as f:   
        return json.load(f)


def adcionarPratos(idPrato, nomePrato, descricaoPrato, precoPrato):
    informacoes = carregarInfo()
    
    idPrato = len(informacoes["cardapio"]) +1
    
    nomePrato = str(input("Qual o nome do novo prato?: ").title())
                                                
    descricaoPrato = str(input("Descreva o novo prato: ").lower())
                                            
    precoPrato = float(input("Insira o preço do novo prato (ex R$ 24.99): R$ "))
    try:
        precoPrato = float(precoPrato)
    except ValueError:
        print("Valor inválido! Digite apenas números (ex: 24.99).")
                            
    novoPrato = {
        'id':idPrato , 
        'nome': nomePrato, 
        'descricao': descricaoPrato, 
        'preco': precoPrato
    }
    informacoes["cardapio"].append(novoPrato)


    

    #confirma que a informação foi adicionada
    with open(arquivo, 'w') as f:
        json.dump(informacoes, f, indent=4, ensure_ascii=False)
    print("Prato adcionado com sucesso!")


def editarPrato(idPrato,novoNomePrato,novoDescPrato,novoPrecoPrato):
    informacoes = carregarInfo()
    for prato in informacoes['cardapio']:        
         
        
        if prato['id'] == idPrato:
            
            prato['nome'] = novoNomePrato
            prato['descricao'] = novoDescPrato
            prato['preco'] = novoPrecoPrato

            print("INFORMAÇÕES ATUALIZADAS COM SUCESSO!")       
            break
        else: 
            print("ID NÃO ENCONTRADO")
            break

    with open(arquivo, 'w') as f:
        json.dump(informacoes, f, indent=4, ensure_ascii=False)



def visualizarCardapio():
    informacoes = carregarInfo()

    print("=" *50)
    print("CARDAPIO".center(50))
    print("=" *50)
    print("-"*50)
    
    if informacoes["cardapio"]:

        for prato in informacoes["cardapio"]:
            print(f"\nID: {prato['id']}")
            print(f"Nome: {prato['nome']}")
            print(f"Descrição: {prato['descricao']}")
            print(f"Preço: R$ {prato['preco']:.2f}")
            print("-"*50)
    else:
        print("Não há pratos adcionados.")



def siriCozido():

    print("=======================")
    print("                       ")
    print("  | 🦀Restaurante🦀 | ")
    print("   |  Siri Cozido |    ")
    print("                       ")
    print("=======================")


def menuCardapio():
    print("                       ")
    print("=======================")
    print("                       ")
    print("  1 - Ver os pratos    ")
    print("  2 - Criar um novo    ")
    print("  3 - Editar           ")
    print("  4 - Deletar          ")    
    print("  5 - Sair para o menu ")
    print("=======================")

def menuPedidos():
    print("                       ")
    print("=======================")
    print("                       ")
    print("  1 - Adicionar Pedi   ")
    print("  2 - Cancelar Pedido  ")
    print("  3 - Editar Pedido    ")
    print("  4 - Listar Pedidos   ")
    print("  5 - Verificar Status do Pedido ")    
    print("  6 - Sair para o menu ")
    print("=======================")

def menuGeral():
    print("                       ")
    print("=======================")
    print("                       ")
    print("     | Módulos |       ")
    print("                       ")
    print("  1 - Cardápio         ")
    print("  2 - Reserva          ")
    print("  3 - Pedidos          ")
    print("  4 - Sair             ")
    print("                       ")
    print("=======================")
    
def homepage():
                        
    print("                       ")
    print("=======================")
    print("                       ")
    print("     | Módulos |       ")
    print("                       ")
    print("  1 - Criar reserva    ")
    print("  2 - Remover reserva  ")
    print("  3 - Listar reservas  ")
    print("  4 - Sair             ")
    print("                       ")
    print("=======================")  
    
def reservaMesas():
    informacoes = carregarInfo()  # Renomeie para 'informacoes' ou algo mais claro
    mesas_ocupadas = len(informacoes["mesas"])  # Acessa as mesas reservadas
    mesas_disponiveis = mesa_qtde - mesas_ocupadas

                            
    
    name = str(input("Qual o seu nome?: ").title())
    email = str(input("Qual o seu email?: ").lower())
    numero_mesa = int(input("Escolha a mesa: "))
    qtde_mesa = int(input("Insira a quantidade de mesas: "))
    while qtde_mesa >=25:
        print("Quantidade excede nosso limite de mesas. ")  
        qtde_mesa = int(input("Insira a quantidade de mesas: "))                                        
                              
    

    remessa = {
        "nome": name,
        "email": email,
        "mesa": numero_mesa,  # Usa o novo nome
        "qtde_mesas": qtde_mesa
        }
    informacoes["mesas"].append(remessa)  # Agora funciona, pois 'informacoes' é o dicionário
                        
    with open(arquivo, 'w', encoding='utf-8') as arq:
        json.dump(informacoes, arq, indent=4, ensure_ascii=False)  # Corrigido: 'informacoes' em vez de 'mesas'

                    
                    
def removerReservaMesas():
        informacoes = carregarInfo()     
        print("Remover reservas-->")
        listarMesas()

        if not informacoes["mesas"]:
            print("Não há reservas no momento.")
            return
        nome_reserva = str(input("Digite o nome utilizado para a reserva-->"))

        nome_encontrado = None
        for reserva in informacoes['mesas']:
            

                    

                    
def listarMesas():
    informacoes = carregarInfo()

    if informacoes['mesas']:

        for lista in informacoes['mesas']:
            print(f"Nome: {lista['nome']}")
            print(f"E-mail: {lista['email']}")
            print(f"Número da mesa: {lista['mesa']}")
            print(f"Quantidade de mesas:{lista['qtde_mesas']}")
            print("-"*50)
    else:
        print("Não há pratos adcionados.")
                    
def main():
    while True:
        
        siriCozido()
        
        menuGeral()
        
        opModulo=int(input("Escolha o Módulo Desejado: "))

        match opModulo:
            case 1: #Cardápio
                    print("Cardápio")
                    while True:
                        
                        menuCardapio()
                        
                        opcardapio = int(input("Escolha uma das opções: "))
                
                        if opcardapio == 1: #ver cardápio
                            os.system('cls')
                            visualizarCardapio()
                            

                        
                        elif opcardapio == 2: #adicionar prato
                            os.system('cls')
                            adcionarPratos('idPrato', 'nomePrato', 'descricaoPrato', 'precoPrato')   
                            break
                        
                        elif opcardapio == 3: #Editar
                            
                            os.system('cls')
                            
                            idPrato = str(input("Insira o Id do prato que quer editar: "))
                            try: 
                                idPrato = int(idPrato)
                            except ValueError:
                                print("VALOR INVÁLIDO")
                                break
                                                            
                            novoNomePrato = str(input("Insira o novo nome do prato: ")).title()
                            
                            novoDescPrato = str(input("Insira a nova descrição do prato: ")).lower()

                            novoPrecoPrato = str(input("Insira o novo preço do prato: "))                           
                            try: 
                                novoPrecoPrato = float(novoPrecoPrato)
                            except ValueError:
                                print("VALOR INVÁLIDO (ex: 19.99)")
                                break

                            editarPrato(idPrato,novoNomePrato,novoDescPrato,novoPrecoPrato,)
                            

                            print("em dev")

                            break
                        
                        elif opcardapio == 4: #Excluir
                            
                            print("em dev")
                            break
                        elif opcardapio == 5: #Sair

                            print("Saindo para o menu principal...")
                            sleep(3)
                            break
                        else:
                            print("Opção inválida.")
                            break


            case 2: #Crud 2
                
                homepage()
                op_mesa = int(input("Insira a opção desejada:"))

                while True: 
                    if op_mesa == 1: 
                        reservaMesas()
                        break
                    elif op_mesa == 2:
                        removerReservaMesas()
                        break
                    elif op_mesa == 3:
                        listarMesas()
                        break
                    
                    elif op_mesa == 4:
                        print("Voltandooo...")
                        sleep(3)
                        break
            
                    else:
                        print("Erro, escolha uma opção válida.")
                        break

                  

                
                    
                
                
            case 3:  # CRUD 3
                while True:
                    os.system('cls')
                    print("\n==================================================")
                    print("PEDIDOS")
                    print("==================================================\n")
                    menuPedidos()
                    opPedidos = int(input("Informe a opção que deseja: "))

                    if opPedidos == 1:
                        os.system('cls')
                        informacoes = carregarInfo()
                        mesaPedido = input("Informe o número da mesa: ")
                        itens_pedido = []  # array armazenando itens antes de colocar no json
                        
                        while True:
                            visualizarCardapio()  #monstrando cardapio(copiei de gabriel fds)
                            comidasPedido = int(input("\nInsira o ID da comida solicitada: "))
                            # Valida se o prato existe
                            prato_encontrado = None #começa atribuindo valor vazio pro prato, como se ele nao existisse
                            for prato in informacoes["cardapio"]:
                                if prato['id'] == comidasPedido:
                                    prato_encontrado = prato
                                    break
                            if not prato_encontrado:
                                print("ID inválido! Insira um ID do cardápio.")
                                continue
                            
                            quantidade = int(input(f"Quantidade de '{prato_encontrado['nome']}': "))
                            obsPedido = input("Observações (ex: sem cebola): ")
                            itens_pedido.append({
                                'id_prato': comidasPedido,
                                'nome_prato': prato_encontrado['nome'],
                                'quantidade': quantidade,
                                'observacoes': obsPedido,
                                'status': 'Em preparo'
                            })
                            
                            continuar = input("\nAdicionar mais itens? (S/N): ").lower()
                            if continuar != 's':
                                break
                        informacoes["pedidos"].append({
                            'mesa': mesaPedido,
                            'itens': itens_pedido
                        })
                        with open(arquivo, 'w') as f:
                            json.dump(informacoes, f, indent=4, ensure_ascii=False)
                        print("\n✅ Pedido registrado!")
                        input("Pressione Enter para continuar...")

                    elif opPedidos == 2:
                        # Pedir a mesa, depois puxar todos os pedidos da mesa e perguntar qual pedido quer cancelar/remover
                        pass

                    elif opPedidos == 3:
                        # Pedir a mesa, depois puxar todos os pedidos da mesa e perguntar qual pedido quer editar ou editar status dele
                        pass

                    elif opPedidos == 4:
                        # Perguntar se quer listar todos os pedidos, ou só os prontos, ou só os em preparo ou só os entregues
                        pass

                    elif opPedidos == 5:
                        os.system('cls')
                        informacoes = carregarInfo()
                        print("\n==================================================")
                        print("VERIFICAR STATUS DO PEDIDO")
                        print("==================================================\n")
                        
                        # Verifica se tem pedido no json
                        if not informacoes["pedidos"]:
                            print("Não há pedidos cadastrados no sistema.")
                            input("\nPressione Enter para voltar...")
                            continue
                            
                        mesaPedido = input("Informe o número da mesa para ver os pedidos: ")
                        
                        #filtra pedidos apenas so da mesa informada
                        pedidos_mesa = [pedido for pedido in informacoes["pedidos"] if pedido['mesa'] == mesaPedido]
                        
                        if not pedidos_mesa:
                            print(f"\nNão há pedidos registrados para a mesa {mesaPedido}.")
                            input("\nPressione Enter para voltar...")
                            continue
                            
                        print(f"\n📋 Status dos Pedidos - Mesa {mesaPedido}:")
                        print("="*50)
                        
                        # Mostra todos os pedidos da mesa
                        for pedido in pedidos_mesa:
                            print("\nItens do Pedido:")
                            print("-"*30)
                            for item in pedido['itens']:
                                if item['status'] == "Em preparo":
                                    icone = "⏳"
                                elif item['status'] == "Pronto":
                                    icone = "✅"
                                elif item['status'] == "Entregue":
                                    icone = "✔️"
                                
                                print(f"{icone} {item['nome_prato']} - {item['status']}")
                                print(f"   Quantidade: {item['quantidade']}")
                                if item['observacoes']:
                                    print(f"   Obs: {item['observacoes']}")
                                print("-"*30)
                        
                        input("\nPressione Enter para voltar ao menu...")

                    elif opPedidos == 6:
                        print("Saindo para o menu principal...")
                        sleep(3)
                        break       
                       
                       

                
            case 4:
                    print("Saindo...")
                    sleep(3)
                    print("Volte sempre!")
                    break

if __name__ == "__main__":
    main()
        