class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях


class BackPack:  # рюкзак
    def __init__(self, max_weight: float):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight
        self.current_wei = 0
    def add_item(self, item: Item):
        if self.current_wei+item.weight>self.max_weight:
            print("Слишком тяжело.",item.name," не кладем")
        else:
            self.current_wei += item.weight
            self.items.append(item)

    def add_items(self, items: list[Item]):
       mn=items[0]
       i=1
       for i in range(len(items)):
            if items[i-1].weight>items[i].weight:
                mn=items[i -1]
                items[i - 1]=items[i]
                items[i]=mn
       for it in items:
           self.add_item(it)

    def show_items(self):
        print("В рюкзаке лежат", len(self.items), "предметов")
        allW=0
        for numobj in range(len(self.items)):
            print(numobj+1,')',self.items[numobj].name,"стоимостью в", self.items[numobj].cost)
            allW+=self.items[numobj].weight
        print("Общий вес (в кг)", allW)


# Создаем предметы
items = [
Item("Гиря", 25, 500),
Item("Арбуз", 4, 300),
Item("Ноутбук", 2.5, 22500),
Item("Кот", 0.5, 250)
]
# Создаем пустой рюкзак
backpack = BackPack(30)


backpack.add_items(items)
# Выводим все предметы в рюкзаке
backpack.show_items()
