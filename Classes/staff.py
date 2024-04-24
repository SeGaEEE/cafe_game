import random
import asyncio
import time
import asyncio
import itertools
from Classes import menu, tables, boss
class Staff:
    staffID=itertools.count(1)
    def __init__(self):
        self.id = int(next(Staff.staffID))
        self.level = 1
        self.busy = False
        self.worktime = 35 - (self.level * 5)
        self.name = random.choice(['Саша', 'Петя', 'Вася', 'Дима'])
    def __str__(self):
        return (f'Работник {self.name} ✪ {self.level}')
    async def cook(self, table,boss):
        if not self.busy:
            active_order = [table.order,table.payment]
            print(f'Работник {self.name} взял заказ со столика №{table.id} \n'
                  f'Заказ: {active_order[0]} \n'
                  f'Оплата: {active_order[1]} \n'
                  f'Время выполнения заказа: {self.worktime} \n')
            await asyncio.sleep(self.worktime-27)
            boss.money+=active_order[1]
            boss.xp+=self.level
            table.free=True
            print(f'Работник {self.name} выполнил заказ столика №{table.id} \n'
                  f'Время затраченное выполнения заказа: {self.worktime}')

