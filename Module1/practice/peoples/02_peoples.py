class People:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def change_age(self, new_age: int) -> None:
        if type(new_age)==int and 1<new_age<100:
            self.age = new_age
        else:
            print("некоррект возраст")
        return self.age

    def full_name(self) -> str:
        return f"{self.surname} {self.name}"

    def full_info(self) -> str:
        return f"Человек: {self.surname} {self.name} и ему {self.age} лет"


# Создадим двух человек:
peoples = [
    People("Иван", "Уткин", 27),
    People("Алена", "Перова", 32),
    People("Василий", "Быстров", 55),
    People("Ольга", "Подгорная", 32),
    People("Ив", "Кин", 27),
    People("Алексей", "Перов", 32),
    People("Василий", "Быстров", 65),
]
min=People("","",101)
for pep in peoples:
    if min.age>pep.age:
        min=pep
print("Самый молодой",min.full_info())
odn = []
while len(peoples)!=0:
    min=peoples[0]
    peoples.pop(0)
    odn.append(min)
    for pep in peoples:
        if pep.age==odn[0].age:
            odn.append(pep)
            peoples.remove(pep)
    for od in odn:
        if len(odn)>1:
            print(od.full_info())
    odn.clear()
