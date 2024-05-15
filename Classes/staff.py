import random
from time import sleep
import itertools
import tkinter.messagebox as mb

class Staff:
    staffID=itertools.count(1)
    def __init__(self):
        self.id = int(next(Staff.staffID))
        self.level = 1
        self.busy = False
        self.worktime = 25 - (self.level * 5)
        self.name = random.choice(['Саша', 'Петя', 'Вася', 'Дима'])
    def __str__(self):
        return (f'Работник {self.name} ✪ {self.level}')
    def cook(self, table,boss):
        self.busy = True
        print(123)
        active_order = [table.order,table.payment]
        msg = f'Работник {self.name} взял заказ со столика №{table.id} \n Заказ: {active_order[0]} \n Оплата: {active_order[1]} \n Время выполнения заказа: {self.worktime} секунд'
        mb.showinfo(title="Заказ взят", message=msg)
        sleep(self.worktime)
        boss.money+=active_order[1]
        boss.xp+=self.level
        table.free=True
        msg = f'\n Работник {self.name} выполнил заказ столика №{table.id} \nВремя затраченное выполнения заказа: {self.worktime} секунд'
        mb.showinfo(title="Заказ выполнен", message=msg)
        self.busy = False

