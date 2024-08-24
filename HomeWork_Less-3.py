class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @property
    def memory(self):
        return self.__memory

    @property
    def make_computations(self):
        return self.__make_computations

    def __make_computations(self):
        print(
            f'Вычисление: {self.cpu - self.memory}. \nСложение {self.cpu + self.memory}. \nУмножение {self.cpu * self.memory} \nДеление {self.cpu / self.memory} ')


class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card

    @property
    def memory_card(self):
        return self.__memory_card

    def info(self):
        print(f'Процессор {self.cpu}, память на {self.memory} и карта памяти на {self.memory_card}.')


pk = Computer(748, 930)
pk.make_computations()
levonio = Laptop(3, 128, 1000)
levonio.info()
levonio.make_computations()                  