class Matrix:

    A = None
    m = None
    n = None

    def __init__(self, m, n=None):
        if m <= 0 or n <= 0 or type(m) != int or type(n) != int:
            raise Exception(ValueError)
        self.A = [[0]*n for i in range(m)]
        self.m = m
        self.n = n
    def __add__(self, other):
        if self.m == other.m and self.n == other.n:
            for j in range(self.m):
                for i in range(self.n):
                    self.A[j][i] += other.A[j][i]
            return self
        else:
            print('Размеры матриц не совпадают')
    def __eq__(self, other):
        if self.m!=other.m or self.n!=other.n:
            raise Exception(ValueError)
        else:
            for i in range(self.n):
                for j in range(self.m):
                    if self.value[i][j]!=other.value[i][j]:
                        return False
            return True
    def get(self, i, j):
        if i <= self.m and j <= self.n:
            raise Exception(ValueError)
        else:
            return self.A[i][j]

    def get_m(self):
        return self.m

    def get_n(self):
        return self.n

    def get_size(self):
        return self.m, self.n

    def set(self,i,j,value):
        self.A[i][j]=value

    def __sub__(self, other):
        result=Matrix(self.get_m(),self.get_n())
        for i in range(self.m):
            for j in range(self.n):
                result.X[i][j] = (self.get(i,j)-other.get(i,j))
        return result
