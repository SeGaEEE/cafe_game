import Classes.staff
from Classes import staff,tables,menu,boss
import asyncio
import os
menu = menu.Menu()

player=boss.owner()
Staff_list = player.personal
Tables_list = player.tabless

busyTable = []
freeStaff = []
player.stat()
while True:
    busyTable.sort()
    freeStaff.sort()
    print(f'\n1: Взять заказ\n'
          f'2: Повысить уровень игрока\n'
          f'3: Повысить лвл персонала\n'
          f'4: Купить персонал\n'
          f'5: Купить столик\n'
          f'6: Статистика')
    for i in Tables_list:
        if i.free:
            busyTable.append(i.id)
            i.take_order(menu=menu,boss=player)
    for i in Staff_list:
        if i.busy==False and i.id not in freeStaff:
           freeStaff.append(i.id)
    print("_"*220)
    a = int(input('Введите нужную функцию: '))
    print("_"*220)
    if a == 1:
        if len(freeStaff)>=1:
            print('Свободные рабочие:')
            for i in freeStaff:
                print(f'ID-индетификатор сотрудника: {i}\nИмя: {Staff_list[i-1].name}\nУровень: {Staff_list[i-1].level}\n{"_"*220}')
            inp=int(input('Введите ID-индетификатор нужного сотрудника: '))
            while inp not in freeStaff:
                    inp=int(input('Данный сотрудник занят/несуществует. Повторите ввод: '))
            print('Выберите стол:')
            for i in busyTable:
                print(f'Номер стола: {i}\nЗаказ: {Tables_list[i-1].order}\n{"_"*220}')
            inp2=int(input('Введите номер нужного стола: '))
            while inp2 not in busyTable:
                inp2=int(input('Данный стол свободен/несуществует. Повторите ввод:'))
            Tables_list[inp2-1].free=True
            busyTable.pop(inp2-1)
            asyncio.run(Staff_list[inp-1].cook(Tables_list[inp2-1],player))



    if a == 2:
        player.bosslvlup()
    if a == 3:
        for i in Staff_list:
            print(f'ID-индетификатор сотрудника: {i}\nИмя: {i.name}\nУровень: {i.level}\n{"_"*220}')
        inp=int(input('Выберите сотрудника которому повысить уровень: '))
        player.personlvlup(Staff_list[inp-1])
    if a==4:
        player.buynewperson(staff.Staff())
    if a==5:
        player.buynewtable(tables.Table())
    if a == 6:
        player.stat()

