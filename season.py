import data
import random

print('\033[1;31;40m __  __       _   _          \033[1;33;40m___        _')
print('\033[1;31;40m|  \/  | __ _| |_| |__  ___\033[1;33;40m / _ \ _   _(_)____')
print("\033[1;31;40m| |\/| |/ _` | __| '_ \/ __|\033[1;33;40m| | | | | | | |_  /")
print("\033[1;31;40m| |  | | (_| | |_| | | \__ |\033[1;33;40m| |_| | |_| | |/ /")
print(f"\033[1;31;40m|_|  |_|\__,_|\__|_| |_|___/\033[1;33;40m\__\_\\__,_|_/___|  {data.ver}")

splash = random.choice(data.ss)
print(splash)
print('Season 1 - Autumn (4 November - 1 December)')

pumpkins = 0
impossible = 0  

print('Rules:')
print('1) You have to collect pumpkins')
print('2) 500 pumpkins - win')
print('3) Pumkins:')
print('-Normal pumpkin - 1 pumpkin')
print('-Super pumpkin - 5 pumkins')
print('-Extra pumpkin - 10 pumkins')
print('-Mega pumkin - 50 pumpkins')
print('4) Have fun')

print('Difficulty levels:')
print('1. Easy - normal pumpkin')
print('2. Normal - super pumpkin')
print('3. Hard - extra pumpkin')
print('4. Impossible - mega pumpkin (Only one per game)')

op = True

while op:
    difficulty = input('Select difficulty: ')
    if difficulty == '1':
        m = random.choice(data.medium)
        print(m)
        ans = input('')
        if m == data.m1:
            if ans == '45':
                pumpkins = pumpkins + 1
        if m == data.m2:
            if ans == '40':
                pumpkins = pumpkins + 1
        if m == data.m3:
            if ans == '24':
                pumpkins = pumpkins + 1
        if m == data.m4:
            if ans == '10':
                pumpkins = pumpkins + 1
        if m == data.m5:
            if ans == '24':
                pumpkins = pumpkins + 1
        if m == data.m6:
            if ans == '36':
                pumpkins = pumpkins + 1
        if m == data.m7:
            if ans == '1':
                pumpkins = pumpkins + 1
        if m == data.m8:
            if ans == '4':
                pumpkins = pumpkins + 1
        if m == data.m9:
            if ans == '6':
                pumpkins = pumpkins + 1
        if m == data.m10:
            if ans == '15':
                pumpkins = pumpkins + 1
        if m == data.m11:
            if ans == '8':
                pumpkins = pumpkins + 1
        if m == data.m12:
            if ans == '338.9':
                pumpkins = pumpkins + 1
        if m == data.m13:
            if ans == '4':
                pumpkins = pumpkins + 1
        if m == data.m14:
            if ans == '6':
                pumpkins = pumpkins + 1
        if m == data.m15:
            if ans == '5':
                pumpkins = pumpkins + 1
        if m == data.m16:
            if ans == '9':
                pumpkins = pumpkins + 1
        if m == data.m17:
            if ans == '81':
                pumpkins = pumpkins + 1
        if m == data.m18:
            if ans == '15':
                pumpkins = pumpkins + 1
        if m == data.m19:
            if ans == '20':
                pumpkins = pumpkins + 1
        if m == data.m20:
            if ans == '4':
                pumpkins = pumpkins + 1

    if (difficulty == '2'):
        h = random.choice(data.hard)
        print(h)
        ans = input('')
        if h == data.h1:
            if ans == '9':
                pumpkins = pumpkins + 5
        if h == data.h4:
            if ans == '27':
                pumpkins = pumpkins + 5
        if h == data.h5:
            if ans == '16':
                pumpkins = pumpkins + 5
        if h == data.h6:
            if ans == '32':
                pumpkins = pumpkins + 5
        if h == data.h7:
            if ans == '1024':
                pumpkins = pumpkins + 5
        if h == data.h8:
            if ans == '2048':
                pumpkins = pumpkins + 5
        if h == data.h9:
            if ans == '8':
                pumpkins = pumpkins + 5
        if h == data.h10:
            if ans == '16':
                pumpkins = pumpkins + 5
        if h == data.h11:
            if ans == '32':
                pumpkins = pumpkins + 5
        if h == data.h12:
            if ans == '64':
                pumpkins = pumpkins + 5
        if h == data.h13:
            if ans == '128':
                pumpkins = pumpkins + 5
        if h == data.h14:
            if ans == '256':
                pumpkins = pumpkins + 5
        if h == data.h15:
            if ans == '512':
                pumpkins = pumpkins + 5
    if (difficulty == '3'):
        rh = random.choice(data.real_hard)
        print(rh)
        ans = input('')
        if rh == data.rh1:
            if ans == '40320':
                pumpkins = pumpkins + 10
        if rh == data.rh2:
            if ans == '24':
                pumpkins = pumpkins + 10
        if rh == data.rh3:
            if ans == '120':
                pumpkins = pumpkins + 10
        if rh == data.rh4:
            if ans == '3628800':
                pumpkins = pumpkins + 10
        if rh == data.rh5:
            if ans == '720':
                pumpkins = pumpkins + 10
        if rh == data.rh6:
            if ans == '362880':
                pumpkins = pumpkins + 10
        if rh == data.rh7:
            if ans == '2':
                pumpkins = pumpkins + 10
    if difficulty == '4' and impossible == 0:
        impossible = 1
        si = random.choice(data.season_impossible)
        print(si)
        ans = input('')
        if si == data.si1:
            if ans == '$':
                pumpkins = pumpkins + 50
        if si == data.si2:
            if ans == '(':
                pumpkins = pumpkins + 50
        if si == data.si3:
            if ans == '())':
                pumpkins = pumpkins + 50
        if si == data.si4:
            if ans == '()':
                pumpkins = pumpkins + 50

    print(f'Pumpkins: {pumpkins}')
    if pumpkins > 199:
        op = False
        print('You won!')
    if pumpkins < -199:
        op = False
        print('You failed')

input('Press enter to exit...')