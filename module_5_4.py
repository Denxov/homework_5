class House:
    houses_history=[]
    def go_to(self,new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1,new_floor+1):
                print(i)
        else:
            print('Такого этажа не существует')

    def __init__(self,name,number_of_floors):
        self.name=name
        self.number_of_floors=number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __new__(cls,*args,**kwargs):
        if args[0] in cls.houses_history:
            print(f'Название <{args[0]}> уже присутствует в истории')
        else: cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")
        return self

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
