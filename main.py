import random
from time import *


def shulte(size):
    """
    :rtype: generated table
    """
    count, elements = size * size, []

    for i in range(1, count + 1):
        elements.append(i)

    table = [([0] * size) for _ in range(size)]

    for i in range(len(table)):
        for j in range(len(table[i])):
            random_index = random.randint(0, len(elements) - 1)
            table[i][j] = elements[random_index]
            elements.pop(random_index)

    for i in range(len(table)):
        print(*[f"{x:>5}" for x in table[i]])
    return 'ShulteTables1.0'


class Game:
    def __init__(self, user_name, table_size, time_of_work):
        self.user_name = user_name
        self.table_size = table_size
        self.time_of_work = time_of_work

    def save(self):
        """
        :return: final data
        """
        f_1 = open('users.txt', 'a')
        f_1.write('\nusername:{} | time:{} | size:{}'.format(self.user_name, int(time() - self.time_of_work), self.table_size))
        f_1.close()
        return '{}, your task completion time is {} sec. You have used the {}x{} grid. Great job.'.format(
            self.user_name, int(time() - self.time_of_work), self.table_size, self.table_size)


if __name__ == '__main__':
    username, size, enter = input('Enter player name: '), int(input('Enter the size of the game grid: ')), input(
        'Type ENTER to start the test: ')
    g = Game(username, size, time())
    print(shulte(size))
    end = input()
    print(g.save())
