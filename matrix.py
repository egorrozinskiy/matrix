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
