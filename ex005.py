#criando funcao para inverter qualquer string
def inverter(txt): 
    return txt[::-1]

texto = str(input("Digite uma palava ou texto para ser invertido: "))
print(inverter(texto))