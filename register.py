import data

print(f'MathsQuiz {data.ver} Register key')

y = input('Do you have a key for premium game? [y/n]')
if y == 'y':
    key = input('Enter key: ')
    if key == data.k1:
        print(f'The password is: {data.pa1}')
    elif key == data.k2:
        print(f'The password is: {data.pa2}')
    elif key == data.k3:
        print(f'The password is: {data.pa3}')
    elif key == data.k3:
        print(f'The password is: {data.pa3}')
    else:
        print('Invalid key')
if y == 'n':
    print('If you dont have a key type an email to s.gruszka@wp.pl')
    print('Subject: Premium, Content: nick and password')
    print('The features of premium mode:')
    print('- Score multiplier')
    print('- Beta channel')
    print('- Nicks')
input('')