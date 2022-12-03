import data
import random
import sys
import os
s = 1
d = 50
print('\033[0;34;40m __  __       _   _         \033[1;31;40m ___        _')
print('\033[0;34;40m|  \/  | __ _| |_| |__  ___ \033[1;31;40m/ _ \ _   _(_)____')
print("\033[0;34;40m| |\/| |/ _` | __| '_ \/ __|\033[1;31;40m| | | | | | | |_  /")
print("\033[0;34;40m| |  | | (_| | |_| | | \__ |\033[1;31;40m| |_| | |_| | |/ /")
print(f"\033[0;34;40m|_|  |_|\__,_|\__|_| |_|___/\033[1;31;40m\__\_\\__,_|_/___| \033[0;32;40m{data.ver}")

splash = random.choice(data.ns)
print(splash)

print('\033[0;37;40mRules:')
print('1) To win you have to collect 1000 points')
print('2) There are 5 difficulty levels: very easy, easy, medium,  hard and extreme')
print('5) You can get help: give up without losing points (type qw) (only one) and get new questions (type ty) (only one)')
print('6) Helps are active after second question')
print('7) If the answer to the first question is wrong, you will fail')
print('8) The helps arent available in extreme difficulty')

score = 0

qw = 0
er = 0
ty = 0

easy = 0
hard = 0
real_hard = 0
extreme = 0
print('Select difficulty:')
print('1. Very easy - 1/0 points (unlimited)')
print('2. Easy - 5/10 points (50)')
print('3. Medium - 10/20 points (20)')
print('4. Hard - 50/100 points (5) - after first round')
print('5. Extreme - win/lose (1) - after first round')
print('Rare level (2% per round) - 900/0')
difficulty = input('')
rn = random.choice(data.random)
if (difficulty == '1') and (rn != 25):
    e = random.choice(data.easy)
    print(e)
    ans = input('')
    if e == data.e1:
        if ans == '4':
            score = score + 1
        else:
            score = -200
    if e == data.e2:
        if ans == '5':
            score = score + 1
        else:
            score = -200
    if e == data.e3:
        if ans == '10':
            score = score + 1
        else:
            score = -200
    if e == data.e4:
        if ans == '12':
            score = score + 1
        else:
            score = -200
    if e == data.e5:
        if ans == '10':
            score = score + 1
        else:
            score = -200
    if e == data.e6:
        if ans == '12':
            score = score + 1
        else:
            score = -200
    if e == data.e7:
        if ans == '0':
            score = score + 1
        else:
            score = -200
    if e == data.e8:
        if ans == '1':
            score = score + 1
        else:
            score = -200
    if e == data.e9:
        if ans == '0':
            score = score + 1
        else:
            score = -200
    if e == data.e10:
        if ans == '5':
            score = score + 1
        else:
            score = -200
    if e == data.e11:
        if ans == '4':
            score = score + 1
        else:
            score = -200
    if e == data.e12:
        if ans == '4':
            score = score + 1
        else:
            score = -200
    if e == data.e13:
        if ans == '6':
            score = score + 1
        else:
            score = -200
    if e == data.e14:
        if ans == '12':
            score = score + 1
        else:
            score = -200
    if e == data.e15:
        if ans == '18':
            score = score + 1
        else:
            score = -200
    if e == data.e16:
        if ans == '10':
            score = score + 1
        else:
            score = -200
    if e == data.e17:
        if ans == '20':
            score = score + 1
        else:
            score = -200
    if e == data.e18:
        if ans == '5':
            score = score + 1
        else:
            score = -200
    if e == data.e19:
        if ans == '15':
            score = score + 1
        else:
            score = -200
    if e == data.e20:
        if ans == '13':
            score = score +1
        else:
            score = -200

if (difficulty == '2'):
    easy = easy + 1
    m = random.choice(data.medium)
    print(m)
    ans = input('')
    if m == data.m1:
        if ans == '45':
            score = score + 5
        else:
            score = -200
    if m == data.m2:
        if ans == '40':
            score = score + 5
        else:
            score = -200
    if m == data.m3:
        if ans == '24':
            score = score + 5
        else:
            score = -200
    if m == data.m4:
        if ans == '10':
            score = score + 5
        else:
            score = -200
    if m == data.m5:
        if ans == '24':
            score = score + 5
        else:
            score = -200
    if m == data.m6:
        if ans == '36':
            score = score + 5
        else:
            score = -200
    if m == data.m7:
        if ans == '1':
            score = score + 5
        else:
            score = -200
    if m == data.m8:
        if ans == '4':
            score = score + 5
        else:
            score = -200
    if m == data.m9:
        if ans == '6':
            score = score + 5
        else:
            score = -200
    if m == data.m10:
        if ans == '15':
            score = score + 5
        else:
            score = -200
    if m == data.m11:
        if ans == '8':
            score = score + 5
        else:
            score = -200
    if m == data.m12:
        if ans == '338.9':
            score = score + 5
        else:
            score = -200
    if m == data.m13:
        if ans == '4':
            score = score + 5
        else:
            score = -200
    if m == data.m14:
        if ans == '6':
            score = score + 5
        else:
            score = -200
    if m == data.m15:
        if ans == '5':
            score = score + 5
        else:
            score = -200
    if m == data.m16:
        if ans == '9':
            score = score + 5
        else:
            score = -200
    if m == data.m17:
        if ans == '81':
            score = score + 5
        else:
            score = -200
    if m == data.m18:
        if ans == '15':
            score = score + 5
        else:
            score = -200
    if m == data.m19:
        if ans == '20':
            score = score + 5
        else:
            score = -200
    if m == data.m20:
        if ans == '4':
            score = score + 5
        else:
            score = -200

if (difficulty == '3') and (hard != 20) and (rn != 25):
    hard = hard + 1
    h = random.choice(data.hard)
    print(h)
    ans = input('')
    if h == data.h1:
        if ans == '9':
            score = score + 10
        else:
            score = -200
    if h == data.h4:
        if ans == '27':
            score = score + 10
        else:
            score = -200
    if h == data.h5:
        if ans == '16':
            score = score + 10
        else:
            score = -200
    if h == data.h6:
        if ans == '32':
            score = score + 10
        else:
            score = -200
    if h == data.h7:
        if ans == '1024':
            score = score + 10
        else:
            score = -200
    if h == data.h8:
        if ans == '2048':
            score = score + 10
        else:
            score = -2000
    if h == data.h9:
        if ans == '8':
            score = score + 10
        else:
            score = -200
    if h == data.h10:
        if ans == '16':
            score = score + 10
        else:
            score = -200
    if h == data.h11:
        if ans == '32':
            score = score + 10
        else:
            score = -200
    if h == data.h12:
        if ans == '64':
            score = score + 10
        else:
            score = -200
    if h == data.h13:
        if ans == '128':
            score = score + 10
        else:
            score = -200
    if h == data.h14:
        if ans == '256':
            score = score + 10
        else:
            score = -2000
    if h == data.h15:
        if ans == '512':
            score = score + 10
        else:
            score = -200
if rn == 25:
    print('Congratulations, you unlocked rare level. You can collect 900 points!')
    print('50+49')
    ans = input('')
    if ans == '99':
        score = score + 900
    else:
        score = score
print('Score: ', score)
op = True
if score < -199:
    print('You lose')
    op = False
while op:

    rn = random.choice(data.random)
    difficulty = input('Select difficulty: ')
    if (difficulty == '1') and (rn != 25):
        e = random.choice(data.easy)
        print(e)
        ans = input('')
        if e == data.e1:
            if ans == '4':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e2:
            if ans == '5':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e3:
            if ans == '10':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e4:
            if ans == '12':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e5:
            if ans == '10':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e6:
            if ans == '12':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e7:
            if ans == '0':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e8:
            if ans == '1':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e9:
            if ans == '0':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e10:
            if ans == '5':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e11:
            if ans == '4':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e12:
            if ans == '4':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e13:
            if ans == '6':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e14:
            if ans == '12':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e14:
            if ans == '12':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e15:
            if ans == '18':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e16:
            if ans == '10':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e17:
            if ans == '20':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e18:
            if ans == '5':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e19:
            if ans == '15':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score
        if e == data.e20:
            if ans == '13':
                score = score + 1
            elif (ans == 'qw') and (qw == 0):
                score = score + 1
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score

    if (difficulty == '2') and (rn != 25) and (easy < 49.9):
        easy = easy + 1
        m = random.choice(data.medium)
        print(m)
        ans = input('')
        if m == data.m1:
            if ans == '45':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m2:
            if ans == '40':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m3:
            if ans == '24':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m4:
            if ans == '10':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m5:
            if ans == '24':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m6:
            if ans == '36':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m7:
            if ans == '1':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m8:
            if ans == '4':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m9:
            if ans == '6':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m10:
            if ans == '15':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m11:
            if ans == '8':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m12:
            if ans == '338.9':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m13:
            if ans == '4':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m14:
            if ans == '6':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m15:
            if ans == '5':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m16:
            if ans == '9':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m17:
            if ans == '81':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m18:
            if ans == '15':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m19:
            if ans == '20':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10
        if m == data.m20:
            if ans == '4':
                score = score + 5
            elif (ans == 'qw') and (qw == 0):
                score = score + 5
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 10

    if (difficulty == '3') and (hard < 19.9) and (rn != 25):
        hard = hard + 1
        h = random.choice(data.hard)
        print(h)
        ans = input('')
        if h == data.h1:
            if ans == '9':
                score = score + 10
            elif (ans == 'qw') and (qw == 0):
                score = score + 10
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 20
        if h == data.h4:
            if ans == '27':
                score = score + 10
            elif (ans == 'qw') and (qw == 0):
                score = score + 10
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 20
        if h == data.h5:
            if ans == '16':
                score = score + 10
            elif (ans == 'qw') and (qw == 0):
                score = score + 10
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 20
        if h == data.h6:
            if ans == '32':
                score = score + 10
            elif (ans == 'qw') and (qw == 0):
                score = score + 10
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 20
        if h == data.h7:
            if ans == '1024':
                score = score + 10
            elif (ans == 'qw') and (qw == 0):
                score = score + 10
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 20
        if h == data.h8:
            if ans == '2048':
                score = score + 10
            elif (ans == 'qw') and (qw == 0):
                score = score + 10
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 20
        if h == data.h9:
            if ans == '8':
                score = score + 10
            elif (ans == 'qw') and (qw == 0):
                score = score + 10
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 20
        if h == data.h10:
            if ans == '16':
                score = score + 10
            elif (ans == 'qw') and (qw == 0):
                score = score + 10
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 20
        if h == data.h11:
            if ans == '32':
                score = score + 10
            elif (ans == 'qw') and (qw == 0):
                score = score + 10
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 20
        if h == data.h12:
            if ans == '64':
                score = score + 10
            elif (ans == 'qw') and (qw == 0):
                score = score + 10
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 20
        if h == data.h13:
            if ans == '128':
                score = score + 10
            elif (ans == 'qw') and (qw == 0):
                score = score + 10
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 20
        if h == data.h14:
            if ans == '256':
                score = score + 10
            elif (ans == 'qw') and (qw == 0):
                score = score + 10
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 20
        if h == data.h15:
            if ans == '512':
                score = score + 10
            elif (ans == 'qw') and (qw == 0):
                score = score + 10
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score =  score - 20
    if difficulty == 'game.addScore(50)':
        score = score + 50
    if difficulty == 'SuperSecretLevel':
        ss=random.choice(data.super_secret)
        add = random.choice(data.points)
    if (difficulty == '5') and (extreme < 0.9) and (rn != 25):
        extreme = extreme + 1
        e = random.choice(data.extreme)
        print(e)
        ans = input('')
        if e == data.ex1:
            if ans == '56':
                score = 1000
            else:
                score = -200
        if e == data.ex2:
            if ans == '2':
                score = 1000
            else:
                score = -200
        if e == data.ex3:
            if ans == '0.625':
                score = 1000
            else:
                score = -200
        if e == data.ex4:
            if ans == '-2':
                score = 1000
            else:
                score = -200
        if e == data.ex5:
            if ans == '8/7':
                score = 1000
            else:
                score = -200
    if (difficulty == '4') and (real_hard == 0):
        real_hard = real_hard + 1
        rh = random.choice(data.real_hard)
        print(rh)
        ans = input('')
        if rh == data.rh1:
            if ans == '40320':
                score = score + 50
            elif (ans == 'qw') and (qw == 0):
                score = score + 50
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 100
        if rh == data.rh2:
            if ans == '24':
                score = score + 50
            elif (ans == 'qw') and (qw == 0):
                score = score + 50
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 100
        if rh == data.rh3:
            if ans == '120':
                score = score + 50
            elif (ans == 'qw') and (qw == 0):
                score = score + 50
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 100
        if rh == data.rh4:
            if ans == '3628800':
                score = score + 500
            elif (ans == 'qw') and (qw == 0):
                score = score + 50
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 100
        if rh == data.rh5:
            if ans == '720':
                score = score + 50
            elif (ans == 'qw') and (qw == 0):
                score = score + 50
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 100
        if rh == data.rh6:
            if ans == '362880':
                score = score + 50
            elif (ans == 'qw') and (qw == 0):
                score = score + 50
                qw = qw + 1
            elif (ans == 'ty') and (ty == 0):
                ty = ty + 1
            else:
                score = score - 100
    if (difficulty == '2') and (easy > 49.9):
        print('No more easy questions')
    if (difficulty == '3') and (hard > 19.9):
        print('Normal difficulty is out')
    if (difficulty == '5') and (extreme > 0.9):
        print('Extreme difficulty is only one time per game')

    if rn == 25:
        print('Congratulations, you unlocked rare level. You can collect 900 points, but you cant use help')
        print('50+49')
        ans = input('')
        if ans == '99':
            score = score + 900
        else:
            score = score
    print('Score: ', score)
    if score > 999:
        op = False
    if score < -199:
        op = False
pass

if score > 999:
    print('You won!')
if score < -199:
    print('You failed!')

input('Click enter to exit...\n')