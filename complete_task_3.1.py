# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

from random import randint
from itertools import product

class Matrix:

    def __init__(self, line, column):
        self.line = line
        self.column = column
        self.data = [[None for _ in range(column)] for _ in range(line)]

    def len(self):
        print('Количество строк ', len(self.data))
        print('Количество столбцов ', len(self.data[0]))

    def __str__(self):
        return "\n".join(map(str, self.data))

    def __repr__(self):
        return f'{self.__class__.__name__}({self.line!r}, {self.column!r})'

    def add(self, add_list):
        values = iter(add_list)

        indices = product(range(self.line), range(self.column))

        for (i, j), value in zip(indices, values):
            self.data[i][j] = value

        return values   
    
    def replace(self,line_index,column_index,value):
        
        self.data[line_index][column_index] = value


my_matrix = Matrix(10,10)
overflow = my_matrix.add([randint(1,15) for i in range(100)])

print(my_matrix)
my_matrix.len()
my_matrix.replace(7,8,59)
print(my_matrix)