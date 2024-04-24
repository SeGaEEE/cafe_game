import Classes.staff
from Classes import staff,tables,menu,boss
import asyncio
import os
menu = menu.Menu()

player=boss.owner()
Staff_list = [staff.Staff()]
Tables_list = [tables.Table()]




player.stat()
while True:
    busyTable = []
    freeStaff = []
    print(f'\n1: Взять заказ\n'
          f'2: Повысить уровень игрока\n'
          f'3: Повысиль лвл персонала\n'
          f'4: купить персонал\n '
          f'5: купить столик\n'
          f'6: Статистика')
    for i in Tables_list:
        if i.free:
            busyTable.append(i.id)
            i.take_order(menu=menu,boss=player)
    for i in Staff_list:
        if i.busy==False:
           freeStaff.append(i.id)
    a = int(input())
    if a == 1:
        if len(freeStaff)>=1:
            print('Свободные рабочие:')
            for i in freeStaff:
                print(f'ID-индетификатор сотрудника: {i}\nИмя: {Staff_list[i-1].name}\nУровень: {Staff_list[i-1].level}\n{"_"*50}')
            inp=int(input('Введите ID-индетификатор нужного сотрудника'))
            while inp not in freeStaff:
                    inp=int(input('Данный сотрудник занят/несуществует. Повторите ввод:'))
            print('Выберите стол:')
            for i in busyTable:
                print(f'Номер стола: {i}\nЗаказ: {Tables_list[i-1].order}\n{"_"*100}')
            inp2=int(input('Введите номер нужного стола:'))
            while inp2 not in busyTable:
                inp2=int(input('Данный стол свободен/несуществует. Повторите ввод:'))
            asyncio.run(Staff_list[inp-1].cook(Tables_list[inp2-1],player))



    if a == 2:
        player.bosslvlup()
    if a == 3:
        player.personlvlup()
    if a == 6:
        player.stat()

