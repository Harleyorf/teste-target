num= int(input("Informe um número para verificar se pertencia a sequência de Fibonacci: ")) #solicita o numero ao usuario 

#inicializando a variaveis como dois primeiros numeros da sequencia
n1 = 0
n2 = 1
pertence = False #variavel de controle para saber se pertence ou nao

#verifica se o numero informador pertence a sequencia
while n1 <= num:

    if n1 == num:
        pertence = True
        break

    temp = n1

    n1 = n2

    n2 = temp + n2
    
#mostra o resultado desejado
if pertence:
    print(f"O número {num}, pertence à sequência de Fibonacci.")
else:
    print(f"O número {num}, não pertence à sequência de Fibonacci.")