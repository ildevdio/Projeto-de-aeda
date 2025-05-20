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
        with open(arquivo, 'w') as f:
            json.dump(dados_iniciais, f, indent=4)
            
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
    print("  | 🦀Restaurante🦀 |  ")
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
    print("  1 - Adicionar Pedido    ")
    print("  2 - Cancelar Pedido   ")
    print("  3 - Editar Pedido           ")
    print("  4 - Listar Pedidos          ")
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
    print("  2 - dev              ")
    print("  3 - Pedidos              ")
    print("  4 - Sair             ")
    print("                       ")
    print("=======================")
    

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
                            

                        
                        elif opcardapio == 2: #adcionar prato
                            os.system('cls')
                            adcionarPratos('idPrato', 'nomePrato', 'descricaoPrato', 'precoPrato')   
                            break
                        
                        elif opcardapio == 3: #Editar
                            
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
                    lorem = 1
                    break
                
            case 3:  # CRUD 3
                while True:
                    os.system('cls')
                    print("\n==================================================")
                    print("PEDIDOS")
                    print("==================================================\n")
                    menuPedidos()
                    opPedidos = int(input("Informe a opção que deseja: "))  # Corrigido o parêntese

                    if opPedidos == 1:
                        os.system('cls')
                        # Mostrar todos os comidas do cardápio
                        comidasPedido = int(input("Insira o id da comida solicitada: "))  # Corrigido o parêntese
                        mesaPedido = input("Informe a mesa do Pedido: ")
                        obsPedido = input("Informe as observações do pedido: ")

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
                        # Pedir a mesa, depois puxar todos os pedidos da mesa e perguntar qual pedido quer conferir o status
                        pass

                    elif opPedidos == 6:
                        # Opção 6 (adicionar lógica aqui)
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
        