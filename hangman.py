print('\n')
print(
''' THE RULES OF THE GAME :
 #1 A word and its clue will be provided,the player must guess the word within 5 tries
 #2 To access the clue, enter 'clue'
 #3 Use only lowercase
 #4 enter 1 letter at a time
 ''')

print('\n'*2)
word1='leopard'
word2='encyclopedia'
word3='asafoetida'
word4='inhabitant'
word5='equinox'
word6='goodbye'
word7='chaptest'
word8='corona'
word9='china'
word10='hibiscus'
clue1='''
 #1 seven letter word
 #2 part of the cat family
'''
clue2='''
 #1 twelve letter word
 #2 you've referred me at least once in your life
'''
clue3='''
 #1 ten letter word
 #2 a medicinal herb used in Indian cuisine
 #3 trivial name is 'stinking gum'
'''
clue4='''
 #1 ten letter word
 #2 synonym for resident
'''
clue5='''
 #1 seven letter word
 #2 happens twice a year
'''
clue6='''
#1 seven letter word
#2 a synonym of adieu 
'''
clue7='''
#1 eight letter word
#2 test conducted after every chapter
'''
clue8='''
#1 lockdown 
#2 a deadly virus
'''
clue9='''
#1 country name
#2 neighbhouring India 
'''
clue10='''
#1 scientific name of shoe flower
#2 starts with h 
'''
library={1:(word1,clue1),2:(word2,clue2),3:(word3,clue3),4:(word4,clue4),5:(word5,clue5),6:(word6,clue6),7:(word7,clue7),8:(word8,clue8),9:(word9,clue9),10:(word10,clue10)}

import random
i=random.randint(1,10)
word=library[i][0]
clue=library[i][1]

import time
def liststr(a):
    x=''
    for i in a:
        x=x+i
    return x
def strlist(a):
    x=[]
    for i in a:
        x=x+[' ']+list(i)
    return x

def disp(b):
    x=[]
    for i in b:
        x=x+[' ']+['_']
    return x

display=disp(word)
check= strlist(word)
life=5
print(clue)
while life>=0:
    if display==check:
        print(word)
        time.sleep(2)
        while True:
            print('YOU WIN',end='  ')
   
    print(liststr(display),' '*10,'lives left = ',life)
    x=input('enter: ')
    if x =='clue':
        print('\n')
        print(clue)
        print('\n')
    if x not in check:
        life=life-1
    for i in range(len(check)):
        if x==check[i]:
            display[i]=x

print('THE WORD IS ',word)
time.sleep(2)
while True:
    print('YOU LOSE',end='  ')
