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


def save():
    pass

while True:
    freeStaff.sort()
    print('\n' * 50)
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
        if len(freeStaff)>=1:
            print('________________________________________________')
            print('Свободные рабочие:')
            for cooker in Staff_list:
                if Staff_list.index(cooker) != len(Staff_list) - 1:
                    print(f'|{cooker.id}|{cooker}\n')
                else:
                    print(f'|{cooker.id}|{cooker}')
            print('________________________________________________')
            inp=int(input('Введите ID-индетификатор нужного сотрудника:'))
            while inp not in freeStaff:
                    inp=int(input('Данный сотрудник занят/несуществует. Повторите ввод: '))
            print('\n' * 50)
            print('________________________________________________')
            print('Выберите стол:')
            for i in busyTable:
                print(Tables_list[i-1].info())
            print('________________________________________________')
            inp2=int(input('Введите номер нужного стола: '))
            while inp2 not in busyTable:
                inp2=int(input('Данный стол свободен/несуществует. Повторите ввод:'))
            Tables_list[inp2-1].free=True
            busyTable.pop(busyTable.index(inp2))
            freeStaff.pop(freeStaff.index(inp))
            thread = threading.Thread(target=Staff_list[inp-1].cook, args=(Tables_list[inp2-1], player))
            thread.start()
        else:
            print('Все сотрудники заняты')
    if a == 2:
        player.bosslvlup()
    if a == 3:
        for cooker in Staff_list:
            print('________________________________________________')
            print(f'|{cooker.id}|{cooker}\n')
            print('________________________________________________')
        inp=int(input('Выберите сотрудника которому повысить уровень: '))
        player.personlvlup(Staff_list[inp-1])
    if a==4:
        player.buynewperson(staff.Staff())
    if a==5:
        player.buynewtable(tables.Table())
    if a == 6:
        mb.showinfo(title='CТАТИСТИКА', message=player.stat())

