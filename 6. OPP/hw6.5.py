# hw6.5.py
# Program for class Mtrx
# Author: 박창협
# Programed on October. 06. 2021

class Mtrx:
    def __init__(self, name, n_row, n_col, L_data):
        self.name = name
        self.n_row = n_row
        self.n_col = n_col
        self.L_data = L_data

    def __str__(self):
        s = str()
        for i in range(self.n_row):
            for j in range(self.n_col):
                s += ("{:3}".format(self.L_data[i][j]))
            s += ("\n")
        return s

    def __add__(self, other):
        matrix = [[x for x in range(len(self.L_data[0]))] for x in range(len(self.L_data))]
        for i in range(self.n_row):
            for j in range(self.n_col):
                matrix[i][j] = self.L_data[i][j] + other.L_data[i][j]
        return Mtrx("M_add", self.n_row, self.n_col, matrix)

    def __sub__(self, other):
        matrix = [[x for x in range(len(self.L_data[0]))] for x in range(len(self.L_data))]
        for i in range(self.n_row):
            for j in range(self.n_col):
                matrix[i][j] = self.L_data[i][j] - other.L_data[i][j]
        return Mtrx("M_sub", self.n_row, self.n_col, matrix) 

    def __mul__(self, other):
        matrix = [[x for x in range(len(other.L_data[0]))] for x in range(len(self.L_data))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = 0
                for k in range(len(self.L_data[0])):
                    matrix[i][j] += self.L_data[i][k] * other.L_data[k][j]
        return Mtrx("M_mult", self.n_row, other.n_col, matrix)
        
# Application
if __name__ == "__main__":
    data_1 = [ 
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]
    data_2 = [
        [1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]]

    m1 = Mtrx("M1", 5, 5, data_1)
    print("m1 =\n{}".format(m1))

    m2 = Mtrx("M2", 5, 5, data_2)
    print("m2 =\n{}".format(m2))

    m3 = m1 + m2
    print("m3 = m1 + m2 =\n{}".format(m3))

    m4 = m1 - m2
    print("m4 = m1 ‐ m2 =\n{}".format(m4))

    m5 = m1 * m2
    print("m5 = m1 * m2 =\n{}".format(m5))
