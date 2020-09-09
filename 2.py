class Triangle:
    def __init__(self,x,y,z):
        self.a = x
        self.b = y
        self.c = z
    def perimeter(self):
        return self.a + self.b + self.c



t1 = Triangle(6,8,10)
t2 = Triangle(6,6,6,)
print('直角三角形的周长:',t1.perimeter())
print('等边三角形的周长:',t2.perimeter())
