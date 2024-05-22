import Classes.staff
from Classes import staff,tables,menu,boss
import asyncio
import os
import time
import threading
import tkinter.messagebox as mb
import random
import os


menu =  menu.Menu()
player = boss.owner()
Staff_list = player.personal
Tables_list = player.tabless
busyTable = []
freeStaff = []
player.stat()

Free = [Tables_list[0]]
def generate_order():
    while True:

        for table in Tables_list:
            if table.free:
                Free.append(table)
                if table in busyTable:
                    busyTable.remove(table)
        if len(Free) >= 1:
            rtime = random.randint(5, 10)
            time.sleep(rtime)
            order = random.choice(Free)
            Free.remove(order)
            order.take_order(menu, player)
            busyTable.append(order.id)
            busyTable.sort()

            for i in busyTable:
                if busyTable.count(i) > 1:
                    for j in range(busyTable.count(i) - 1):
                        busyTable.pop(busyTable.index(i))
order_thread = threading.Thread(target=generate_order)
order_thread.start()

def main():
    while True:
        print('\n' * 50)
        freeStaff.sort()
        print('________________________________________________')
        print(f'1: Взять заказ\n'
              f'2: Повысить уровень игрока\n'
              f'3: Повысить лвл персонала\n'
              f'4: Купить персонал\n'
              f'5: Купить столик\n'
              f'6: Статистика')
        print('________________________________________________')
        for i in Staff_list:
            if i.busy==False and i.id not in freeStaff:
               freeStaff.append(i.id)
        a = int(input('Введите нужную функцию: '))
        print('\n' * 50)
        if a == 1:
            print('________________________________________________')
            print('Свободные рабочие:')
            for cooker in Staff_list:
                print(f'|{cooker.id}|{cooker}')
            print('________________________________________________')
            inp=int(input('Введите ID нужного сотрудника: \nИли введите 0 для выхода в меню '))
            if inp == 0:
                main()
            while inp not in freeStaff:
                    inp=int(input('Данный сотрудник занят/не существует. Повторите ввод: \nИли введите 0 для выхода в меню '))
                    if inp == 0:
                        main()
            print('\n' * 50)
            print('________________________________________________')
            print('Выберите стол:')
            for i in busyTable:
                print(Tables_list[i-1].info())
            print('________________________________________________')
            inp2=int(input('Введите номер нужного стола\nИли введите 0 для выхода в меню: '))
            if inp2 == 0:
                main()
            while inp2 not in busyTable:
                if inp2 == 0:
                    main()
                inp2=int(input('Данный стол свободен/не существует. Повторите ввод: '))
            Tables_list[inp2-1].free=True
            thread = threading.Thread(target=Staff_list[inp-1].cook, args=(Tables_list[inp2-1], player))
            thread.start()
            busyTable.pop(busyTable.index(inp2))
            freeStaff.pop(freeStaff.index(inp))
        if a == 2:
            inp = input(f'Вы уверены? Это будет стоить {400*player.lvl}₽\n(1-да/0-нет) ')
            while inp not in ['1', '0']:
                inp = input("Некорекнтный ввод. Попробуйте ещё раз: ")
            if inp == '0':
                main()
            else:
                player.bosslvlup()
        if a == 3:
            print('________________________________________________')
            print('Список рабочих:')
            for cooker in Staff_list:
                print(f'|{cooker.id}|{cooker}')
            print('________________________________________________')
            inp=int(input('Введите ID нужного сотрудника: \nИли введите 0 для выхода в меню '))
            if inp == 0:
                main()
            while inp not in Staff_list:
                    inp=int(input('Данный сотрудник не существует. Повторите ввод\nИли введите 0 для выхода в меню '))
                    if inp == 0:
                        main()
            else:
                player.personlvlup(Staff_list[inp-1])
        if a==4:
            inp = input(f'Вы уверены? Это будет стоить {500}₽\n(1-да/0-нет) ')
            while inp not in ['1', '0']:
                inp = input("Некорекнтный ввод. Попробуйте ещё раз:")
            if inp == '0':
                main()
            else:
                player.buynewperson(staff.Staff())
        if a==5:
            inp = input(f'Вы уверены? Это будет стоить {300}₽\n(1-да/0-нет) ')
            while inp not in ['1', '0']:
                inp = input("Некорекнтный ввод. Попробуйте ещё раз:")
            if inp == '0':
                main()
            else:
                player.buynewtable(tables.Table())
        if a == 6:
            mb.showinfo(title='CТАТИСТИКА', message=player.stat())

main()