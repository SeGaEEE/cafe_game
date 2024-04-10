from tables import Table
import random
import time
import asyncio
class Staff:
    def __init__(self):
        self.level = 1
        self.busy = False
        self.worktime = 15 - (self.level * 5)
        self.name = random.choice(['Саша', 'Петя', 'Вася', 'Дима'])
    def __str__(self):
        return (f'Работник {self.name} ✪ {self.level}')
    def cook(self, table):
        if not self.busy:
            active_order = table.take_order()
            print(f'Работник {self.name} взял заказ со столика №{table.id} \n'
                  f'Заказ: {active_order[0]} \n'
                  f'Оплата: {active_order[1]} \n'
                  f'Время выполнения заказа: {self.worktime} \n')
            time.sleep(self.worktime)
            print(f'Работник {self.name} выаолнил заказ столика №{table.id} \n'
                  f'Заказ: {active_order[0]} \n'
                  f'Оплата: {active_order[1]} \n'
                  f'Время выполнения заказа: {self.worktime}')
