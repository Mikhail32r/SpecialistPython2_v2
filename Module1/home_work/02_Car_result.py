class Car:
    def __init__(self, capacity: int, gas_per_km: float):
        self.__gas = 0
        if type(capacity) == int:
            self.__capacity = capacity
        else:
            print('Неверное значение. Элемет будет работат неправильно. Присвоено значение 0')
            self.__capacity = 0
        if type(gas_per_km) == int or type(gas_per_km) == float:
            self.__gas_per_km = gas_per_km
        else:
            print('Неверное значение. Элемет будет работат неправильно. Присвоено значение 0')
            self.__gas_per_km = 0
        self.__mileage = 0

    def fill(self,gas):
        if type(gas) == float or type(gas) == int:
            if gas <= self.__capacity-self.__gas:
                self.__gas = self.__gas + gas
            else:
                print("В бак влезло только {}. Не влезло {} литров".format(self.__capacity-self.__gas, gas - self.__capacity-self.__gas))
                self.__gas = self.__capacity
        else:
            print("Некорректное число")


    def ride(self,km:float):
        if type(km) == float or type(km) == int:
            if self.__gas - km/self.__gas_per_km >= 0:
                self.__gas = self.__gas - km/self.__gas_per_km
                self.__mileage = self.__mileage + km
                print("Проехали {} км. Бензина осталось {}".format(km,self.__gas))
            else:
                print("Проехали {} км. Бензина кончился. Не хватило на {} км из запланированных".format(km,self.__gas * self.__gas_per_km))
                self.__gas = 0
                self.__mileage = self.__mileage + self.__gas * self.__gas_per_km



car1=Car(50,6.2)
car1.fill(70)
car1.ride(500)

