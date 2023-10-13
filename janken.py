'''
Created on 2023/10/13

@author: t21cs022
'''
import random

a = random.randint(0, 2)
b = random.randint(0, 2)

print("A = ", a, "B = ", b)

if a == b:
    print("引き分け")    
elif (a==0 and b==1)or(a==1 and b==2)or(a==2 and b==0):
    print("Aの勝ち")    
elif (a==0 and b==2)or(a==1 and b==0)or(a==2 and b==1):
    print("Bの勝ち")

