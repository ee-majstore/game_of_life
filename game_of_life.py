import time
import os
import random
import copy

##########################################

n_polja         = 10
poljana         = []
susedi          = []

putanja = [
    [-1, -1], 
    [-1,  0],
    [-1,  1],
    [ 0, -1],
    [ 0,  1],
    [ 1, -1],
    [ 1,  0],
    [ 1,  1]
]

###########################################

def okruzi(i, j, t):
        dopustiv = [True for _ in range(8)]
        if i == 0:
            dopustiv[0] = False 
            dopustiv[1] = False 
            dopustiv[2] = False 
        if i == n - 1:
            dopustiv[5] = False
            dopustiv[6] = False
            dopustiv[7] = False
        if j == 0:
            dopustiv[0] = False
            dopustiv[3] = False
            dopustiv[5] = False
        if j == n - 1:
            dopustiv[2] = False
            dopustiv[4] = False
            dopustiv[7] = False

        for x, ap in enumerate(dopustiv):
            if ap :
                if t:
                    # povecaj
                    susedi[putanja[x][0] + i][putanja[x][1] + j] += 1
                else:  
                    # smanji
                    susedi[putanja[x][0] + i][putanja[x][1] + j] -= 1

def ubaci(i, j):
    t = False
    while not t:
        #i = int(input("unesite koordinatu 1: "))
        #j = int(input("unesite koordinatu 2: "))
        if poljana[i][j] == False:
            poljana[i][j] = True
            okruzi(i, j, True)
            t = True

def ispisi():
    for red in poljana:
        for polje in red:
            if polje:
                print("@", end = " ")
            else:
                print(" ", end = " ")
        print()

#    for red in susedi:
#        for polje in red:
#            print(polje, end = " ")
#        print()
#    print("-----------------")

def updejt():
    pom_poljana = copy.deepcopy(poljana)
    pom_susedi  = copy.deepcopy(susedi)
    for i, red in enumerate(pom_poljana):
            for j, polje in enumerate(red):
                if (polje == False) and (pom_susedi[i][j] == 3):
                    poljana[i][j] = True
                    okruzi(i, j, True)
                if (polje == True) and (not ((pom_susedi[i][j] == 2) or (pom_susedi[i][j] == 3))):
                    poljana[i][j] = False
                    okruzi(i, j, False)

def randomizuj(k):
    possible_coordinates = [(x, y) for x in range(n) for y in range(1, n)]
    bomb_coordinates = random.sample(possible_coordinates, k)
    print(bomb_coordinates)

    for cord in bomb_coordinates:
        poljana[cord[0]][cord[1]] = True
        okruzi(cord[0], cord[1], True)


###################################################

os.system("clear")
n = int(input("velicina matrice: "))
susedi  = [[0 for _ in range(n)] for _ in range(n)]
poljana = [[False for _ in range(n)] for _ in range(n)]

x = int(input("broj zivih: "))
randomizuj(x)

#for i in range(0, 40, 10):
#    ubaci(i + 1, 0)
#    ubaci(i + 2, 1)
#    ubaci(i + 0, 2)
#    ubaci(i + 1, 2)
#    ubaci(i + 2, 2)

s = 0
while s < 60:
    os.system("clear")
    ispisi()
    updejt()
    time.sleep(1/60)
    s += 1/60
    
