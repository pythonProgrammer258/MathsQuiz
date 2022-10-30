import data
import random

print('\033[1;31;40m __  __       _   _          ___        _')
print('\033[1;31;40m|  \/  | __ _| |_| |__  ___ / _ \ _   _(_)____')
print("\033[1;31;40m| |\/| |/ _` | __| '_ \/ __| | | | | | | |_  /")
print("\033[1;31;40m| |  | | (_| | |_| | | \__ | |_| | |_| | |/ /")
print("\033[1;31;40m|_|  |_|\__,_|\__|_| |_|___/\__\_\\__,_|_/___|  v0.6")
print('Extreme mode')
print('Rules:')
print('To win you have to collect 2000 points')
print('No helps')
print('Only correct answers; bad answer = lose')
print('There are 1 difficulty level: extreme')

score = 0
op = True

while op:
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
    print(f'Score: {score}')
    if score > 1999:
        op = False
    if score < -199:
        op = False

if score > 1999:
    print('You won')
if score < -199:
    print('You failed!')

input('Click enter to exit...\n')