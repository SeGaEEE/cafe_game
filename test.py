import random
from time import sleep
import itertools
import tkinter.messagebox as mb

class Staff:
    def __init__(self):
        self.level = 1
        self.busy = False
        self.worktime = 25 - (self.level * 5)
        self.name = random.choice(['Саша', 'Петя', 'Вася', 'Дима'])

    def __str__(self):
        return (f'Работник {self.name} ✪ {self.level}')

    def cook(self):
        if not self.busy:
            active_order = [1, 20]
            msg = f'Работник {self.name} взял заказ со столика №{1} \n Заказ: {active_order[0]} \n Оплата: {active_order[1]} \n Время выполнения заказа: {self.worktime}'
            mb.showinfo(title="Заказ взят", message=msg)
            sleep(self.worktime)
            print(123)
            msg = f'\n Работник {self.name} выполнил заказ столика №{1} \nВремя затраченное выполнения заказа: {self.worktime}'
            mb.showinfo(title="Заказ выполнен", message=msg)



a = Staff()
a.cook()