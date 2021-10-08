#Esse codigo deve testar senhas até descobrir qual é
from os import system 
from os import name
system('cls' if name == 'nt' else 'clear')

pre_senha = 'carroça321'
pre_senha_nmr = 2531
chaves = {
    1 : 'carro123',
    2 : 'moto123',
    3 : 'cachorro123',
    4 : 'modekaifoda',
    5 : 'anavoltapramim',
    5.5 : 'novaera',
    6 : 'carroça321'
}

print('''
_________|||
________|___|
_________|||
_________|_|
_________|_|
_______|||_||\
_____||__|||__||\            
___||__|||||||___\            
__|_______________|
_|_________________|
_|_________________|             +==========================================+
_|_____|||||||||||||||           |      Brute force usando Python           |
_|____|_______________|          +==========================================+
_|____|___|||||||||||||          | ♚ Coded: Link                            |
_|___|___|___________|||         | ♚ Contact: @Rei_Covid19        (Telegram)|
_|___|___|_|||___|||__||         | ♚ Date: 07/03/2017                       |
_|___|___|_|||___|||__||         | ♚ I take no responsibilities for the     |
_|___|___|___________|||         |   use of this program !                  |
_|____|___|||||||||||||          +==========================================+
_|_____||||||||||||||            |          Grupo de uns corno              |
_|_________________|             +==========================================+
_|____||||||||||||||
_|___|__|__|__|__|                  ESCOLHA UMA OPÇÃO:       
_|__||||||||||||||                  [1] SENHAS PRE-ESCOLHIDAS       
_|__|___|__|__|__|                  [2] SENHA DE NUMEROS       
_|___|||||||||||||||                [3] SENHAS GERADAS
|||_________________|||
''')
try:
    pergunta = input('OPÇÃO: ')
    if pergunta > 3 or pergunta < 1:
        print('\nDIGITE APENAS NUMERO ENTRE 1 E 3')
        False
except:
    print('\nDIGITE APENAS NUMEROS')
def testarchaves(senhas):
    for io in senhas:
        if senhas.get(io) == pre_senha:
            print('achei a senha {}'.format(senhas.get(io)))
            break
        else:
            print('foi testada a senha {}'.format(senhas.get(io)))

def testarnumeros(qntd = 4):
    comeco = qntd * '0'
    comeco = int(comeco)
    while len(str(comeco) > len(str())):
        if comeco == pre_senha_nmr:
            print('achamos a senha {}'.format(comeco))
        else:
            print('testamos a senha {}'.format(comeco))
            comeco += 1
def testargen():
    pass
if pergunta == '1':
    testarchaves(chaves)
elif pergunta == '2':
    testarnumeros()
elif pergunta == '3':
    testargen()