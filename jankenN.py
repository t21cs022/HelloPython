'''
Created on 2023/10/13

@author: t21cs022
'''
import random

num_player = 3

choice = []
for i in range(num_player):
    x = random.randint(0, 2)
    choice.append(x)
    print("player", i, "=", x)

a=0; b=0; c=0;
for i in range(num_player):
    if choice[i]==0:
        a+=1
    elif choice[i]==1:
        b+=1
    elif choice[i]==2:
        c+=1
    

    
if a == b:
    print("引き分け")    
elif (a==0 and b==1)or(a==1 and b==2)or(a==2 and b==0):
    print("Aの勝ち")    
elif (a==0 and b==2)or(a==1 and b==0)or(a==2 and b==1):
    print("Bの勝ち")

