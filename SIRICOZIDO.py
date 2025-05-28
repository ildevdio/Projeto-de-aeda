import json
import os
from time import sleep
os.system('cls')

arquivo = os.path.join(os.path.dirname(__file__), 'storage.json')

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
    with open(arquivo, 'r', encoding="utf-8") as f:   
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

    with open(arquivo, 'w', encoding='utf-8') as f:
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

    with open(arquivo, 'w', encoding='utf-8') as f:
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
    
def menuReserva():
    print("=======================")
    print("\n     | Módulos |     ")
    print("\n  1 - Fazer reserva  ")
    print("  2 - Cancelar Reserva ")
    print("  3 - Ver reservas     ")
    print("  4 - Editar Reserva   ")
    print("  5 - Sair             ")
    print("\n=======================") 
    
def adicionarReserva():
    informacoes = carregarInfo()  # Renomeie para 'informacoes' ou algo mais claro

    if informacoes['mesas']:
        
        print("Mesas Utilizadas:", end="")
        for lista in informacoes['mesas']:
            print(f"{lista['mesa']} ", end="")
        print()    
        print("-"*50)
    else:
        print("Não há mesas reservadas.")
    
    name = str(input("Qual o seu nome?: "))
    email = str(input("Qual o seu email?: "))
    numero_mesa = int(input("Escolha a mesa: "))
    qtde_mesa = int(input("Insira a quantidade de mesas: (Quantidade Máxima é  10)"))    
    while qtde_mesa > 10:
        print("Quantidade excede nosso limite de mesas por reserva. ")  
        qtde_mesa = int(input("Insira a quantidade de mesas: "))

    while qtde_mesa <= 0:
        print("Quantidade inválida. ")  
        qtde_mesa = int(input("Insira a quantidade de mesas: "))


    id_mesa = len(informacoes["mesas"]) + 1

    

    mesa_ocupada = False
    for verificar in informacoes["mesas"]:
        if numero_mesa == verificar["mesa"]:
            mesa_ocupada = True
            break

    if mesa_ocupada:
        print("Esta mesa já está ocupada. Por favor, escolha outra.")
       
    else:
        remessa = {
        "nome": name,
        "email": email,
        "mesa": numero_mesa,  
        "qtde_mesas": qtde_mesa,
        "id_da_mesa": id_mesa
        }
        informacoes["mesas"].append(remessa)


    
        print(f"seu id é: {remessa['id_da_mesa']}")
                        
        with open(arquivo, 'w', encoding='utf-8') as arq:
            json.dump(informacoes, arq, indent=4, ensure_ascii=False)  # Corrigido: 'informacoes' em vez de 'mesas'

                    
                    
def removerReserva():
    
    informacoes = carregarInfo()

    if not informacoes['mesas']:
        print("Não há reservas no momento.")
        return

    try:
        quest = int(input("Qual o seu id? "))
    except ValueError:
        print("ID inválido! Deve ser um número.")
        return

    encontrou = False

    for reserva in informacoes["mesas"]:
        if reserva['id_da_mesa'] == quest:
            informacoes["mesas"].remove(reserva)
            encontrou = True
            print("Reserva removida com sucesso.")
            break

    if encontrou:
        with open(arquivo, 'w', encoding='utf-8') as arq:
            json.dump(informacoes, arq, indent=4, ensure_ascii=False)
    else:
        print("ID não encontrado.")
            
def listarReserva():
    informacoes = carregarInfo()

    if informacoes['mesas']:

        for lista in informacoes['mesas']:
            print(f"\nNome: {lista['nome']}")
            print(f"E-mail: {lista['email']}")
            print(f"Número da mesa: {lista['mesa']}")
            print(f"Quantidade de mesas:{lista['qtde_mesas']}")
            print(f"Id: {lista['id_da_mesa']}\n")
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
                while True:
                    menuReserva()
                    op_mesa = int(input("Insira a opção desejada:"))
                    
                    if op_mesa == 1: 
                        adicionarReserva()
                        
                    
                    elif op_mesa == 2:
                        removerReserva()
                        

                    elif op_mesa == 3:
                        listarReserva()
                        
    

                    elif op_mesa == 5:
                        print("saindo...")
                        sleep(3)
                        
                
                    else:
                        print("Erro, escolha uma opção válida.")
                        

                    

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
        