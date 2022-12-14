import data
import random

print('\033[1;31;40m __  __       _   _          ___        _')
print('\033[1;31;40m|  \/  | __ _| |_| |__  ___ / _ \ _   _(_)____')
print("\033[1;31;40m| |\/| |/ _` | __| '_ \/ __| | | | | | | |_  /")
print("\033[1;31;40m| |  | | (_| | |_| | | \__ | |_| | |_| | |/ /")
print(f"\033[1;31;40m|_|  |_|\__,_|\__|_| |_|___/\__\_\\__,_|_/___|  {data.ver}")

splash = random.choice(data.exts)
print(splash)

print('Extreme mode')
print('Rules:')
print('To win you have to collect 2000 points')
print('No helps')
print('Only correct answers; bad answer = lose')
print('There are 2 difficulty levels: extreme and impossible')

print('1. Extreme (100/lose)')
print('2. Impossible (250/lose)')
score = 0
imp = 0
op = True


def main():
    global score
    global imp
    global op
    difficulty = input('Select difficulty: ')
    if difficulty == '1':
        e = random.choice(data.extreme)
        print(e)
        ans = input('')
        if e == data.ex1:
            if ans == '56':
                score = score + 100
            else:
                score = -200
        if e == data.ex2:
            if ans == '2':
                score = score + 100
            else:
                score = -200
        if e == data.ex3:
            if ans == '0.625':
                score = score + 100
            else:
                score = -200
        if e == data.ex4:
            if ans == '-2':
                score = score + 100
            else:
                score = -200
        if e == data.ex5:
            if ans == '8/7':
                score = score + 100
            else:
                score = -200
    if difficulty == '2' and imp < 2.9:
        imp = imp + 1
        yn = input('Are you sure> [y/n] ')
        if yn == 'y':
            i = random.choice(data.impossible)
            print(i)
            ans = input('Y+ ')
            if i == data.i1:
                if ans == ')>%':
                    score = score + 250
                else:
                    score = -200
            if i == data.i2:
                if ans == '#$%>%':
                    score = score + 250
                else:
                    score = -200
            if i == data.i3:
                if ans == '^':
                    score = score + 250
                else:
                    score = -200
    if difficulty == '2' and imp > 2.9:
        print('No more impossible levels')
    print(f'Score: {score}')
    if score > 1999:
        op = False
    if score < -199:
        op = False



while op:
    main()

if score > 1999:
    print('You won')
if score < -199:
    print('You failed!')

input('Click enter to exit...\n')