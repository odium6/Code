import requests
import json
import matplotlib.pyplot as plt
import time
from colorama import Fore, init
import re

password = 0

while True:
    try:
        time.sleep(0.3)
        password = int(input(Fore.LIGHTCYAN_EX + 'Enter the mode\n' + Fore.CYAN + '1 - standart or 2 - fast\n'))
        if(password != 1) and (password != 2):
            print(Fore.RED + 'Error ' + Fore.LIGHTRED_EX + '(Invalid number)')
            time.sleep(0.2)
            print(Fore.WHITE + 'Please, try again')
        else:
            break
    except ValueError:
        print(Fore.RED + 'Error ' + Fore.LIGHTRED_EX + '(Incorrect data)')
        time.sleep(0.2)
        print(Fore.WHITE + 'Please, try again')

errors = 0
num = 0
languages = []
count = []
succs = 0
number_c = 1
custom_language = 2
exit_graph = 0

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

while True:
    print(Fore.BLUE + f'\nEnter the programming language you need\nAlready entered: {number_c-1}')
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
    if(custom_language != 0) and (custom_language not in languages) and (not re.search("^\s*$", custom_language)):
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
    time.sleep(0.2)
    print(Fore.LIGHTRED_EX + f'\nTotal errors - {errors}')

def plot_stolb():
    global languages, count
    try:
        plt.bar(languages, count)
        plt.title('Языки программирования')
        plt.xlabel('Языки')
        plt.ylabel('Количество проектов')
        plt.show()
    except:
        exit(0)

grade = languages
def plot_pie():
    global languages, count
    plt.pie(count, labels = grade, autopct = '%2.3f%%')
    plt.show()

if(errors != 0):
    print(Fore.RED + 'Error' + Fore.LIGHTRED_EX + '\nFailed to build graph')

if(errors == 0) and (num != 0):
    while True:
        try:
            time.sleep(0.6)
            WouldGraph = int(input(Fore.LIGHTCYAN_EX + '\nWould you like to display a graphic?\n' + Fore.LIGHTGREEN_EX + '1 - Yes ' + Fore.RESET + 'or' + Fore.RED + ' 2 - No\n'))
            if(WouldGraph != 1) and (WouldGraph != 2):
                print(Fore.RED + 'Error ' + Fore.LIGHTRED_EX + '(Invalid number)')
                print(Fore.WHITE + 'Please, try again')
            if(WouldGraph == 1):
                exit_graph = 0
                break
            if(WouldGraph == 2):
                print(Fore.LIGHTGREEN_EX + '\n\nThanks for use!')
                exit_graph = 1 #----------------------------------------------------------------------------------------для корректного выхода из программы
                break
        except ValueError:
            print(Fore.RED + 'Error' + Fore.LIGHTRED_EX + '(Value error)')
            print(Fore.WHITE + 'Please, try again')
        except:
            print(Fore.LIGHTRED_EX + 'Unknown error')
            print(Fore.WHITE + 'Please, try again')

    if(exit_graph == 1): #----------------------------------------------------------------------------------------------для корректного выхода из программы
        exit(0)

    while True:
        try:
            vvod_plot = int(input(Fore.LIGHTCYAN_EX + '\nWhat graphic do you want to display?\n' + Fore.CYAN +'1 - Bar graph' + Fore.WHITE + ' or' + Fore.CYAN + ' 2 - Circular chart\n'))
            if(vvod_plot != 1) and (vvod_plot != 2):
                print(Fore.RED + 'Error ' + Fore.LIGHTRED_EX + '(Invalid number)')
                print(Fore.WHITE + 'Please, try again')
            else:
                break
        except ValueError:
            print(Fore.RED + 'Error' + Fore.LIGHTRED_EX + '(Value error)')
            print(Fore.WHITE + 'Please, try again')
        except:
            print(Fore.LIGHTRED_EX + 'Unknown error')
            print(Fore.WHITE + 'Please, try again')

    if(vvod_plot == 1):
        try:
            plot_stolb()
        except ValueError:
            print(Fore.RED + '\nFailed to build graph' + Fore.LIGHTRED_EX + ' (Value error)')
            exit(0)
        except:
            print(Fore.LIGHTRED_EX + 'Unknown error')
            exit(0)
    if(vvod_plot == 2):
        try:
            plot_pie()
        except ValueError:
            print(Fore.RED + '\nFailed to build graph' + Fore.LIGHTRED_EX + ' (Value error)')
            exit(0)
        except:
            print(Fore.LIGHTRED_EX + 'Unknown error')
            exit(0)
    print(Fore.LIGHTCYAN_EX + "\nSUCCESSFUL!")
    time.sleep(0.2)
    print(Fore.LIGHTRED_EX + f'\nTotal errors - {errors}')

else:
    exit(0)