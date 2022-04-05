import gspread

gc = gspread.service_account(filename='')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1iFb09TFXuPy2vSJ1n7RF1A7X_0F5crNUXrPj1vkFnrc/edit#gid=0')
dado = sh.worksheet('Página1')

def menu():
    print(f'1- Para iniciar o cadastro\n2- Sair')

def adicionar():
    nome = input("Digite seu nome")
    idade = input("Digite sua idade")
    matricula = input("Digite sua matricula")
    return [nome, idade, matricula]

while True:
    menu()
    entrada = int(input())
    if entrada == 2:
        print('ate a proxima')
        break
    if entrada == 1:
        user = adicionar()
        dado.append_row(user)
    else:
        print("Numero digitado invalido")