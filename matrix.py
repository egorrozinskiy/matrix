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
    
