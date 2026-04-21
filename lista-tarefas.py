import json
import os
import time

def salvar():
    dados = {
        "xp":xp,
        "tarefas":tarefas
    }

    with open("dados.json", "w", encoding="utf-8") as f:
     json.dump(dados, f, ensure_ascii=False, indent=4)

def carregar():
    try:
     with open("dados.json", "r", encoding="utf-8") as f:
        return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "xp": 0,
            "tarefas": []
        }

dados = carregar()

xp = dados["xp"]
tarefas = dados["tarefas"]

def apagar():
    time.sleep(1.5)
    os.system("clear")

def adicionar():
     os.system("clear")
     global tarefas
     if tarefas:
        mostrar()
     add = input("Adicione uma nova tarefa:  ")
     if add in tarefas:
        print("Esse item já existi !")
    
     else:
      tarefas.append(add)
      print(f"Tarefa {add} Foi adicionada !!! ")
     apagar()

def remover():
    os.system("clear")
    global tarefas
    if not tarefas:
        print("você ainda não adicionou uma tarefa !")
    else:
     mostrar()
     remover = input("Qual tarefa deseja remover ?:  ")
     if remover in tarefas:
      tarefas.remove(remover)
      print("Tarefa removida")
      apagar()
     else:
        print("Digite uma tarefa existente !")
    apagar()

def feito():
    os.system("clear")
    global tarefas
    global xp
    try:
        if not tarefas:
            print("Você não possui tarefas !")
        else:
         mostrar()   
         marcar = int(input("Digite o numero do item correspodente para marcar: "))
         tarefas.pop(marcar)
         print("Tarefa feita !")
         xp += 25
         print(f"Você recebeu 25 de xp !")
    except IndexError:
        print("Esse Item não existi !")
    apagar()

def mostrar():
    os.system("clear")
    global tarefas
    quantidade = 0
    if not tarefas:
        print("Sem Tarefas !")
    else:
      for item in tarefas:
        print(f"{quantidade}. {item}")
        quantidade += 1
    apagar()

def mostar_xp():
    os.system("clear")
    global xp
    print(f"Você possui {xp} de xp !")
    apagar()

def sair():
    print("---- Sair ----")
    print("""
1 - sair
2 - ficar    
    """)
    sair = int(input("Deseja Sair ?: "))
    if sair == 1:
        salvar()
        print("Saiando ....")
        time.sleep(0.5)
        exit()
    if sair == 2:
        opcoes()

def opcoes():
    print("---- LISTA DE TAREFAS ----")

    print("""
1 -  Adicionar tarefas 
2 -  Remover tarefas
3 -  Mostrar tarefas    
4 -  Marcar tarefa como feito
5 -  Mostrar XP
6 -  Sair
    """)
    try:
     esc = int(input("Escolha uma opção:  "))
     match esc:
        case 1:
            adicionar()
        case 2:
            remover()
        case 3:
            mostrar()
        case 4:
            feito()
        case 5:
            mostar_xp()
        case 6:
            sair()

    except ValueError:
        print("Digite uma opção válida !")
        apagar()
while True:
    opcoes()
