
class owner:
    def __init__(self):
        self.xp=0
        self.money=0
        self.lvl=1
        self.personal=[]
        self.table=[]
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
        if self.money>=(20*self.lvl) and self.xp>=(20*self.lvl):
            print(f'Вы повысили уровень с {self.lvl} до {self.lvl+1}\nС вашего баланса списано: {20*self.lvl}\nОстаток: {self.money}')
            self.lvl+=1
            self.money-=20*self.xp
        elif self.money<(self.xp>=(20*self.lvl)) and self.xp<(20*self.lvl):
            print(f'Вам не хватает опыта и денег для повышения уровня. Вам нужно: {(20*self.lvl)-self.money}$\n{(20*self.lvl)-self.xp} XP')
        elif self.money<20*self.lvl:
            print(f'Вам не хватает опыта и денег для повышения уровня. Вам нужно ещё: {(20*self.lvl)-self.money}$')
        elif self.xp<20*self.lvl:
            print(f'Вам не хватает опыта и денег для повышения уровня. Вам нужно: {(20*self.lvl) - self.xp} XP')
    def buynewperson(self,person):
        if self.money>=30 and self.lvl>=2:
            self.personal.append(person)
            self.money-=30
            print(f'Вы успешно приобрели официанта.\nС вашего баланса списано 30$\nОстаток по балансу: {self.money-30}\nКоличество кадров: {len(self.personal)}')
        elif self.money<30 and self.lvl<=2:
            print(f'Вам не хватает уровня и денег для покупки персонала. Вам нужно: {30-self.money}$\n+1 LVL')
        elif self.money<30:
            print(f'Вам не хватает денег для покупки персонала. Вам нужно: {30 - self.money}$')
        elif self.lvl<=30:
            print(f'Вам не хватает уровня для покупки персонала. Вам нужен еще 1 LVL')
    def buynewtable(self,table):
        if self.money>=30 and self.lvl>=2:
            self.table.append(table)
            self.money-=30
            print(f'Вы успешно приобрели стол.\nС вашего баланса списано 30$\nОстаток по балансу: {self.money-30}\nКоличество столов: {len(self.table)}')
        elif self.money<30 and self.lvl<=2:
            print(f'Вам не хватает уровня и денег для покупки стола. Вам нужно: {30-self.money}$\n+1 LVL')
        elif self.money<30:
            print(f'Вам не хватает денег для покупки стола. Вам нужно: {30 - self.money}$')
        elif self.lvl<=30:
            print(f'Вам не хватает уровня для покупки стола. Вам нужен еще 1 LVL')