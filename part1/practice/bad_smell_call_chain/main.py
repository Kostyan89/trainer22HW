# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, room_num, population):
        self.room_num = room_num
        self.population = population

    def get_room(self):
        return self.room_num

    def get_city_population(self):
        return self.population


# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

person = Person(33, 9999)
print(person.get_room())
print(person.get_city_population())