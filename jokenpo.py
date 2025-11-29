from random import randint
from time import sleep

print('JOKENPÔ' .center(40, '-'))

#Usuário
escolhaUsuario = int(input('''Opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA

Sua escolha: '''))

#Máquina
escolhaMaquina = randint(1, 3)

#Processamento
print('-=' *11)
print('JO')
sleep(1)    
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 11)

#Resultado
if escolhaUsuario == 1: #Usuário escolheu PEDRA
    print('Você escolheu PEDRA.')
    if escolhaMaquina == 1:
        print('A máquina escolheu PEDRA.')
        print('EMPATE!')
    elif escolhaMaquina == 2:
        print('A máquina escolheu PAPEL.')
        print('VOCÊ PERDEU!')
    else:
        print('A máquina escolheu TESOURA.')
        print('VOCÊ VENCEU!')
elif escolhaUsuario == 2:   #Usuário escolheu PAPEL
    print('Você escolheu PAPEL.')
    if escolhaMaquina == 1:
        print('A máquina escolheu PEDRA.')
        print('VOCÊ VENCEU!')
    elif escolhaMaquina == 2:
        print('A máquina escolheu PAPEL.')
        print('EMPATE!')
    else:
        print('A máquina escolheu TESOURA.')
        print('VOCÊ PERDEU!')
elif escolhaUsuario == 3: ##Usuário escolheu TESOURA
    print('Você escolheu TESOURA.')
    if escolhaMaquina == 1:
        print('A máquina escolheu PEDRA.')
        print('VOCÊ PERDEU!')
    elif escolhaMaquina == 2:
        print('A máquina escolheu PAPEL.')
        print('VOCÊ VENCEU!')
    else:
        print('A máquina escolheu TESOURA.')
        print('EMPATE!')
else:
    print('Opção inválida. Tente novamente.')