class Vehicle:
    def __init__(self, marka, fuel):
        self.marka = marka
        self.fuel = fuel

    def move(self):
        print(f'{self.marka} движется')

    def type_fuel(self):
        print(f'Тип топлива {self.fuel}')


class Car(Vehicle):
    def __init__(self, marka, fuel):
        super().__init__(marka, fuel)

    def move(self):
        print(f'{self.marka} едет')

    def type_fuel(self):
        print(f'Тип топлива {self.fuel}')


class Bicycle(Vehicle):
    def __init__(self, marka, fuel):
        super().__init__(marka, fuel)

    def move(self):
        print(f'{self.marka} едет')

    def type_fuel(self):
        print(f'Тип топлива {self.fuel}')


class Boat(Vehicle):
    def __init__(self, marka, fuel):
        super().__init__(marka, fuel)

    def move(self):
        print(f'{self.marka} плывет')

    def type_fuel(self):
        print(f'Тип топлива {self.fuel}')


bmv = Car("Машина ", "бензин ")
bike = Bicycle("Велосипед ", "Нету ")
boat = Boat("Лодка ", "бензин ")

bmv.move()
bmv.type_fuel()
bike.move()
bike.type_fuel()
boat.move()
boat.type_fuel()


