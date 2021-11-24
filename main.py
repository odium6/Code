import requests
import json
import matplotlib.pyplot as plt
import time
from colorama import Fore, init

password = int(input('Enter code access\n'))

errors = 0
num = 0
languages = ['python', 'cpp', 'java', 'c#', 'javascript', 'go', 'pascal', 'basic']
count = []
succs = 0
custom_language = 0
number_c = 1

def point(number):
    number = str(number)[::-1]
    result = ''
    for i, num in enumerate(number):
        if i % 3 == 0:
            result += '.'
        result += num
    result = result[::-1][:-1]
    return result

def api():
    global errors, num
    for i in languages:
        num += 1
        try:
            a = requests.get(f"https://api.github.com/search/repositories?q=language:{i}")
            data = a.json()
            dat = data['total_count']
            print(Fore.LIGHTWHITE_EX + f'{num} ' + Fore.RESET + f'{i} -- ' + Fore.GREEN + point(f'{dat}') + Fore.RESET + ' -- projects')
            count.append(data['total_count'])
            succs = 1
        except KeyError:
            errors += 1
            print(Fore.LIGHTWHITE_EX + f'{num} ' + Fore.RESET + 'Server ' + Fore.RED + 'rejected ' + Fore.RESET + 'request' + Fore.CYAN+ f' {i}' + Fore.LIGHTRED_EX + ' (KeyError)')
            succs = 0
        except:
            print(Fore.RED + 'Unknown error')
            succs = 0
            errors += 1
    if(succs == 1):
        time.sleep(1)
        print(Fore.LIGHTCYAN_EX + "\nSUCCESSFUL!")
    else:
        pass

if(password != 1) and (password != 2):
    print(Fore.LIGHTRED_EX + 'YOU DON’T HAVE ACCESS')
    exit(0)

try:
    check_custom = int(input("Would you like to introduce your programming languages?\n" + Fore.LIGHTCYAN_EX + "1 - yes" + " or" + " 2 - no\n"))
except ValueError:
    errors += 1
    time.sleep(1)
    print(Fore.RED + "You entered a line, not a number")
    time.sleep(0.4)
    print(Fore.WHITE + 'Please, try again')
    exit(0)
if(check_custom == 1):
    print("How many programming languages do you need?")
    try:
        colvo = int(input())
    except ValueError:
        errors += 1
        print(Fore.RED + 'You entered a line, not a number')
        print(Fore.WHITE + 'Please, try again')
        exit(0)
    except:
        errors += 1
        print(Fore.RED + 'Unknown error')
    for i in range(0, colvo):
        while custom_language != languages:
            print(Fore.BLUE + f'Enter the programming languages you need {number_c}')
            custom_language = input()
            if(custom_language in languages):
                print(Fore.RED + "Such a programming language already exists in the array")
                time.sleep(0.7)
                print(Fore.WHITE + 'Please, try again')
            else:
                languages.append(custom_language)
                number_c += 1
                break
else:
    pass

if(password == 1):
    print(Fore.RESET + 'Get info.', end='')
    time.sleep(1)
    print(Fore.RESET + '.', end='')
    time.sleep(0.7)
    print(Fore.RESET + '.', end='')
    time.sleep(2)
    print(Fore.RESET + '.', end='')
    time.sleep(0.3)
    print(Fore.RESET + '.')
    api()
if(password == 2):
    print(Fore.GREEN + "START!")
    api()

print(Fore.LIGHTRED_EX + f'\nTotal errors - {errors}')

def plot():
    plt.bar(languages, count)
    plt.title('Языки программирования')
    plt.xlabel('Языки')
    plt.ylabel('Количество проектов')
    plt.show()
