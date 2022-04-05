import gspread
import psycopg2

conn = psycopg2.connect(database="postgres", user="", password="", host="")

gc = gspread.service_account(filename='')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1U1XDkHXGwVWOR78kJbSO82je6w4ooM94VSMuJiGymVc/edit#gid=0')
dado = sh.worksheet('Página1')

dicionario = {}

for i in range(5, 22+1):
    chave = dado.acell(f"F{i}").value
    valor = float(dado.acell(f"H{i}").value[3:].replace(",", "."))
    if chave not in dicionario:
        dicionario[chave] = []
        dicionario[chave].append(valor)
    else:
        dicionario[chave].append(valor)
print(dicionario)
for k, v in dicionario.items():
    print(f"O vendedor {k} teve uma media de comissao de R$ {sum(v)/len(v):.2f}")

print(dicionario)
