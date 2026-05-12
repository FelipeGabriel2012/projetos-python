import sqlite3
import random
import os
import time
logar = False

banco = sqlite3.connect('banco_lista.db')
cursor = banco.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Pessoas (
                  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                  titular TEXT NOT NULL,
                  saldo INTEGER NOT NULL,
                  senha TEXT NOT NULL)
""")
banco.commit()

def tempo():
    time.sleep(1.5)  
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
class Pessoa:
 def __init__(self,titular,saldo,senha):
        self.senha = senha
        self.titular = titular
        self.saldo = saldo
 def menu(self):
    while True:
     print(f"""
     {'_' * 12}
     --BANCO--    
      1.Adicionar
      2.Remover
      3.Saldo
      4.Sair
     {'_' * 12}
      """)
     try:
      esc = int(input("Escolha uma opção: "))
     except ValueError:
        print("Escolha uma opção valida !")
        continue
     match esc:
       case 1:
        self.add()
       case 2:
        self.remover()
       case 3:
        self.ver_saldo()
       case 4:
        break

 def add(self):
  try:
   titular = input("Digite seu nome: ")
   senha = input("Digite Sua Senha: ")
   saldo = random.randint(1,1000) 
   pessoa = Pessoa(titular,saldo,senha)
   cursor.execute("INSERT INTO Pessoas (titular,saldo,senha) VALUES(?,?,?)",(pessoa.titular,pessoa.saldo,pessoa.senha))
   banco.commit()
   print(f"{titular} foi adicionado !")
  except ValueError:
    print("Ocorreu um erro !")
  finally:
    tempo()  

 def ver_saldo(self):
    print(f"""----SALDO----
Nome:{self.titular}
R$:{self.saldo}
    """)
    tempo()
 def sair(self):
    exit()
 def remover(self):
   try:
    nome = input("Digite o nome de sua conta: ")
    senha = input("Digite a senha: ")    
    cursor.execute("SELECT * FROM Pessoas WHERE titular = ? AND senha = ?",(nome,senha))
    usuarioR = cursor.fetchone()
    if usuarioR:
     cursor.execute("DELETE FROM Pessoas WHERE titular = ? AND senha = ?",(nome,senha))
     print(f"Conta {usuarioR[1]} Foi Removida !")
     banco.commit()
   except ValueError:
    print("Erro")
   finally:
    tempo()  
 def entrar(self):
    print("""----ENTRAR----
1.logar
2.Cadastrar    
3.Sair
""")
    esc_entrar = int(input("Escolha uma opção: "))
    match esc_entrar:
        case 1:
            self.logar()
        case 2:
            self.add()
        case 3:
            self.sair() 
 def logar(self):
   try:
    nome = input("Digite o nome de sua conta: ")
    senha = input("Digite a senha: ")
    cursor.execute("SELECT * FROM Pessoas WHERE titular = ? AND senha = ? ",(nome,senha))
    
    usuario = cursor.fetchone()

    if usuario:
        self.titular = usuario[1]
        self.saldo = usuario[2]
        self.senha = usuario[3]
        print(f"Olá {usuario[1]}")
        self.menu()
        return True
    else:
        print("Acesso Negado")
        return False
   except ValueError:
    print("Algo deu Errado")
   finally:
    tempo()  
pessoa = Pessoa("",0,"")

while True:
    pessoa.entrar()
