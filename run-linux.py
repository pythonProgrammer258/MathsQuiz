import os
import data
print('\033[0;34;40m __  __       _   _         \033[1;31;40m ___        _')
print('\033[0;34;40m|  \/  | __ _| |_| |__  ___ \033[1;31;40m/ _ \ _   _(_)____')
print("\033[0;34;40m| |\/| |/ _` | __| '_ \/ __|\033[1;31;40m| | | | | | | |_  /")
print("\033[0;34;40m| |  | | (_| | |_| | | \__ |\033[1;31;40m| |_| | |_| | |/ /")
print(f"\033[0;34;40m|_|  |_|\__,_|\__|_| |_|___/\033[1;31;40m\__\_\\__,_|_/___|  \033[0;32;40m{data.ver}")

print(r'Enter path for example /home/user/documents/mathsQuiz')
src = input('')

normal = rf'{src}/normal.py'
extreme = rf'{src}/extreme.py'
easy = rf'{src}/easy.py'
tut = rf'{src}/tutorial.py'
seas = rf'{src}/season.py'
exp = rf'{src}/exp.py'
premium = rf'{src}/premium.py'
reg = rf'{src}\register.py'
print('\033[0;34;40m1. Normal mode (all help and difficulty levels)')
print('\033[1;31;40m2. Extreme mode (without helps and very hard levels)')
print('\033[0;34;40m3. Easy mode (unlimited helps and easy difficulty levels)')
print('\033[0;32;40m4. Tutorial mode (tutorial)')
print('\033[0;34;40m 5. -')
print('\033[0m6.Experimental mode')
print('\033[0;34;40m7.Premium mode')
print('\033[0;34;40m8.Register key for premium mode')

ver = input('\033[0;34;40mSelect mode: ')
if ver == '1':
    os.system('cls')
    os.system(f'python {normal}')
elif ver == '2':
    os.system('cls')
    os.system(f'python {extreme}')
elif ver == '3':
    os.system('cls')
    os.system(f'python {easy}')
elif ver == '4':
    os.system('cls')
    os.system(f'python {tut}')
elif ver == '5':
    print('Season mode has been ended')
    #os.system('cls')
    #os.system(f'python {seas}')
elif ver == '6':
    y = input('Running experimental mode... Are you sure? [y/n] ')
    if y == 'y':
        os.system('cls')
        os.system(f'python {exp}')
elif ver == '7':
    os.system('cls')
    os.system(f'python {premium}')
elif ver == '8':
    os.system('cls')
    os.system(f'python {reg}')