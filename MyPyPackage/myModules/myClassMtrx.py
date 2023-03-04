# myClassMtrx.py

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
                s += ("{:6.1f}".format(self.L_data[i][j]))
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
        
    def print(self):
        for i in range(self.n_row):
            for j in range(self.n_col):
                print(("{:6.1f}".format(self.L_data[i][j])))
            print("")
