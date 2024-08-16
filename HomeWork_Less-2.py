class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Меня зовут {self.fullname}, мне {self.age} я {self.is_married}')


class Teacher(Person):

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)

        self.experience = experience
        self.salary = 0

    def count_salary(self):
        for i in range(self.experience):
            self.salary += 3000
        print(f'Мой опыт работы {self.experience}, моя зарплата {self.salary}')


Aslan = Teacher('Aslan', 16, 'женат', 1)
Aslan.introduce_myself()
Aslan.count_salary()
