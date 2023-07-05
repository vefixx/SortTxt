from colorama import Fore, Style, init
import time
import os

init()

RED = Fore.RED
GREEN = Fore.GREEN
RESET = Style.RESET_ALL
YELLOW = Fore.YELLOW

custom_donate = []

#main


def loadSettings(param):
    global custom_donate
    if param == 'HolyWorld':
        with open(rf'templeFiles\HolyWorldSettings.txt', 'r') as settings:
            setting = settings.readline()
            donates = setting.split(', ')
            custom_donate = donates
            return custom_donate
        
    elif param == 'SelfSettings':
        with open(rf'settings\DonateSettings.txt', 'r') as settings:
            setting = settings.readline()
            donates = setting.split(', ')
            custom_donate = donates
            return custom_donate
        
    elif param == 'ReallyWorld':
        with open(rf'templeFiles\ReallyWorldSettings.txt', 'r') as settings:
            setting = settings.readline()
            donates = setting.split(', ')
            custom_donate = donates
            return custom_donate




def input_loop():
    stop = None
    print('2 - настройки для HolyWorld')
    print('3 - настройки для ReallyWorld')
    print('4 - свои настройки из файла DonateSettings.txt')
    print()
    while stop != False:
        
        input1 = str(input("Введите название доната без ошибок (напишите '0' чтобы продолжить / '1' - удалить запись): "))
        if input1 == '0':
            stop = False
        elif input1 == '1':
            print("Список добавленных донатов:")
            print(custom_donate)
            input2 = str(input("Введите название доната, который вы хотите удалить: "))
            try:
                custom_donate.remove(input2)
            except:
                print("Ошибка, возможно вы ввели несуществующий донат..")
        elif input1 == '2':
            print('Загрузка настроек базовых настроек HolyWorld')
            loadSettings('HolyWorld')
            print('Готово')
            return True
        elif input1 == '3':
            print('Загрузка настроек базовых настроек ReallyWorld')
            loadSettings('ReallyWorld')
            print('Готово')
            return True

        elif input1 == '4':
            print('Загрузка пользовательских настроек..')
            loadSettings('SelfSettings')
            print('Готово')
            return True


        else:
            if input1 in custom_donate:
                print("Вы уже добавили этот донат в список")
            else:
                custom_donate.append(input1)
                print("Донат добавлен!", custom_donate)
                
    #выход из цикла
    print('-------------------------')
    print("Список донатов:")
    print(custom_donate)
    print('-------------------------')



def getFullLogs(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return lines


def main(lines):
    len_donate = len(custom_donate)
    count = 0
    while count < len_donate:  # Изменено условие
        donate = custom_donate[count]
        with open(fr'ReadyLogs\{donate}Data.txt', 'w') as output_file:
            for line in lines:
                parsed_line = line.strip()
                parsed_list_line = parsed_line.split()

                if len(parsed_list_line) > 0:
                    if parsed_list_line[0].lower() == donate:
                        output_file.write(parsed_line + '\n')

        count += 1

def getCountLogsInFiles(list_donate):
    print('\n')
    for donate in list_donate:
        with open(fr'ReadyLogs\{donate}Data.txt', 'r', encoding='cp1251') as file:
            lines = file.readlines()
        print(f'Количество игроков с донатом {donate}: {len(lines)}')    
        if len(lines) < 1:
            os.remove(fr'ReadyLogs\{donate}Data.txt')
            

while True:

    input_loop()
    lines = getFullLogs('logs.txt')
    time.sleep(0.5)
    main(lines)
    getCountLogsInFiles(custom_donate)
    time.sleep(0.5)
    print('\n','-------------------------------','\n')







