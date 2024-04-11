from tables import Table
import random
import asyncio
import time
import asyncio
class Staff:
    def __init__(self):
        self.level = 12
        self.busy = False
        self.worktime = 65 - (self.level * 5)
        self.name = random.choice(['Саша', 'Петя', 'Вася', 'Дима'])
    def __str__(self):
        return (f'Работник {self.name} ✪ {self.level}')
    async def cook(self, table):
        if not self.busy:
            active_order = table.take_order()
            print(f'Работник {self.name} взял заказ со столика №{table.id} \n'
                  f'Заказ: {active_order[0]} \n'
                  f'Оплата: {active_order[1]} \n'
                  f'Время выполнения заказа: {self.worktime} \n')
            await asyncio.sleep(self.worktime)
            print(f'Работник {self.name} выаолнил заказ столика №{table.id} \n'
                  f'Заказ: {active_order[0]} \n'
                  f'Оплата: {active_order[1]} \n'
                  f'Время выполнения заказа: {self.worktime}')


d = Staff()
t = Table()
print(d)
asyncio.run(d.cook(t))