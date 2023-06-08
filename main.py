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
    def __init__(self, username, size, time):
        self.username = username
        self.size = size
        self.time = time

    def user(self):
        self.username = input('Enter player name: ')
        return self.username

    def save(self):
        """
        :return: final data
        """
        f_1 = open('users.txt', 'a')
        f_1.write('\nusername:{} | time:{} | size:{}'.format(self.username, int(time() - self.time), self.size))
        f_1.close()
        return '{}, your task completion time is {} sec. You have used the {}x{} grid. Great job.'.format(
            self.username, int(time() - self.time), self.size, self.size)


if __name__ == '__main__':
    username, size, enter = input('Enter player name: '), int(input('Enter the size of the game grid: ')), input(
        'Type ENTER to start the test: ')
    g = Game(username, size, time())
    print(shulte(size))
    end = input()
    print(g.save())
