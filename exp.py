import data
import random

print('\033[0;34;40m __  __       _   _         \033[1;31;40m ___        _')
print('\033[0;34;40m|  \/  | __ _| |_| |__  ___ \033[1;31;40m/ _ \ _   _(_)____')
print("\033[0;34;40m| |\/| |/ _` | __| '_ \/ __|\033[1;31;40m| | | | | | | |_  /")
print("\033[0;34;40m| |  | | (_| | |_| | | \__ |\033[1;31;40m| |_| | |_| | |/ /")
print(f"\033[0;34;40m|_|  |_|\__,_|\__|_| |_|___/\033[1;31;40m\__\_\\__,_|_/___| \033[0;32;40m{data.ver}")

print('Experiment')

l = True


score = 0
def main():
    global score
    global l
    e = random.choice(data.extreme)
    print(e)
    ans = input('')
    if e == data.ex1:
        if ans == '56':
            score = score + 100
        else:
            score = score - 200
    if e == data.ex2:
        if ans == '2':
            score = score + 100
        else:
            score = score - 200
    if e == data.ex3:
        if ans == '0.625':
            score = score + 100
        else:
            score = score - 200
    if e == data.ex4:
        if ans == '-2':
            score = score + 100
        else:
            score = score - 200
    if e == data.ex5:
        if ans == '8/7':
            score = score + 100
        else:
            score = score - 200
    if score > 999:
        l = False
    if score < -199:
        l = False
    print(score)

while l:
    main()

if score > 999:
    print('You won!')
    input('')
if score < -199:
    print('You failed!')
    input('')