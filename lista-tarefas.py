import os
import time

tarefas = []

xp = 0

def apagar():
    time.sleep(1.5)
    os.system("clear")

def adicionar():
     global tarefas
     add = input("Adicione uma nova tarefa:  ")
     if add in tarefas:
        print("Esse item já existi !")
     else:
      tarefas.append(add)
      print(f"Tarefa {add} Foi adicionada !!! ")
      apagar()

def remover():
    mostrar()
    global tarefas
    remover = input("Qual tarefa deseja remover ?:  ")
    if remover in tarefas:
     tarefas.remove(remover)
     print("Tarefa removida")
    else:
        print("Digite uma tarefa existente !")
    apagar()

def feito():
    mostrar()
    global tarefas
    global xp
    try:
        marcar = int(input("Digite o numero do item correspodente para marcar: "))
        tarefas.pop(marcar)
        print("Tarefa feita !")
        xp += 25
        print(f"Você recebeu {xp} de xp !")
    except IndexError:
        print("Esse Item não existi !")
    apagar()

def mostrar():
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
    global xp
    print(f"Você possui {xp} de xp !")
    apagar()

def sair():
    print("---- Sair ----")
    print("""
1 - sair
2 - ficar    
    """)
    sair = int(input("Nesta versão não possui salvamento !, Deseja sair mesmo assim ?:  "))
    if sair == 1:
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