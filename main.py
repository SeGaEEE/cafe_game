from Classes import staff,tables,menu,boss
import asyncio
import os
menu = menu.Menu

Boss=boss.owner()
Staff_list = [staff.Staff()]
Tables_list = [tables.Table()]

Boss.stat()
while True:
    freeTable = []
    freeStaff = []
    print(f'\n1: Взять заказ\n'
          f'2: Повысить уровень игрока\n'
          f'3: Повысиль лвл персонала\n'
          f'4: купить персонал\n '
          f'5: купить столик\n'
          f'6: Статистика')
    for i in Tables_list:
        if i.free:
            freeTable.append(i)
            i.take_order(menu,Boss)

    a = int(input())
    if a == 1:

    if a == 2:
        print(Boss.bosslvlup())
    if a == 3:
        print(Boss.personlvlup())
    if a == 6:
        print(Boss.stat())

