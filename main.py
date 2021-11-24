import requests
import json
import matplotlib.pyplot as plt
import time
from colorama import Fore, init
import re

password = int(input(Fore.LIGHTCYAN_EX + 'Enter the mode\n' + Fore.CYAN + '1 - standart or 2 - fast\n'))

errors = 0
num = 0
languages = []
count = []
succs = 0
number_c = 1
custom_language = 2

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

while True:
    print(Fore.BLUE + f'\nEnter the programming languages you need\nCount number: {number_c}')
    time.sleep(0.2)
    print(Fore.MAGENTA + 'To stop typing, enter 0')
    custom_language = input()
    custom_language = custom_language.lower()
    if(custom_language == '0'):
        print(Fore.LIGHTWHITE_EX + f'\nTotal entered: {number_c - 1}')
        break
    if(custom_language in languages):
        print(Fore.RED + "Such a programming language already exists in the array")
        time.sleep(0.7)
        print(Fore.WHITE + 'Please, try again')
    if not custom_language or re.search("^\s*$", custom_language):
        print(Fore.RED + "You haven't entered anything")
        time.sleep(0.3)
        print(Fore.WHITE + 'Please, try again')
    else:
        languages.append(custom_language)
        number_c += 1

if(password == 1):
    if(number_c != 1):
        print(Fore.RESET + '\nGet info.', end='')
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
    if(number_c != 1):
        print(Fore.GREEN + "\nSTART!")
        api()
if(number_c != 1):
    print(Fore.LIGHTRED_EX + f'\nTotal errors - {errors}')

def plot():
    plt.bar(languages, count)
    plt.title('Языки программирования')
    plt.xlabel('Языки')
    plt.ylabel('Количество проектов')
    plt.show()
#plot()