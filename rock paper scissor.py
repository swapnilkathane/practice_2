print(' Welcome to SPL-GAMING Arena ')
S="scissors"
R='rock'
P='paper'
#print(S)
P1=input('Player one : ')
P2=input('Player second : ')
if(P1==S or P1==R or P1==P):
    if P1==S and P2==P:
        print('Player one win')
    if(P1==S and P2==R):
        print('player two win')
    if(P1==S and P2==S):
        print('Opps draw')
    if(P1==P and P2==P):
        print('Opps Draw')
    if(P1==P and P2==R):
        print('player one win')
    if(P1==P and P2==S):
        print('Playr two win')
    if (P1==R and P2==P):
        print('Player two win')
    if (P1==R and P2==R):
        print('opps draw')
    if (P1==R and P2==S):
        print('Player one win')
else:
    print('Check spelling')

