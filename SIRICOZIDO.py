import json
import os
from time import sleep
os.system('cls')

arquivo = os.path.join(os.path.dirname(__file__), 'storage.json')

def carregarInfo():
    if not os.path.exists(arquivo):
        dados_iniciais = {
            "cardapio" : [],
            "mesas" : [],
            "pedidos" : []
        }
        with open(arquivo, 'w', encoding="utf-8") as f:
            json.dump(dados_iniciais, f, indent=4, ensure_ascii=False)
            
    with open(arquivo, 'r', encoding="utf-8") as f:   
        return json.load(f)


def adcionarPratos(idPrato, nomePrato, descricaoPrato, precoPrato):
    informacoes = carregarInfo()
    
    idPrato = len(informacoes["cardapio"]) +1
    
    nomePrato = str(input("Qual o nome do novo prato?: ").title())
                                                
    descricaoPrato = str(input("Descreva o novo prato: ").lower())
                                            
    while True:
        preco_input = input("Insira o preço do novo prato (ex R$ 24.99): R$ ")
        try:
            precoPrato = float(preco_input.replace(',', '.'))
            if precoPrato < 0:
                print("O preço não pode ser negativo. Tente novamente.")
                continue
            break
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
        os.system('cls')
    print("Prato adcionado com sucesso!")


def editarPrato(idPrato,novoNomePrato,novoDescPrato,novoPrecoPrato):
    informacoes = carregarInfo()
    for prato in informacoes['cardapio']:        
         
        
        if prato['id'] == idPrato:
            
            prato['nome'] = novoNomePrato
            prato['descricao'] = novoDescPrato
            prato['preco'] = novoPrecoPrato

            os.system('cls')
            print("INFORMAÇÕES ATUALIZADAS COM SUCESSO!")       
            break
        else:
            os.system('cls') 
            print("ID NÃO ENCONTRADO")
        


    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(informacoes, f, indent=4, ensure_ascii=False)

def deletarPrato():
    informacoes = carregarInfo()
    
    if not informacoes["cardapio"]:
        print("O cardápio está vazio. Nenhum prato para remover.")
        return

    visualizarCardapio()

    try:
        id_prato = int(input("Informe o ID do prato que deseja deletar: "))
    except ValueError:
        print("ID inválido. Digite apenas números.")
        return

    prato_encontrado = None
    for prato in informacoes["cardapio"]:
        if prato["id"] == id_prato:
            prato_encontrado = prato
            break

    if not prato_encontrado:
        print(f"Nenhum prato com o ID {id_prato} foi encontrado.")
        return

    confirmar = input(f"Tem certeza que deseja deletar o prato '{prato_encontrado['nome']}'? (S/N): ").strip().lower()
    if confirmar != 's':
        print("Ação cancelada.")
        return

    informacoes["cardapio"].remove(prato_encontrado)

    for index, prato in enumerate(informacoes["cardapio"], start=1):
        prato["id"] = index

    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(informacoes, f, indent=4, ensure_ascii=False)
    os.system('cls')    
    print("Prato removido com sucesso.")

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

def menuReserva():
    print("=======================")
    print("\n     | Módulos |     ")
    print("\n  1 - Fazer reserva  ")
    print("  2 - Cancelar Reserva ")
    print("  3 - Ver reservas     ")
    print("  4 - Editar Reserva   ")
    print("  5 - Sair             ")
    print("\n=======================") 
    


def menuPedidos():
    print("                       ")
    print("=======================")
    print("                       ")
    print("  1 - Adicionar Pedidos   ")
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
    
def adicionarReserva():
    informacoes = carregarInfo()

    if informacoes['mesas']:
        
        print("Mesas Utilizadas:", end="")
        for lista in informacoes['mesas']:
            print(f"{lista['mesa']} ", end="")
        print()    
        print("-"*50)
    else:
        print("Não há mesas reservadas.")
    
    os.system('cls')
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
    id_existente = False
    for verify_id in informacoes["mesas"]:
        if id_mesa == verify_id["id_da_mesa"]:
            id_existente = True
            break

    if id_existente:
        id_mesa += 1
    
    
    mesa_ocupada = False
    for verificar in informacoes["mesas"]:
        if numero_mesa == verificar["mesa"]:
            mesa_ocupada = True
            break

    if mesa_ocupada:
        os.system("cls")
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
            json.dump(informacoes, arq, indent=4, ensure_ascii=False)

def removerReserva():
    
    informacoes = carregarInfo()

    if not informacoes['mesas']:
        print("Não há reservas no momento.")
        return

    try:
        os.system('cls')
        listarReserva()
        quest = int(input("Qual o seu id? "))
    except ValueError:
        print("ID inválido! Deve ser um número.")
        return

    encontrou = False
    for reserva in informacoes["mesas"]:
        if reserva['id_da_mesa'] == quest:
            informacoes["mesas"].remove(reserva)
            encontrou = True
            os.system('cls')
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

        os.system('cls')
        for lista in informacoes['mesas']:
            print(f"\nNome: {lista['nome']}")
            print(f"E-mail: {lista['email']}")
            print(f"Número da mesa: {lista['mesa']}")
            print(f"Quantidade de mesas:{lista['qtde_mesas']}")
            print(f"Id: {lista['id_da_mesa']}\n")
            print("-"*50)
    else:
        print("Não há reservas adcionadas.")

def editarReserva():
    informacoes = carregarInfo()

    if informacoes['mesas']:
        
        print("Mesas Utilizadas:", end="")
        for lista in informacoes['mesas']:
            print(f"{lista['mesa']} ", end="")
        print()    
        print("-"*50)
    else:
        print("Não há mesas reservadas.")

    
    for lista in informacoes['mesas']:
        id_mesa = lista['id_da_mesa']

    quest = int(input("Qual o seu id? "))
    reserva_encontrada = False
    for i, reserva in enumerate(informacoes['mesas']):
        if reserva['id_da_mesa'] == quest:
            reserva_encontrada = True


        
            novo_nome = str(input("Qual o nome que deseja colocar?: "))
            novo_email = str(input("Qual o seu email?: "))
            novo_numero_mesa = int(input("Escolha a mesa: "))
            novo_qtde_mesa = int(input("Insira a quantidade de mesas: "))
            
            informacoes['mesas'][i] = {
            "nome": novo_nome,
            "email": novo_email,
            "mesa": novo_numero_mesa,  
            "qtde_mesas": novo_qtde_mesa,
            "id_da_mesa": id_mesa
            }   
        
            print("Mudança Concluída.")

        with open(arquivo, 'w', encoding='utf-8') as arq:
            json.dump(informacoes, arq, indent=4, ensure_ascii=False)

    if not reserva_encontrada:
        print("ID não encontrado.")   

def registrar_pedido():
    os.system('cls')
    informacoes = carregarInfo()
    listarReserva()
    mesa_encontrada = None
    mesaPedido = input("Informe o número da mesa: ")
    for mesa in informacoes["mesas"]:
        if mesa['id_da_mesa'] == mesaPedido:
            mesa_encontrada = mesa
            break
        if not mesa_encontrada:
            print("ID inválido! Insira um ID do cardápio.")
            continue
    itens_pedido = []  
    
    while True:
        visualizarCardapio()  
        comidasPedido = int(input("\nInsira o ID da comida solicitada: "))

        prato_encontrado = None 
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


def verificar_status_pedido():
    os.system('cls')
    informacoes = carregarInfo()
    print("\n==================================================")
    print("VERIFICAR STATUS DO PEDIDO")
    print("==================================================\n")
    
    if not informacoes["pedidos"]:
        print("Não há pedidos cadastrados no sistema.")
        input("\nPressione Enter para voltar...")
        return
        
    mesaPedido = input("Informe o número da mesa para ver os pedidos: ")
    
    pedidos_mesa = [pedido for pedido in informacoes["pedidos"] if pedido['mesa'] == mesaPedido]
    
    if not pedidos_mesa:
        print(f"\nNão há pedidos registrados para a mesa {mesaPedido}.")
        input("\nPressione Enter para voltar...")
        return
        
    print(f"\n📋 Status dos Pedidos - Mesa {mesaPedido}:")
    print("="*50)
    
    
    for pedido in pedidos_mesa:
        print("\nItens do Pedido:")
        print("-"*30)
        for item in pedido['itens']:
            
                
            print(f"{item['nome_prato']} - {item['status']}")
            print(f"   Quantidade: {item['quantidade']}")
            if item['observacoes']:
                print(f"   Obs: {item['observacoes']}")
            print("-"*30)
    
    input("\nPressione Enter para voltar ao menu...")                 


def removerPedidos():
    os.system('cls')
                        
    informacoes = carregarInfo()
    print("\n==================================================")
    print("CANCELAR PEDIDO .")
    print("==================================================\n")
    mesaPedido = input("Informe o número da mesa: ")
    pedidos_filtrados = [p for p in informacoes["pedidos"] if p['mesa'] == mesaPedido] 
                        
    if not pedidos_filtrados:
        print(f"Nenhum pedido encontrado para a mesa {mesaPedido}.")
        input("Pressione Enter para continuar...")
                            

    print("\nPedidos encontrados:")
    for idx, pedido in enumerate(pedidos_filtrados): 
        print(f"\nPedido #{idx + 1}")
    for item in pedido['itens']:
        print(f"- {item['nome_prato']} (x{item['quantidade']})") 

    escolha = int(input("Qual pedido deseja cancelar? (número): ")) - 1

    if 0 <= escolha < len(pedidos_filtrados):
        informacoes["pedidos"].remove(pedidos_filtrados[escolha]) 
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(informacoes, f, indent=4, ensure_ascii=False)
        print("✅ Pedido cancelado com sucesso!")
    else:
        print("Opção inválida.")
    input("\nPressione Enter para continuar...")
    pass
def listar_pedidos():
    os.system('cls')
    informacoes = carregarInfo()
    
    print("\n==================================================")
    print("LISTAGEM DE PEDIDOS")
    print("==================================================\n")
    if not informacoes["pedidos"]:
        print("Não há pedidos cadastrados no sistema.")
        input("\nPressione Enter para voltar...")
        return
    print("Filtrar por:")
    print("1 - Todos os pedidos")
    print("2 - Pedidos em preparo")
    print("3 - Pedidos prontos")
    print("4 - Pedidos entregues")
    print("5 - Voltar")
    try:
        opcao_filtro = int(input("\nEscolha o tipo de listagem: "))
    except ValueError:
        print("Opção inválida! Digite um número de 1 a 5.")
        input("\nPressione Enter para voltar...")
        return
    
    if opcao_filtro == 5:
        return
    filtro = None
    if opcao_filtro == 1:
        status_filtro = "TODOS"
    elif opcao_filtro == 2:
        status_filtro = "Em preparo"
    elif opcao_filtro == 3:
        status_filtro = "Pronto"
    elif opcao_filtro == 4:
        status_filtro = "Entregue"
    else:
        print("Opção inválida!")
        input("\nPressione Enter para voltar...")
        return

    print("\n" + "="*50)
    print(f"PEDIDOS {f'({status_filtro})' if opcao_filtro != 1 else '(TODOS)'}".center(50))
    print("="*50)
    
    pedidos_encontrados = False
    
    for pedido in informacoes["pedidos"]:
        itens_filtrados = []
        
        for item in pedido['itens']:
            if opcao_filtro == 1 or item['status'] == status_filtro:
                itens_filtrados.append(item)
        
        if itens_filtrados:
            pedidos_encontrados = True
            print(f"\n📋 Mesa: {pedido['mesa']}")
            print("-"*50)
            for item in itens_filtrados:
                if item['status'] == "Em preparo":
                    icone = "⏳"
                elif item['status'] == "Pronto":
                    icone = "✅"
                elif item['status'] == "Entregue":
                    icone = "✔️"
                else:
                    icone = "🔹"
                print(f"{icone} {item['nome_prato']} - {item['status']}")
                print(f"   Quantidade: {item['quantidade']}")
                if item['observacoes']:
                    print(f"   Obs: {item['observacoes']}")
                print("-"*30)
    
    if not pedidos_encontrados:
        print(f"\nNenhum pedido encontrado com o filtro selecionado ({status_filtro}).")
    
    input("\nPressione Enter para voltar ao menu...")

def editarPedido():
    os.system('cls') 
    informacoes = carregarInfo()
    print("\n==================================================")
    print("EDITAR PEDIDO")
    print("==================================================\n")    
    mesaPedido = input("Informe o número da mesa: ") 

    pedidos_mesa = [p for p in informacoes["pedidos"] if p['mesa'] == mesaPedido]
                        
    if not pedidos_mesa: 
        print(f"Não há pedidos registrados para a mesa {mesaPedido}.") 
    input("Pressione Enter para voltar...")
                            

    for idx, pedido in enumerate(pedidos_mesa):
        print(f"\nPedido #{idx + 1}:")
    for i, item in enumerate(pedido['itens']):
        print(f"  [{i}] {item['nome_prato']} - Status: {item['status']}")

    pedido_idx = int(input("\nQual pedido deseja editar? (número): ")) - 1
    if 0 <= pedido_idx < len(pedidos_mesa):
            itens = pedidos_mesa[pedido_idx]['itens']
            item_idx = int(input("Qual item deseja editar? (índice): "))
            if 0 <= item_idx < len(itens):
                novo_status = input("Novo status (Em preparo / Pronto / Entregue): ") 
                itens[item_idx]['status'] = novo_status 
                with open(arquivo, 'w', encoding='utf-8') as f:
                    json.dump(informacoes, f, indent=4, ensure_ascii=False)
                print("✅ Status atualizado com sucesso!") 
            else:
                                print("Item inválido.")
    else:
                            print("Pedido inválido.")
                        
    input("\nPressione Enter para continuar...")
    pass


def main():
    while True:
        
        siriCozido()
        
        menuGeral()
        
        opModulo=int(input("Escolha o Módulo Desejado: "))

        match opModulo:
            case 1:
                    print("Cardápio")
                    while True:
                        
                        menuCardapio()
                        
                        opcardapio = int(input("Escolha uma das opções: "))
                
                        if opcardapio == 1:
                            os.system('cls')
                            visualizarCardapio()
                            
                        elif opcardapio == 2:
                            os.system('cls')
                            adcionarPratos('idPrato', 'nomePrato', 'descricaoPrato', 'precoPrato')   
                            
                        elif opcardapio == 3:
                            
                            os.system('cls')
                            visualizarCardapio()
                            idPrato = str(input("Insira o Id do prato que quer editar: "))
                            try: 
                                idPrato = int(idPrato)
                            except ValueError:
                                print("VALOR INVÁLIDO")
                                                       
                            novoNomePrato = str(input("Insira o novo nome do prato: ")).title()
                            
                            novoDescPrato = str(input("Insira a nova descrição do prato: ")).lower()

                            novoPrecoPrato = str(input("Insira o novo preço do prato: "))                           
                            try: 
                                novoPrecoPrato = float(novoPrecoPrato)
                            except ValueError:
                                print("VALOR INVÁLIDO (ex: 19.99)")
                            
                            editarPrato(idPrato,novoNomePrato,novoDescPrato,novoPrecoPrato,)
                            
                        elif opcardapio == 4:
                            
                            os.system('cls')
                            deletarPrato()
                            
                        elif opcardapio == 5:

                            print("Saindo para o menu principal...")
                            sleep(3)
                            break
                        else:
                            print("Opção inválida.")
                            


            case 2:
                 while True:
                    menuReserva()
                    op_mesa = int(input("Insira a opção desejada:"))
                    
                    if op_mesa == 1: 
                        adicionarReserva()
                        
                    elif op_mesa == 2:
                        removerReserva()
                    
                    elif op_mesa == 3:
                        listarReserva()
                    
                    elif op_mesa == 4:
                        editarReserva()
                        
                    elif op_mesa == 5:
                        print("Saindo...")
                        sleep(3)
                        break
                    else:
                        print("Erro, escolha uma opção válida.")
     
            case 3:
                while True:
                    os.system('cls')
                    print("\n==================================================")
                    print("PEDIDOS")
                    print("==================================================\n")
                    menuPedidos()
                    opPedidos = int(input("Informe a opção que deseja: "))

                    if opPedidos == 1:
                        registrar_pedido()

                    elif opPedidos == 2:
                        removerPedidos()

                    elif opPedidos == 3:
                        editarPedido()
                        

                    elif opPedidos == 4:
                        listar_pedidos()

                    elif opPedidos == 5:
                        verificar_status_pedido()
                    elif opPedidos == 6:
                        print("Saindo...")
                        sleep(3)
                        break 
                       
                       

                
            case 4:
                    print("Saindo...")
                    sleep(3)
                    print("Volte sempre!")
                    break

if __name__ == "__main__":
    main()
        