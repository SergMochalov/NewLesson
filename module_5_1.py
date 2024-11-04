


class House:
    def __init__(self, name, number_of_floors):
        self.name=name
        self.number_of_floors=number_of_floors




    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            if new_floor > 0:
                i=0
                while i < new_floor:
                   i += 1
                   print(i)
            else:
                i = new_floor
                new_floor = 0
                print(i)
                while i < new_floor:
                    i += 1
                    print(i)





h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(-7)
h2.go_to(2)