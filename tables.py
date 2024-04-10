import itertools
class Table:
    tableID = itertools.count()
    def __init__(self):
        self.id = next(Table.tableID)
        self.order=''
        self.payment=0
        self.free=True
    def new_order(self,menu):
        order=menu.takeorder()
        self.order=order[0]
        self.payment=order[1]
        self.free=False
    def take_order(self):
        return [self.order,self.payment]
    def __str__(self):
        return f'Заказ: {self.order}. Оплата: {self.payment}. Принести за {self.id} столик.'

