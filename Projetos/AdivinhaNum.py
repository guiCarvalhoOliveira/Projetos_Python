from random import randint # impota random

numero_certo = randint(1,100) #sorteia um numero de 1 a 100

print(f"Bem vindo ao jogo de adivinhação de número!")
print(f"O jogo consiste em acertar um número entre 1 e 100, dando dicas ao longo da 'gameplay'") #Introduz jogo e regras

palpite = (int(input(("Faça seu palpite: ")))) # Inicia palpite
tentativas= 1 # começa contagem de tentativas feitas

while palpite != numero_certo: # Enquanto o palpite for diferente do numero sorteado...
        
# Nesse 'if' verifica se o palpite se encaixa na regra entre 1 e 100 e sobrepõe o palpite inicial pelo que tentou posteriormente
        if palpite > 100 or palpite <= 0:
            print(f"Seu palpite |{palpite}| deve ser entre 1 e 100") 
            palpite = int(input("Tente novamente: "))
# Nesse 'if' verifica se o palpite é maior que o numero sorteado e sobrepõe o palpite anterior pelo novo palpite e adiciona a contagem de tentativas
        elif palpite > numero_certo:
            print(f"Seu palpite |{palpite}| foi MAIOR que o numero certo!")
            palpite = int(input("Tente novamente: ")) 
            tentativas = tentativas + 1
# Nesse 'if' verifica se o palpite é menor que o numero sorteado e sobrepõe o palpite anterior pelo novo palpite e adiciona a contagem de tentativas
        elif palpite < numero_certo:
            print(f"Seu palpite |{palpite}| foi MENOR que o numero certo!") 
            palpite = int(input("Tente novamente: ")) 
            tentativas = tentativas + 1
        
# Nesse 'if' verifica se a quantidade de tentativas é uma ou varias, e ajusta texto conforme valor
if tentativas > 1:
    print((f"Você Acertou o número correto ({numero_certo}) em {tentativas} tentativas!")) 
else:
     print((f"Você Acertou o número correto ({numero_certo}) em {tentativas} tentativa!"))