from Classes import staff,tables,menu,boss
import asyncio
import os
menu = menu.Menu
clear = lambda: os.system('cls')
clear()
Boss=boss.owner()
Vasya = staff.Staff()
t1 = tables.Table()
Boss.stat()
while True:
    print(f'\n1: Новый заказ\n'
          f'2: Повысить уровень игрока\n'
          f'3: Повысиль лвл персонала\n'
          f'4: купить персонал\n '
          f'5: купить столик\n'
          f'6: Статистика')
    a = int(input())
    if a == 1:
        clear()
        asyncio.run(Vasya.cook(t1, Boss))

    if a == 2:
        clear()
        print(Boss.bosslvlup())
    if a == 3:
        clear()
        print(Boss.personlvlup())
    if a == 6:
        clear()
        print(Boss.stat())

