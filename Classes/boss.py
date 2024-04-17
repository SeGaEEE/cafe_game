import staff
class owner:
    def __init__(self):
        self.xp=0
        self.money=0
        self.lvl=1
    def personlvlup(self,person):
        if self.money>=(10*person.level) and self.xp>=(10*person.level):
            print(f'Вы повысили уровень с {person.level} до {person.level+1} у: {person.name}\nС вашего баланса списано: {10*person.level}\nОстаток: {self.money}')
        elif self.money<(10*person.level) and self.xp<(10*person.level):
            print(f'Вам не хватает опыта и денег для повышения уровня у {person.name}. Вам нужно: {(10*person.level)-self.money}$\n{(10*person.level)-self.xp} XP')
        elif self.money<10*person.level:
            print(f'Вам не хватает опыта и денег для повышения уровня у {person.name}. Вам нужно ещё: {(10*person.level)-self.money}$')
        elif self.xp<10*person.level:
            print(f'Вам не хватает опыта и денег для повышения уровня у {person.name}. Вам нужно: {(10 * person.level) - self.xp} XP')
    def bosslvlup(self):
        if self.money>=(20*self.xp) and self.xp>=(20*self.xp):
            print(f'Вы повысили уровень с {self.xp} до {self.xp+1}\nС вашего баланса списано: {self.xp>=(20*self.xp)}\nОстаток: {self.money}')
        elif self.money<(self.xp>=(20*self.xp)) and self.xp<(20*self.xp):
            print(f'Вам не хватает опыта и денег для повышения уровня. Вам нужно: {(20*self.xp)-self.money}$\n{(20*self.xp)-self.xp} XP')
        elif self.money<20*self.xp:
            print(f'Вам не хватает опыта и денег для повышения уровня. Вам нужно ещё: {(20*self.xp)-self.money}$')
        elif self.xp<20*self.xp:
            print(f'Вам не хватает опыта и денег для повышения уровня. Вам нужно: {(20*self.xp) - self.xp} XP')
