from time import sleep
from threading import Thread

class Knight(Thread):
    def __init__(self, name_, power):
        self.name_ = str(name_)
        self.power = int(power)
        super().__init__()

    def run(self):
        print(f'{self.name_}, на нас напали!')
        num_days = 0
        enemyes = 100
        while enemyes > 0:
            sleep(1)
            num_days += 1
            enemyes = enemyes - self.power
            if enemyes < 0:
                enemyes = 0
            print(f'{self.name_} сражается {num_days}-й день..., осталось {enemyes} воинов.')

        print(f'{self.name_} одержал победу спустя {num_days} дней(дня)!')

threads = []


first_knight = Knight('Sir Lancelot', 10)
first_knight .start()
second_knight = Knight("Sir Galahad", 20)
second_knight.start()

threads.append(first_knight )
threads.append(second_knight)

for thread in threads:
    thread.join()
print(f'\nВсе враги повержены, битвы закончены!')