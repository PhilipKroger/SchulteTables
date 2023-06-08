import random
from time import *
f = open('users.txt', 'r')
s = f.readlines()
f.close()

class Game:
    def __init__(self, username, size, time):
        self.username = username
        self.size = size
        self.time = time

    def user(self):
        self.username = input('Введите имя игрока: ')
        return self.username

    def shulte(self, size):
        """
        :rtype: object
        :param size of table:
        :return: generated table
        """
        count, elements = size * size, []
        for i in range(1, count + 1):
            elements.append(i)

        table = [([0] * size) for i in range(size)]

        for i in range(len(table)):
            for j in range(len(table[i])):
                random_index = random.randint(0, len(elements) - 1)
                table[i][j] = elements[random_index]
                elements.pop(random_index)

        for i in range(len(table)):
            print(*[f"{x:>5}" for x in table[i]])
        return 'ShulteTables1.0'
    def save(self):
        f_1 = open('users.txt', 'w')
        f_1.write('username:{} | time:{} | size:{}'.format(self.username, int(time() - self.time), self.size))
        return '{}, ваше время выполнения задания {} сек. Вы использовали сетку {}x{}. Отличная работа.'.format(self.username, int(time() - self.time), self.size, self.size)


if __name__ == '__main__':
    username = input('Введите имя игрока: ')
    size = int(input('Введите размер игровой сетки: '))
    enter = input('Введите ENTER для начала испытания: ')
    t1 = time()  # время начала игры
    g = Game(username, size, t1)
    print(g.shulte(size))
    end = input()
    print(g.save())