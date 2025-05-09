#Importando o json e o sistema operacional
import json
import os
from time import sleep
os.system('cls')

#Definindo o caminho do arquivo
arquivo = os.path.join(os.path.dirname(__file__), 'info.json')

def carregarInfo():
    #Verifica se o arquivo existe, se não existir, cria o arquivo com uma lista vazia
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)
            #lalalalala
    #carrega o conteúdo
    with open(arquivo, 'r') as f:   
        return json.load(f)
    
#adcionar informações ao json
def adcionarInfo(info1, info2):
    informacoes = carregarInfo()

    informacoes.append({'info1': info1, 'info2': info2})

#confirma que a informação foi adicionada
    with open(arquivo, 'w') as f:
        json.dump(informacoes, f, indent=4, ensure_ascii=False)
    print("Informação adicionada com sucesso!")

#lista as informações
def listarInfo():
    informacoes = carregarInfo()

    if informacoes:
        print("=" *50)
        print("LISTA DE INFORMAÇÕES ADICIONADAS")
        print("-" *50)
        for informacao in informacoes:
            print(f"INFO 1: {informacao['info1']} INFO 2: {informacao['info2']}")

    else:
        print("Nennhuma informação foi adcionada anteriormente. :(")
        
#atualizar informação:
def atualizarInfo(info1_antiga, info1_nova, info2_nova):
    informacoes = carregarInfo()

    for informacao in informacoes:
        if informacao['info1'] == info1_antiga:
            informacao['info1'] = info1_nova
            informacao['info2'] = info2_nova
            break

    with open(arquivo, 'w') as f:
        json.dump(informacoes, f, indent=4, ensure_ascii=False)
    print("INFORMAÇÕES ATUALIZADAS COM SUCESSO!")

#excluir informações
def excluirInfo(info1):
    informacoes = carregarInfo()

    for informacao in informacoes:
        if informacao['info1'] == info1:
            informacoes.remove(informacao)
    with open(arquivo, 'w') as f:
        json.dump(informacoes, f, indent=4, ensure_ascii=False)
    print("INFORMAÇÃO EXLCUIDA COM SUCESSO!")

#pesquisar informações
def pesquisarInfo(info1):
    informacoes = carregarInfo()

    encontrado = False

    for informacao in informacoes:
        if informacao['info1'] == info1:
            print(f"INFO 1: {informacao['info1']} INFO 2:{informacao['info2']}")
            encontrado = True
        if not encontrado:
            print("Informação1 não encontrada")

#menu
def menu():
    print("MENUUUUUUUUUU")
    print("1-Adcionar informações")
    print("2-Listar informações")
    print("3-Atualizar informações")
    print("4-Remover informações")
    print("5-Buscar informações")
    print("6-Voltar ao menu anterior")
#funcionamento do software:
def main():
    while True:
        #menu inicial
        print("BEM VINDO")
        print("1-MODULO INICIAL (escolha esse, só tem esse e apenas esse.)")
        print("2-Sair")
        op_inicial = int(input("QUAL MODULO DESEJAS UTILIZAR?"))
        match op_inicial:
            case 1:
                while True: 
                    menu()#Menu principal
                    op = int(input("Escolha uma opção--->"))
                    if(op == 1):
                        #Adição 
                        info1 = input("Insira a informação 1 (COMPARAVEL A UM NOME) ").lower()
                        info2 = input("Insira a informação 2 (COMPARAVEL A IDADE) ").lower()
                        adcionarInfo(info1, info2)
                    elif(op == 2):
                        #Listagem
                        os.system('cls')
                        listarInfo()
                    elif(op ==  3):
                        #Edição
                        info1_antiga = input("Qual informação deseja alterar? ").lower()
                        info1_nova = input("Insira os dados a serem atualizados. ").lower()
                        info2_nova = input("Insira a informação 2 que deseja atualizar. ").lower()
                        atualizarInfo(info1_antiga, info1_nova, info2_nova)
                    elif(op == 4):
                        #Exclusão
                        info1 = input("Insira a informação que deseja excluir ").lower()
                        excluirInfo(info1)
                    elif(op == 5):
                        #Pesquisa
                        info1 = input("Insira o a informação que deseja buscar ").lower()
                        pesquisarInfo(info1)
                    elif(op == 6):
                        #Sair
                        os.system('cls')
                        print("Voltando para o menu inicial...")
                        sleep(3)
                        break
                    else:
                        print("Opção inválida.")
            case 2:     #Finalizar o 
                print("SAINDO...")
                sleep(3)
                break
            case __:
                print("OPÇÃO INVÁLIDA.")

#Roda o Software
if __name__ == "__main__":
    main()