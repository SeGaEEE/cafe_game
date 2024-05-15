from Classes import staff,tables
class owner:
    def __init__(self):
        self.xp=1000
        self.money=1000
        self.lvl=1
        self.personal=[staff.Staff()]
        self.tabless=[tables.Table()]
    def stat(self):
        print(f'Ваш опыт: {self.xp} XP.\nВаш баланс: {self.money}$\nВаш уровень: {self.lvl}')
    def personlvlup(self,person):
        if self.money>=(10*person.level) and self.xp>=(10*person.level):
            print(f'Вы повысили уровень с {person.level} до {person.level+1} у: {person.name}\nС вашего баланса списано: {10*person.level}\nОстаток: {self.money}')
            person.level+=1
            self.money-=10*person.level
        elif self.money<(10*person.level) and self.xp<(10*person.level):
            print(f'Вам не хватает опыта и денег для повышения уровня у {person.name}. Вам нужно: {(10*person.level)-self.money}$\n{(10*person.level)-self.xp} XP')
        elif self.money<10*person.level:
            print(f'Вам не хватает опыта и денег для повышения уровня у {person.name}. Вам нужно ещё: {(10*person.level)-self.money}$')
        elif self.xp<10*person.level:
            print(f'Вам не хватает опыта и денег для повышения уровня у {person.name}. Вам нужно: {(10 * person.level) - self.xp} XP')
    def bosslvlup(self):
        if self.lvl>1:
            if self.money>=(20*self.lvl) and self.xp>=(20*self.lvl):
                print(f'Поздравляем, Вы перешли на новый {self.lvl} уровень!\nДоступны новые блюда в меню!\nС вашего баланса списано: {20*self.lvl}\nОстаток: {self.money-20*self.lvl}')
                self.lvl+=1
                self.money-=20*self.lvl
            elif self.money<(self.xp>=(20*self.lvl)) and self.xp<(20*self.lvl):
                print(f'Вам не хватает опыта и денег для повышения уровня. Вам нужно: {(20*self.lvl)-self.money}$\n{(20*self.lvl)-self.xp} XP')
            elif self.money<20*self.lvl:
                print(f'Вам не хватает денег для повышения уровня. Вам нужно ещё: {(20*self.lvl)-self.money}$')
            elif self.xp<20*self.lvl:
                print(f'Вам не хватает опыта для повышения уровня. Вам нужно: {(20*self.lvl) - self.xp} XP')
        else:
            if self.money>=(20*self.lvl):
                print(f'Вы повысили уровень с {self.lvl} до {self.lvl+1}\nС вашего баланса списано: {20*self.lvl}\nОстаток: {self.money-20*self.lvl}')
                self.lvl+=1
                self.money-=20*self.lvl
            elif self.money<20*self.lvl:
                print(f'Вам не хватает денег для повышения уровня. Вам нужно ещё: {(20*self.lvl)-self.money}$')

    def buynewperson(self,person):
            if self.money>=30 and self.lvl>=2:
                self.personal.append(person)
                self.money-=30
                print(f'Вы успешно наняли официанта.\nС вашего баланса списано 30$\nОстаток по балансу: {self.money-30}\nКоличество кадров: {len(self.personal)}')
            elif self.money<30 and self.lvl<2:
                print(f'Вам не хватает уровня и денег для покупки персонала. Вам нужно: {30-self.money}$ и +1 LVL')
            elif self.money<30:
                print(f'Вам не хватает денег для покупки персонала. Вам нужно: {30 - self.money}$')
            elif self.lvl<=30:
                print(f'Вам не хватает уровня для покупки персонала. Вам нужен еще 1 LVL')
    def buynewtable(self,table):
        if self.money>=30 and self.lvl>=2:
            self.tabless.append(table)
            self.money-=30
            print(f'Вы успешно приобрели стол.\nС вашего баланса списано 30$\nОстаток по балансу: {self.money-30}\nКоличество столов: {len(self.tabless)}')
        elif self.money<30 and self.lvl<=2:
            print(f'Вам не хватает уровня и денег для покупки стола. Вам нужно: {30-self.money}$\n+1 LVL')
        elif self.money<30:
            print(f'Вам не хватает денег для покупки стола. Вам нужно: {30 - self.money}$')
        elif self.lvl<=30:
            print(f'Вам не хватает уровня для покупки стола. Вам нужен еще 1 LVL')
