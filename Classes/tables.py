import itertools
class Table:
    tableID = itertools.count(1)
    def __init__(self):
        self.id = next(Table.tableID)
        self.order=''
        self.payment=0
        self.free=True
    def take_order(self,menu,boss):
        if self.free:
            orders=menu.takeorder(boss)
            self.order=orders[0]
            self.payment=orders[1]
            self.free=False
            print(f'За столом: {self.id} сделали заказ: {self.order}')
    def __str__(self):
        return f'Заказ: {self.order}. Оплата: {self.payment}. Принести за {self.id} столик.'

