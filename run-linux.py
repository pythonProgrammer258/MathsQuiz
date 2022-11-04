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

print('\033[0;34;40m1. Normal mode (all help and difficulty levels)')
print('2. Extreme mode (without helps and hard levels)')
print('3. Easy mode (unlimited helps and easy difficulty levels)')
print('4. Tutorial')
print('5. Season mode (autumn)')

ver = input('Select mode: ')
if ver == '1':
    os.system('clear')
    os.system(f'python3 {normal}')
elif ver == '2':
    os.system('clear')
    os.system(f'python3 {extreme}')
elif ver == '3':
    os.system('clear')
    os.system(f'python3 {easy}')
elif ver == '4':
    os.system('clear')
    os.system(f'python3 {tut}')
elif ver == '5':
    os.system('clear')
    os.system(f'python3 {seas}')