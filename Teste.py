def cria_conta(numero, titular, saldo, limite):
    conta = {"Agencia": numero, "Titular": titular, "Saldo": saldo, "Limite": limite}
    return conta

def deposita(conta, valor):
    conta["Saldo"] += valor

def saca(conta, valor):
    conta["Saldo"] -= valor

def extrato(conta):
    print("O saldo atual é {}".format(conta["Saldo"]))