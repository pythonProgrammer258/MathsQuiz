import data
import random

print('\033[0;34;40m __  __       _   _          ___        _')
print('\033[0;34;40m|  \/  | __ _| |_| |__  ___ / _ \ _   _(_)____')
print("\033[0;34;40m| |\/| |/ _` | __| '_ \/ __| | | | | | | |_  /")
print("\033[0;34;40m| |  | | (_| | |_| | | \__ | |_| | |_| | |/ /")
print("\033[0;34;40m|_|  |_|\__,_|\__|_| |_|___/\__\_\\__,_|_/___|  v0.6")

print('Tutorial')

print('2+2')
print('Solve this')

ans = input('')

if ans == '4':
    print('Correct!')
else:
    print('Incorrect :(')

print('Now, you can choose difficulty:')
print('1. Very easy, if your answer is correct, you get 1 point, if your answer isnt correct, no problem')
print('2. Easy, if your answer is correct, you get 5 points, if your answer isnt correct, you lose 10 points')
print('3. Medium, if your answer is correct, you get 10 points, if your answer isnt correct, you lose 20 points')
print('When you get 500 points, you win, if you get score points, you lose')
difficulty = input('')
score = 0

op = True
while op:
    rn = random.choice(data.random)
    if (difficulty == '1') and (rn != 25):
        e = random.choice(data.easy)
        print(e)
        ans = input('')
        if e == data.e1:
            if ans == '4':
                score = score + 1
            else:
                score = score
        if e == data.e2:
            if ans == '5':
                score = score + 1
            else:
                score = score
        if e == data.e3:
            if ans == '10':
                score = score + 1
            else:
                score = score
        if e == data.e4:
            if ans == '12':
                score = score + 1
            else:
                score = score
        if e == data.e5:
            if ans == '10':
                score = score + 1
            else:
                score = score
        if e == data.e6:
            if ans == '12':
                score = score + 1
            else:
                score = score
        if e == data.e7:
            if ans == '0':
                score = score + 1
            else:
                score = score
        if e == data.e8:
            if ans == '1':
                score = score + 1
            else:
                score = score
        if e == data.e9:
            if ans == '0':
                score = score + 1
            else:
                score = score
        if e == data.e10:
            if ans == '5':
                score = score + 1
            else:
                score = score
        if e == data.e11:
            if ans == '4':
                score = score + 1
            else:
                score = score
        if e == data.e12:
            if ans == '4':
                score = score + 1
            else:
                score = score
        if e == data.e13:
            if ans == '6':
                score = score + 1
            else:
                score = score
        if e == data.e14:
            if ans == '12':
                score = score + 1
            else:
                score = score
        if e == data.e15:
            if ans == '18':
                score = score + 1
            else:
                score = score
        if e == data.e16:
            if ans == '10':
                score = score + 1
            else:
                score = score
        if e == data.e17:
            if ans == '20':
                score = score + 1
            else:
                score = score
        if e == data.e18:
            if ans == '5':
                score = score + 1
            else:
                score = score
        if e == data.e19:
            if ans == '15':
                score = score + 1
            else:
                score = score
        if e == data.e20:
            if ans == '13':
                score = score +1
            else:
                score = score

    if (difficulty == '2'):
        m = random.choice(data.medium)
        print(m)
        ans = input('')
        if m == data.m1:
            if ans == '45':
                score = score + 5
            else:
                score = score -10
        if m == data.m2:
            if ans == '40':
                score = score + 5
            else:
                score = score -10
        if m == data.m3:
            if ans == '24':
                score = score + 5
            else:
                score = score -10
        if m == data.m4:
            if ans == '10':
                score = score + 5
            else:
                score = score -10
        if m == data.m5:
            if ans == '24':
                score = score + 5
            else:
                score = score -10
        if m == data.m6:
            if ans == '36':
                score = score + 5
            else:
                score = score -10
        if m == data.m7:
            if ans == '1':
                score = score + 5
            else:
                score = score -10
        if m == data.m8:
            if ans == '4':
                score = score + 5
            else:
                score = score -10
        if m == data.m9:
            if ans == '6':
                score = score + 5
            else:
                score = score -10
        if m == data.m10:
            if ans == '15':
                score = score + 5
            else:
                score = score - 10
        if m == data.m11:
            if ans == '8':
                score = score + 5
            else:
                score = score -10
        if m == data.m12:
            if ans == '338.9':
                score = score + 5
            else:
                score = score - 10
        if m == data.m13:
            if ans == '4':
                score = score + 5
            else:
                score = score -10
        if m == data.m14:
            if ans == '6':
                score = score + 5
            else:
                score = score - 10
        if m == data.m15:
            if ans == '5':
                score = score + 5
            else:
                score = score -10
        if m == data.m16:
            if ans == '9':
                score = score + 5
            else:
                score = score - 10
        if m == data.m17:
            if ans == '81':
                score = score + 5
            else:
                score = score - 10
        if m == data.m18:
            if ans == '15':
                score = score + 5
            else:
                score = score -10
        if m == data.m19:
            if ans == '20':
                score = score + 5
            else:
                score = score -10
        if m == data.m20:
            if ans == '4':
                score = score + 5
            else:
                score = score -10

    if (difficulty == '3') and (rn != 25):
        h = random.choice(data.hard)
        print(h)
        ans = input('')
        if h == data.h1:
            if ans == '9':
                score = score + 10
            else:
                score = score -20
        if h == data.h4:
            if ans == '27':
                score = score + 10
            else:
                score = score-20
        if h == data.h5:
            if ans == '16':
                score = score + 10
            else:
                score = score-20
        if h == data.h6:
            if ans == '32':
                score = score + 10
            else:
                score = score-20
        if h == data.h7:
            if ans == '1024':
                score = score + 10
            else:
                score = score-20
        if h == data.h8:
            if ans == '2048':
                score = score + 10
            else:
                score = score-20
        if h == data.h9:
            if ans == '8':
                score = score + 10
            else:
                score = score-20
        if h == data.h10:
            if ans == '16':
                score = score + 10
            else:
                score = score-20
        if h == data.h11:
            if ans == '32':
                score = score + 10
            else:
                score = score-20
        if h == data.h12:
            if ans == '64':
                score = score + 10
            else:
                score = score-20
        if h == data.h13:
            if ans == '128':
                score = score + 10
            else:
                score = score-20
        if h == data.h14:
            if ans == '256':
                score = score + 10
            else:
                score = score-20
        if h == data.h15:
            if ans == '512':
                score = score + 10
            else:
                score = score-20
    if rn == 25:
        print('Congratulations, you unlocked rare level. You can collect 900 points!')
        print('50+49')
        ans = input('')
        if ans == '99':
            score = score + 900
        else:
            score = score
    if score > 499:
        op = False
    if score < -199:
        op = False

    print('Score: ', score)

    difficulty = input('Select difficulty: ')
if score > 499:
    print('You completed the tutorial')
if score < -199:
    print('You failed, didnt complete the tutorial')
input('Click enter to exit...')