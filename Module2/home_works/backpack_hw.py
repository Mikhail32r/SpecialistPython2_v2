class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self) -> str:
        """
        Возвращает строковое представление объекта Item
        """
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self, max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """
        if self.sum_weight() + item.weight > self.max_weight:
            print(f"Предмет {item.name} слишком тяжелый")
        else:
            self.items.append(item)

    def show_items(self) -> None:
        """
        Выводит(print'ом) все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        i = 1
        for one in self.items:
            print(i, one.show())
            i += 1

    def sum_weight(self) -> float:
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        weight = 0
        for item in self.items:
            weight += item.weight
        return weight

    def sum_cost(self) -> int:
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        cost = 0
        for item in self.items:
            cost += item.cost
        return cost

    def add_items(self, items: list[Item]):
        """
        :param items: Список вещей(объектов класса Item)
        """
        items.sort(key=lambda x: x.weight)
        for item in items:
            self.add_item(item)

    def max_weight_item(self):
        """
        самый тяжелый предмет
        """
        i=len(items)-3 #возвращает 5, нумерация с 0 - последний элемент с индексом 4. в конце списка пустота итого минус 3
        print("Самый тяжелый {} с весом {} кг".format(self.items[i].name,self.items[i].weight ))

    def max_valuable(self):
        """
        :param items: Список вещей(объектов класса Item)
        """
        items.sort(key=lambda x: x.cost/x.weight, reverse=True)
        print("Самый дорогой {} с соотношением цены к весу {} за кг ".format(items[0].name, items[0].cost/items[0].weight))

# Создаем предметы
items = [
     Item("Гиря", 25, 500),
     Item("Арбуз", 4, 300),
     Item("Ноутбук", 2.5, 22500),
     Item("Кот", 0.5, 250),
     Item("Мяч", 1, 250),
     Item("Трос", 3, 150),
]

# Создаем пустой рюкзак и указываем его вместимость(в кг)
backpack = BackPack(max_weight=7)

# Пытаемся добавлять максимальное кол-во предметов в рюкзак
backpack.add_items(items)

# Выводим все предметы в рюкзаке
backpack.show_items()

backpack.max_weight_item()

backpack.max_valuable()
