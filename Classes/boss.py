
class owner:
    def __init__(self):
        self.xp=0
        self.money=0
        self.lvl=1
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
