class Aplicase:
    def turn_on(self):
        pass
    def turn_off(self):
        pass
    def use(self):
        pass
    def repair(self):
        pass

class WashingMachine(Aplicase):
    def __init__(self):
        super().__init__()

    def use(self):
        print('Стиральная машина начала стирку')

    def repair(self):
        print('Ремонт стиральной машины')

class Microwave(Aplicase):
    def __init__(self):
        super().__init__()

    def use(self):
        print('Микроволновая печь разогревает еду')

    def repair(self):
        print('Ремонт микроволновой печи')

class Refrigerator(Aplicase):
    def __init__(self):
        super().__init__()

    def use(self):
        print('Холодильник охлаждает продукты')

    def repair(self):
        print('Ремонт холодильника')



wm = WashingMachine()
mv = Microwave()
rf = Refrigerator()


wm.use()
wm.repair()
mv.use()
mv.repair()
rf.use()
rf.repair()




