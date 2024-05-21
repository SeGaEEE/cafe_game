import random
from time import sleep
import itertools
import tkinter.messagebox as mb

class Staff:
    staffID = itertools.count(1)
    def __init__(self):
        self.id = int(next(Staff.staffID))
        self.level = 1
        self.busy = False
        self.worktime = 30 - (self.level * 5)
        self.name = random.choice(['Александр', 'Петр', 'Василий', 'Дмитрий', 'Артур', 'Павел', 'Владислав', 'Владимир', 'Иван', 'Савелий', 'Даниил',  'Роман', 'Илья', 'Егор', 'Кирилл',])
    def __str__(self):
        if self.busy:
            return (f'{self.name} (yр.{self.level})|ЗАНЯТ')
        else:
            return (f'{self.name} (yр.{self.level})|CBOБОДЕН')
    def cook(self, table,boss):
        self.busy = True
        table.free = False
        active_order = [table.order,table.payment]
        msg = f'Работник {self.name} взял заказ со столика №{table.id} \n Заказ: {active_order[0]} \n Оплата: {active_order[1]} \n Время выполнения заказа: {self.worktime} секунд'
        mb.showinfo(title="Заказ взят", message=msg)
        sleep(self.worktime)
        boss.money+=active_order[1] * self.level
        boss.xp+=5 * self.level
        msg = f'\n Работник {self.name} выполнил заказ столика №{table.id} \nВремя затраченное выполнения заказа: {self.worktime} секунд'
        mb.showinfo(title="Заказ выполнен", message=msg)
        self.busy = False
        table.free = True
