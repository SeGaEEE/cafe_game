from Classes import staff, tables
import tkinter.messagebox as mb

class owner:
    def __init__(self):
        self.xp = 0
        self.money = 100
        self.lvl = 1
        self.personal = [staff.Staff()]
        self.tabless = [tables.Table()]

    def stat(self):
        return (f'Ваш опыт: {self.xp} XP.\nВаш баланс: {self.money}₽\nВаш уровень: {self.lvl}')

    def personlvlup(self, person):
        if self.money >= (200 * person.level) and self.xp >= (10 * person.level) and person.level < 5:
            mb.showinfo(title='Повышение уровня повара',
                message=f'Вы повысили уровень с {person.level} до {person.level + 1} у: {person.name}\nС вашего баланса списано: {200 * person.level}₽\nОстаток: {self.money}₽')
            self.money -= 200 * person.level
            person.level += 1
        elif self.money < (200 * person.level) and self.xp < (10 * person.level):
            mb.showinfo(title='Повышение уровня повара',
                        message=f'Вам не хватает опыта и денег для повышения уровня у {person.name}. Вам нужно: {(200 * person.level) - self.money}₽\n{(10 * person.level) - self.xp} XP')
        elif self.money < 200 * person.level:
            mb.showinfo(title='Повышение уровня повара',
                        message= f'Вам не хватает опыта и денег для повышения уровня у {person.name}. Вам нужно ещё: {(200 * person.level) - self.money}₽')
        elif self.xp < 10 * person.level:
            mb.showinfo(title='Повышение уровня повара',
                        message=  f'Вам не хватает опыта и денег для повышения уровня у {person.name}. Вам нужно: {(10 * person.level) - self.xp} XP')
        elif person.level >= 5:
            mb.showinfo(title='Повышение уровня повара',message= f'{person.name} уже имеет максимальный уровень')
    def bosslvlup(self):
        if self.lvl > 1:
            if self.money >= (400 * self.lvl) and self.xp >= (20 * self.lvl):
                mb.showinfo(title='Повышение уровня игрока',
                    message=  f'Поздравляем, Вы перешли на новый {self.lvl} уровень!\nДоступны новые блюда в меню!\nС вашего баланса списано: {20 * self.lvl}₽\nОстаток: {self.money - 20 * self.lvl}₽')
                self.money -= 400 * self.lvl
                self.lvl += 1
            elif self.money < (self.xp >= (400 * self.lvl)) and self.xp < (400 * self.lvl):
                mb.showinfo(title='Повышение уровня игрока',
                    message=  f'Вам не хватает опыта и денег для повышения уровня. Вам нужно: {(400 * self.lvl) - self.money}₽\n{(400 * self.lvl) - self.xp} XP')
            elif self.money < 400 * self.lvl:
                mb.showinfo(title='Повышение уровня игрока',
                    message= f'Вам не хватает денег для повышения уровня. Вам нужно ещё: {(400 * self.lvl) - self.money}₽')
            elif self.xp < 400 * self.lvl:
                mb.showinfo(title='Повышение уровня игрока',
                    message=   f'Вам не хватает опыта для повышения уровня. Вам нужно: {(400 * self.lvl) - self.xp} XP')
        else:
            if self.money >= (400 * self.lvl):
                mb.showinfo(title='Повышение уровня игрока',
                   message= f'Вы повысили уровень с {self.lvl} до {self.lvl + 1}\nС вашего баланса списано: {400 * self.lvl}\nОстаток: {self.money - 400 * self.lvl}')
                self.money -= 400 * self.lvl
                self.lvl += 1
            elif self.money < 400 * self.lvl:
                mb.showinfo(title='Повышение уровня игрока',
                 message=f'Вам не хватает денег для повышения уровня. Вам нужно ещё: {(400 * self.lvl) - self.money}₽')

    def buynewperson(self, person):
        if self.money >= 500 and len(self.personal) <= self.lvl:
            self.personal.append(person)
            self.money -= 500
            mb.showinfo(title='Покупка повара',
                message= f'Вы успешно наняли повара.\nС вашего баланса списано 500₽\nОстаток по балансу: {self.money - 500}\nКоличество кадров: {len(self.personal)}')
        elif self.money < 500 and len(self.personal) <= self.lvl:
            mb.showinfo(title='Покупка повара',
                message= f'Вам не хватает уровня и денег для покупки повара. Вам нужно: {500 - self.money}₽ и +1 LVL')
        elif self.money < 500:
            mb.showinfo(title='Покупка повара',
                message= f'Вам не хватает денег для покупки повара. Вам нужно: {500 - self.money}₽')
        elif self.lvl <= 500:
            mb.showinfo(title='Покупка повара',
                message= f'Вам не хватает уровня для покупки повара. Вам нужен еще 1 LVL')

    def buynewtable(self, table):
        if self.money >= 300 and len(self.tabless) <= self.lvl + 1:
            self.tabless.append(table)
            self.money -= 300
            mb.showinfo(title="Покупка столика",
               message=  f'Вы успешно приобрели стол.\nС вашего баланса списано 300₽\nОстаток по балансу: {self.money - 300}\nКоличество столов: {len(self.tabless)}')
        elif self.money < 300 and len(self.tabless) <= self.lvl + 1:
            mb.showinfo(title="Покупка столика",
                message= f'Вам не хватает уровня и денег для покупки стола. Вам нужно: {300 - self.money}₽\n+1 LVL')
        elif self.money < 300:
            mb.showinfo(title="Покупка столика",
                message= f'Вам не хватает денег для покупки стола. Вам нужно: {300 - self.money}₽')
        elif self.lvl <= 300:
            mb.showinfo(title="Покупка столика",
                message= f'Вам не хватает уровня для покупки стола. Вам нужен еще 1 LVL')
