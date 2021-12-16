from colorama import Fore

print(Fore.LIGHTWHITE_EX + '\nWait...\n')

import requests
import matplotlib.pyplot as plt
import time
import re
import speedtest

password = 0
st = speedtest.Speedtest()
speed_int = 0

def toFixedDownload(download, digits=2):
    return f"{download:.{digits}f}"

def toFixedUpload(upload, digits=2):
    return f"{upload:.{digits}f}"

while True:
    try:
        time.sleep(0.3)
        password = int(input(Fore.LIGHTCYAN_EX + 'Enter the mode\n' + Fore.CYAN + '1 - standart' +  Fore.RESET + ' or ' + Fore.CYAN + '2 - fast\n'))
        if(password != 1) and (password != 2):
            print(Fore.RED + 'Error ' + Fore.LIGHTRED_EX + '(Invalid number)')
            time.sleep(0.2)
            print(Fore.WHITE + 'Please, try again')
        else:
            break
    except ValueError:
        print(Fore.RED + 'Error ' + Fore.LIGHTRED_EX + '(Incorrect data)')
        time.sleep(0.2)
        print(Fore.WHITE + 'Please, try again\n')

def choose_speed():
    global speed_int, show_would_check_speed
    while True:
        print(Fore.LIGHTWHITE_EX + '\nChoose point\n')
        print(Fore.CYAN + '1 - download speed\n2 - upload speed\n3 - all information')
        try:
            speed_int = int(input())
            if(speed_int != 1) and (speed_int != 2) and (speed_int != 3):
                print(Fore.RED + 'Error ' + Fore.LIGHTRED_EX + '(Invalid number)')
                time.sleep(0.2)
                print(Fore.WHITE + 'Please, try again')
            if(speed_int == 1) or (speed_int == 2) or (speed_int == 3):
                show_would_check_speed = 1
                speedtest()
                break
        except ValueError:
            print(Fore.RED + 'Error ' + Fore.LIGHTRED_EX + '(ValueError)')
            time.sleep(0.3)
            print(Fore.WHITE + 'Please, try again')
        except:
            print(Fore.LIGHTRED_EX + 'Unknown error')
            time.sleep(0.3)
            print(Fore.WHITE + 'Please, try again')

def speedtest():
    global speed_int, st
    if(speed_int == 1):
        print(Fore.RESET + '\nYou choise download speed\n')
        time.sleep(0.2)
        print(Fore.GREEN + 'Connecting.', end='')
        time.sleep(0.25)
        print(Fore.GREEN + '.', end='')
        time.sleep(0.45)
        print(Fore.GREEN + '.', end='')
        time.sleep(0.25)
        print(Fore.GREEN + '.', end='')
        time.sleep(0.65)
        print(Fore.GREEN + '.', end='')
        time.sleep(0.25)
        print(Fore.LIGHTGREEN_EX + "\nSUCCESSFUL CONNECTION!")
        print(Fore.WHITE + '\nWait...')
        download = ((st.download()/1024) / 1024)
        print(Fore.LIGHTWHITE_EX + f'Download speed = {toFixedDownload(download)} Mbit/s')

    if(speed_int == 2):
        print(Fore.RESET + '\nYou choise upload speed\n')
        time.sleep(0.2)
        print(Fore.GREEN + 'Connecting.', end='')
        time.sleep(0.25)
        print(Fore.GREEN + '.', end='')
        time.sleep(0.45)
        print(Fore.GREEN + '.', end='')
        time.sleep(0.25)
        print(Fore.GREEN + '.', end='')
        time.sleep(0.65)
        print(Fore.GREEN + '.', end='')
        time.sleep(0.25)
        print(Fore.LIGHTGREEN_EX + "\nSUCCESSFUL CONNECTION!")
        print(Fore.WHITE + '\nWait...')
        upload = ((st.upload() / 1024) / 1024)
        print(Fore.LIGHTWHITE_EX + f'Upload speed = {toFixedUpload(upload)} Mbit/s')

    if(speed_int == 3):
        print(Fore.RESET + '\nYou choise all information\n')
        time.sleep(0.2)
        print(Fore.GREEN + 'Connecting.', end='')
        time.sleep(0.25)
        print(Fore.GREEN + '.', end='')
        time.sleep(0.45)
        print(Fore.GREEN + '.', end='')
        time.sleep(0.25)
        print(Fore.GREEN + '.', end='')
        time.sleep(0.65)
        print(Fore.GREEN + '.', end='')
        time.sleep(0.25)
        print(Fore.LIGHTGREEN_EX + "\nSUCCESSFUL CONNECTION!")
        print(Fore.WHITE + '\nWait...')
        download = ((st.download() / 1024) / 1024)
        print(Fore.LIGHTWHITE_EX + f'Download speed = {toFixedDownload(download)} Mbit/s')
        print(Fore.WHITE + '\nWait...')
        upload = ((st.upload() / 1024) / 1024)
        print(Fore.LIGHTWHITE_EX + f'Upload speed = {toFixedUpload(upload)} Mbit/s')

show_would_check_speed = 0

if(show_would_check_speed == 0):
    while True:
        time.sleep(0.3)
        print(Fore.CYAN + '\nWould you like to check your internet speed before starting the program?\n' + Fore.GREEN + '1 - Yes' + Fore.RESET + ' or ' + Fore.RED + '2 - No')
        try:
            would_speed_test = int(input())
            if (would_speed_test != 1) and (would_speed_test != 2):
                print(Fore.RED + 'Error ' + Fore.LIGHTRED_EX + '(Invalid number)')
                time.sleep(0.2)
                print(Fore.WHITE + 'Please, try again')
            if(would_speed_test == 2):
                break
            if(would_speed_test == 1):
                choose_speed()
                break

        except ValueError:
            print(Fore.RED + 'Error ' + Fore.LIGHTRED_EX + '(ValueError)')
            time.sleep(0.3)
            print(Fore.WHITE + 'Please, try again')
        except:
            print(Fore.LIGHTRED_EX + 'Unknown error')
            time.sleep(0.3)
            print(Fore.WHITE + 'Please, try again')
            exit(0)

errors = 0
num = 0
languages = []
count = []
succs = 0
number_c = 1
custom_language = 2
exit_graph = 0
prov_array = ['cpp', 'java', 'python', 'javascript', 'pascal', 'php', 'basic', 'ruby', 'c++', 'css', 'c#', 'c', 'go', 'json', 'typescript', 'swift', 'scala', 'Objective-C', 'shell'] #НУЖНО БУДЕТ ПОПОЛНЯТЬ
proverka_caps = ''
prov_array_number = 0
HorV = 0

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
    global errors, num, succs
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
        print(Fore.LIGHTWHITE_EX + "\nSUCCESSFUL!")
    else:
        pass

while True:
    print(Fore.BLUE + f'\nEnter the programming language you need\nAlready entered: {number_c-1}')
    time.sleep(0.2)
    print(Fore.MAGENTA + 'To stop typing, enter 0')
    custom_language = input()
    prov_array_number = 0
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
    if(custom_language not in prov_array) and (custom_language not in languages):
        while True:
            print(Fore.YELLOW + '\nAre you sure you entered the programming language correctly?')
            print(Fore.LIGHTWHITE_EX + custom_language.upper())
            print(Fore.LIGHTGREEN_EX + '1 - YES' + Fore.RESET + ' or ' + Fore.LIGHTRED_EX + '2 - NO')
            try:
                prov_array_number = int(input())
            except ValueError:
                print(Fore.RED + 'Error ' + Fore.LIGHTRED_EX + '(ValueError)')
                time.sleep(0.3)
                print(Fore.WHITE + 'Please, try again')
            except:
                print(Fore.LIGHTRED_EX + 'Unknown error')
                time.sleep(0.3)
                print(Fore.WHITE + 'Please, try again')
            if(prov_array_number != 1) and (prov_array_number != 2):
                print(Fore.RED + 'Error ' + Fore.LIGHTRED_EX + '(Invalid number)')
                time.sleep(0.3)
                print(Fore.WHITE + 'Please, try again')
            if(prov_array_number == 1) or (prov_array_number == 2):
                break
    if(custom_language != 0) and (custom_language not in languages) and (not re.search("^\s*$", custom_language)) and (prov_array_number != 2):
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

def plot_stolb_h():
    global languages, count
    try:
        plt.barh(languages, count)
        plt.title('Языки программирования')
        plt.ylabel('Языки')
        plt.xlabel('Количество проектов')
        plt.show()
    except:
        exit(0)

grade = languages

def plot_pie():
    global languages, count
    plt.pie(count, labels = grade, autopct = '%2.3f%%', shadow='True')
    plt.show()

if(errors != 0):
    print(Fore.RED + 'Error' + Fore.LIGHTRED_EX + ' (Failed to build graph)')

if(errors == 0) and (num != 0):
    while True:
        try:
            time.sleep(0.6)
            WouldGraph = int(input(Fore.LIGHTCYAN_EX + '\nWould you like to display the graphic?\n' + Fore.LIGHTGREEN_EX + '1 - Yes ' + Fore.RESET + 'or' + Fore.RED + ' 2 - No\n'))
            if(WouldGraph != 1) and (WouldGraph != 2):
                print(Fore.RED + 'Error ' + Fore.LIGHTRED_EX + '(Invalid number)')
                time.sleep(0.3)
                print(Fore.WHITE + 'Please, try again')
            if(WouldGraph == 1):
                exit_graph = 0
                break
            if(WouldGraph == 2):
                print(Fore.LIGHTGREEN_EX + '\n\nThanks for using!')
                exit_graph = 1 #----------------------------------------------------------------------------------------для корректного выхода из программы
                break
        except ValueError:
            print(Fore.RED + 'Error' + Fore.LIGHTRED_EX + '(Value error)')
            time.sleep(0.3)
            print(Fore.WHITE + 'Please, try again')
        except:
            print(Fore.LIGHTRED_EX + 'Unknown error')
            time.sleep(0.3)
            print(Fore.WHITE + 'Please, try again')

    if(exit_graph == 1): #----------------------------------------------------------------------------------------------для корректного выхода из программы
        exit(0)

    while True:
        try:
            vvod_plot = int(input(Fore.LIGHTCYAN_EX + '\nWhat graphic do you want to display?\n' + Fore.CYAN +'1 - Bar graph' + Fore.RESET + ' or' + Fore.CYAN + ' 2 - Circular chart ' + Fore.RESET + 'or' + Fore.CYAN + ' 3 - All graphics\n'))
            if(vvod_plot != 1) and (vvod_plot != 2) and (vvod_plot != 3):
                print(Fore.RED + 'Error ' + Fore.LIGHTRED_EX + '(Invalid number)')
                time.sleep(0.3)
                print(Fore.WHITE + 'Please, try again')
            else:
                break
        except ValueError:
            print(Fore.RED + 'Error' + Fore.LIGHTRED_EX + '(Value error)')
            time.sleep(0.3)
            print(Fore.WHITE + 'Please, try again')
        except:
            print(Fore.LIGHTRED_EX + 'Unknown error')
            time.sleep(0.3)
            print(Fore.WHITE + 'Please, try again')

    if(vvod_plot == 1):
        try:
            while True:
                print(Fore.LIGHTCYAN_EX + '\nWhat graphic do you want to display?\n' + Fore.CYAN + '1 - vertical' + Fore.RESET + ' or ' + Fore.CYAN + '2 - horizontal?')
                try:
                    HorV = int(input())
                    if (HorV != 1) and (HorV != 2):
                        print(Fore.RED + 'Error' + Fore.LIGHTRED_EX + ' (Invalid number)')
                        time.sleep(0.3)
                        print(Fore.WHITE + 'Please, try again')
                except ValueError:
                    print(Fore.RED + 'Error' + Fore.LIGHTRED_EX + ' (Value error)')
                    time.sleep(0.3)
                    print(Fore.WHITE + 'Please, try again')
                except:
                    print(Fore.LIGHTRED_EX + 'Unknown error')
                    time.sleep(0.3)
                    print(Fore.WHITE + 'Please, try again')
                if(HorV == 1):
                    plot_stolb()
                    break
                if(HorV == 2):
                    plot_stolb_h()
                    break
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
            print(Fore.RED + '\nFailed to build graphic' + Fore.LIGHTRED_EX + ' (Value error)')
            exit(0)
        except:
            print(Fore.LIGHTRED_EX + 'Unknown error')
            exit(0)

    if(vvod_plot == 3):
        try:
            while True:
                print(Fore.LIGHTCYAN_EX + '\nWhat bar graphic do you want to display?\n' + Fore.CYAN + '1 - vertical' + Fore.RESET + ' or ' + Fore.CYAN + '2 - horizontal?' + Fore.RESET + ' or ' + Fore.CYAN + '3 - all')
                try:
                    HorV = int(input())
                    if(HorV != 1) and (HorV != 2) and (HorV != 3):
                        print(Fore.RED + 'Error' + Fore.LIGHTRED_EX + ' (Invalid number)')
                        time.sleep(0.3)
                        print(Fore.WHITE + 'Please, try again')
                except ValueError:
                    print(Fore.RED + 'Error' + Fore.LIGHTRED_EX + ' (Value error)')
                    time.sleep(0.3)
                    print(Fore.WHITE + 'Please, try again')
                except:
                    print(Fore.LIGHTRED_EX + 'Unknown error')
                    time.sleep(0.3)
                    print(Fore.WHITE + 'Please, try again')
                if(HorV == 1):
                    plot_stolb()
                    plot_pie()
                    break
                if(HorV == 2):
                    plot_stolb_h()
                    plot_pie()
                    break
                if(HorV == 3):
                    plot_stolb()
                    plot_stolb_h()
                    plot_pie()
                    break
        except ValueError:
            print(Fore.RED + '\nFailed to build graph' + Fore.LIGHTRED_EX + ' (Value error)')
            exit(0)
        except:
            print(Fore.LIGHTRED_EX + 'Unknown error')
            exit(0)
    print(Fore.LIGHTWHITE_EX + "\nSUCCESSFUL!")
    time.sleep(0.2)
    print(Fore.LIGHTRED_EX + f'\nTotal errors - {errors}')
    print(Fore.LIGHTGREEN_EX + '\n\nThanks for using!')

else:
    exit(0)
