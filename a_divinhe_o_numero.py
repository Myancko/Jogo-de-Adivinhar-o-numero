import random
import os
from sys import exit

while True:

    os.system('cls')

    tentativas = int(0)
    adivinhaçoes = int(0)

    loop = True
    print("Yo me diz o teu nome:\n")
    while  loop == True:

        try:
            Jogador = str(input(">>>  "))
            Jogador = Jogador[0].upper() + Jogador[1:].lower()
            loop = False

        except:
            loop == True
            os.system('cls')
            print('Erro ao ler o nome digitado!')
            print("\nQual o seu nome?\n")

    os.system('cls')
    print("Oi " + Jogador + " Vamos jogar um jogo valendo um biscoito (＾▽＾)\n\n",end='')
    print("Eu vou pensar em um numero de 0 a 24, e voce tenta adivinhar qual é\n",end=''
    "simplis não? vamos lá!\n")

    resultado = random.randint(0,24)

    print("\nJa pensei no numero!\n", end=''
    "agora tente adivinhar qual numero foi\n")
    
    while tentativas < 6:

        try:
            adivinhaçoes = int(input(">>> "))
        except:
            adivinhaçoes = -1

        if adivinhaçoes ==  resultado:
            os.system('cls')
            print(' ヽ(ˇヘˇ)ノ Parabens '+ Jogador +' você acertou ┐( ˘ ､ ˘ )┌ \n\n' +
            'Espero que esteja feliz.\n')
            break
            
        if tentativas == 5:
            os.system('cls')
            print("È adivinha quem perdeu...\n"+
            '\nVocê.'+
            '\nEspero que voce esteja pronto para ficar sem biscoito :('+
            '\n\n<<< (づ｡◕‿‿◕｡)づ E  S E M  A  A L M A  T A M B E M ＼(^ω^＼) >>>\n')
            input("O que voce acha disso " + Jogador + '? alias o numero era ' + 
            str(resultado)  + ".\n>>>  ")
            print('HA' * 1000000)
            os.system('cls')
            break

        elif adivinhaçoes == -1:
            print("Não sei o que você digitou, mais sei que voce digitou errado\n" +
            'Digite novamente')
            tentativas +=  1

        elif adivinhaçoes > resultado:
            print("Noup voce errou!\n", end=''
            'Porque voce não tenta novamente?' +
            '\nQuem sabe um numero menor dessa vez!')
            tentativas  += 1

        elif adivinhaçoes  < resultado:
            print("Noup voce errou\nQue peninha porque voce não tenta de novo?" +
            '\nQuem sabe um numero maior dessa vez!')
            tentativas += 1

    print("O B R I G A D O  P O R  J O G A R\n\n" + 
    'Deseja jogar novamente[S][N]?')

    loop_final  = str(input('>>>  ')).upper()
    if loop_final ==  'S':
        continue
    
    else:
        os.system('cls')
        exit()