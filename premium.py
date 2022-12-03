import data
import random
import os

print('\033[0;34;40m __  __       _   _          ___        _')
print('\033[0;34;40m|  \/  | __ _| |_| |__  ___ / _ \ _   _(_)____')
print("\033[0;34;40m| |\/| |/ _` | __| '_ \/ __| | | | | | | |_  /")
print("\033[0;34;40m| |  | | (_| | |_| | | \__ | |_| | |_| | |/ /")
print(f"\033[0;34;40m|_|  |_|\__,_|\__|_| |_|___/\__\_\\__,_|_/___|  {data.ver}")

print('Extreme mode with miltiplier (in present)')

op = False
logged = 0
score = 0
mult = 0

def login():
    global logged
    global op
    global mult
    print('Key:')
    k = input('')
    print('Password:')
    p = input('')
    if k == data.k1 and p == data.pa1:
        print(f'Hi, {data.ni1}')
        logged = 1
        op = True
        mult = data.mu1
    elif k == data.k2 and p == data.pa2:
        logged = 1
        op = True
        mult = data.mu2
        print(f'Hi, {data.ni2}')
    elif k == data.k3 and p == data.pa3:
        print(f'Hi, {data.ni3}')
        logged = 1
        op = True
        mult = data.mu3
    elif k == data.k4 and p == data.pa4:
        logged = 1
        op = True
        print(f'Hi, {data.ni4}')    
        mult = data.mu4
    else:
        print('Invalid key or password.')
login()
print('1. Extreme')
print('2. Impossible')

def main():
    global score
    global op
    global mult
    difficulty = input('Select difficulty: ')
    if difficulty == '1':
        e = random.choice(data.extreme)
        print(e)
        ans = input('')
        if e == data.ex1:
            if ans == '56':
                score = int(score + (100 * mult))
            else:
                score = -200
        if e == data.ex2:
            if ans == '2':
                score = int(score + (100 * mult))
            else:
                score = -200
        if e == data.ex3:
            if ans == '0.625':
                score = int(score + (100 * mult))
            else:
                score = -200
        if e == data.ex4:
            if ans == '-2':
                score = int(score + (100 * mult))
            else:
                score = -200
        if e == data.ex5:
            if ans == '8/7':
                score = int(score + (100 * mult))
            else:
                score = -200
    if difficulty == '2':
        yn = input('Are you sure> [y/n] ')
        if yn == 'y':
            i = random.choice(data.impossible)
            print(i)
            ans = input('Y+ ')
            if i == data.i1:
                if ans == ')>%':
                    score = int(score + (250 * mult))
                else:
                    score = -200
            if i == data.i2:
                if ans == '#$%>%':
                    score = int(score + (250 * mult))
                else:
                    score = -200
            if i == data.i3:
                if ans == '^':
                    score = int(score + (250 * mult))
                else:
                    score = -200
    print(f'Score: {score}')
    if score > 999:
        op = False
    if score < -199:
        op = False

while op:
    main()

if score > 999:
    print('You won!')
if score < -199:
    print('You failed')
input('')
