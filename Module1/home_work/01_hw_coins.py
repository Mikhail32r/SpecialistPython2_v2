import random

lstrnd=["heads","tails"]

class Coin:
    def __init__(self):
        self.side = None

    def flip(self) -> None:
        self.side = random.choice(lstrnd)

#n = input('Ввведите кол-во монет:')
n=4

list_coin = []
for i in range(n):
    list_coin.append(Coin())
for i in list_coin:
    i.flip()
print('Количество орлов: ', len([item for item in list_coin if item.side == "heads"])/n*100)
print('Количество решек: ', len([item for item in list_coin if item.side == "tails"])/n*100)
