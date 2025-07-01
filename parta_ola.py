#Themistokleia Siakavara, A.M. 4786

players= int(input("Please input number of players: "))
beans= int(input ("Please input number of beans per player: "))

import random
#random turn of a player in the beginning of the game
turn= random.randint(1, players)

Roulette = ['Put one', 'Put two', 'Everyone puts one', 'Take one', 'Take two', 'Take them all']
pot= players
rounds =1

person = range(1, players +1)

#list of the beans, depend on the number of players
prize = players * [beans]
    
allplayers= list(person)

#function: beginning of every round. everyone -1 bean and pot +(players) bean        

def begin(rounds, prize, players):
    print('-' *100)
    for i in range(len(prize)):
        prize[i] -=1
    print('Round', rounds, 'begins: everyone puts 1')
            
def output(pot, prize):
    print('Current state: \nPot: ', pot)
    for j in range(len(prize)):
        if prize[j]>0 or prize[j]==0:
            print('Player', j+1, '\'s budget: ', prize[j])
        else:
            print('Player', j+1, 'is eliminated')

def partaola(rounds,pot,players,beans,prize):
    begin(rounds, prize, players)
    output(pot, prize)
    while len(allplayers)>1:
        for i in range(0, players):
            if pot>0:
                if i+1 in allplayers:
                    spin = random.choice(Roulette)
                    print('\nPlayer', i+1, 'spinned', spin)
                    if spin == Roulette[0]:
                        if prize[i]!=0:
                            pot= pot+1
                            prize[i]= prize[i] -1
                            output(pot, prize)
                        elif prize[i]==0:
                            allplayers.remove(i+1)
                            prize[i]= prize[i] -1
                            output(pot, prize)
                            if len(allplayers)==1:
                                break
                    if spin ==Roulette[1]:
                        if prize[i]==2 or prize[i]>2:
                            pot= pot +2
                            prize[i]= prize[i] -2
                        elif prize[i]<2:
                            if prize[i]==1:
                                pot = pot+1
                                prize[i]= prize[i]-2
                                allplayers.remove(i+1)
                            elif prize[i]==0:
                                prize[i]=-2
                                allplayers.remove(i+1)
                        output(pot, prize)
                        if len(allplayers)==1:
                            break
                    if spin == Roulette[2]:
                        for k in range(0, players):
                            if prize[k]>0:
                                prize[k] = prize[k]-1
                                pot= pot+1
                            elif prize[k]==0:
                                allplayers.remove(k+1)
                                prize[k] = prize[k] -1
                        output(pot, prize)
                        if len(allplayers)==1:
                            break
                    if spin == Roulette[3]:
                        pot= pot-1
                        prize[i]= prize[i] + 1
                        output(pot, prize)
                    if spin== Roulette[4]:
                        if pot>1:
                            pot= pot -2
                            prize[i]= prize[i]+2
                            output(pot, prize)
                        elif pot==1:
                            pot=0
                            prize[i] = prize[i]+1
                            output(pot,prize)
                    if spin== Roulette[5]:
                        prize[i]= prize[i]+ pot
                        pot=0
                        for k in range(0,players):
                            if prize[k]==0:
                                allplayers.remove(k+1)
                        output(pot,prize)
                        print('\nPot is zero: round ends')
                        if len(allplayers)==1:
                            break
                        rounds+= 1
                        begin(rounds, prize, players)
                        pot= len(allplayers)
                        output(pot, prize)
                else:
                    continue
            else:
                print('\nPot is zero: round ends')
                rounds+= 1
                begin(rounds, prize,players)
                pot=len(allplayers)
                output(pot, prize)

partaola(rounds,pot,players,beans,prize)
print('\nGame finished: Player' , allplayers[0] , 'wins')