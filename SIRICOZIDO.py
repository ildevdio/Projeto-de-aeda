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
            "garcons" : []
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

def menuGeral():
    print("                       ")
    print("=======================")
    print("                       ")
    print("     | Módulos |       ")
    print("                       ")
    print("  1 - Cardápio         ")
    print("  2 - dev              ")
    print("  3 - dev              ")
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
                while True:
                    print("Cardápio")
                    while True:
                        
                        menuCardapio()
                        
                        opcardapio = int(input("Escolha uma das opções: "))
                
                        if opcardapio == 1: #ver cardápio
                            os.system('cls')
                            visualizarCardapio()
                            

                        
                        if opcardapio == 2: #adcionar prato
                            os.system('cls')
                            adcionarPratos('idPrato', 'nomePrato', 'descricaoPrato', 'precoPrato')   
                            break
                        
                        if opcardapio == 3: #Editar
                            
                            print("em dev")
                            break
                        
                        if opcardapio == 4: #Excluir
                            
                            print("em dev")
                            break
                        if opcardapio == 5: #Sair

                            print("Saindo para o menu principal...")
                            sleep(3)
                            break


            case 2: #Crud 2
                    lorem = 1
                    break
                
            case 3: #Crud 3
                    lorem = 2
                    break
                
            case 4:
                    print("Saindo...")
                    sleep(3)
                    print("Volte sempre!")
                    break

if __name__ == "__main__":
    main()
        