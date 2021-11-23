import requests
import json
import matplotlib.pyplot as plt
import time
from colorama import Fore, init
password = int(input('Enter code access\n'))
languages = ['python', 'cpp', 'java', 'c#', 'javascript', 'go', 'pascal', 'basic']
count = []
succs = 0
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
    for i in languages:
        try:
            data = a.json()
            dat = data['total_count']
            count.append(data['total_count'])
            succs = 1
        except KeyError:
            succs = 0
        except:
            print(Fore.RED + 'Unknown error')
            succs = 0
    if(succs == 1):
        time.sleep(1)
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
if(password != 2 and password !=1):
    print(Fore.RED + 'YOU DON’T HAVE ACCESS')
def plot():
    plt.bar(languages, count)
    plt.title('Языки программирования')
    plt.xlabel('Языки')
    plt.ylabel('Количество проектов')
    plt.show()
