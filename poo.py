from Teste import deposita,saca,extrato,cria_conta

x214079 = cria_conta(321, "Amanda", 3000, 10000)

print("Agencia: ",x214079["Agencia"])

extrato(x214079)

saca(x214079,500)

extrato(x214079)

deposita(x214079,150)

extrato(x214079)