import data
import random

score = 0
qw = 0
ty = 0

print('\033[0;34;40m __  __       _   _          ___        _')
print('\033[0;34;40m|  \/  | __ _| |_| |__  ___ / _ \ _   _(_)____')
print("\033[0;34;40m| |\/| |/ _` | __| '_ \/ __| | | | | | | |_  /")
print("\033[0;34;40m| |  | | (_| | |_| | | \__ | |_| | |_| | |/ /")
print("\033[0;34;40m|_|  |_|\__,_|\__|_| |_|___/\__\_\\__,_|_/___|  v0.6")

print('Easy mode')
print('Rules:')
print('To win you have to collect 500 points')
print('You can use helps (one "ty" and one "qw")')
print('Good answer + 10; bad answer - 10')
print('-200 points = you lose')

op = True
while op:
    e = random.choice(data.easy_mode)
    print(e)
    ans = input('')
    if e == data.e1:
        if ans == '4':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.e2:
        if ans == '5':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.e3:
        if ans == '10':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.e4:
        if ans == '12':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.e5:
        if ans == '10':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.e6:
        if ans == '12':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.e7:
        if ans == '0':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.e8:
        if ans == '1':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.e9:
        if ans == '0':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.e10:
        if ans == '5':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.e11:
        if ans == '4':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.e12:
        if ans == '4':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.m1:
        if ans == '45':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.m2:
        if ans == '40':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.m3:
        if ans == '24':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.m4:
        if ans == '10':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.m5:
        if ans == '24':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.m6:
        if ans == '36':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.m7:
        if ans == '1':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.m8:
        if ans == '4':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.m9:
        if ans == '6':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.m10:
        if ans == '15':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.m11:
        if ans == '8':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    if e == data.m12:
        if ans == '338.9':
            score = score + 10
        elif (ans == 'qw') and (qw == 0):
            score = score + 10
            qw = qw + 1
        elif (ans == 'ty') and (ty == 0):
            ty = ty + 1
        else:
            score = score - 10
    print(f'Score: {score}')
    if score > 499:
        op = False
    if score < -199:
        op = False
if score > 499:
    print('You won!')
if score < -199:
    print('You failed!')

input('Click enter to exit')
