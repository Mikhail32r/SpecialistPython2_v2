class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях


class BackPack:  # рюкзак
    def __init__(self):
        self.items = []  # Предметы, которые хранятся в рюкзаке

    def add_item(self, item: Item):
       self.items.append(item)

    def show_items(self):
        print("В рюкзаке лежат", len(self.items), "предметов")
        allW=0
        for numobj in range(len(self.items)):
            print(numobj+1,')',self.items[numobj].name,"стоимостью в", self.items[numobj].cost)
            allW+=self.items[numobj].weight
        print("Общий вес (в кг)", allW)


# Создаем предметы
item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)

# Создаем пустой рюкзак
backpack = BackPack()

# Добавляем пару предметов в рюкзак
backpack.add_item(item1)
backpack.add_item(item2)

# Выводим все предметы в рюкзаке
backpack.show_items()
