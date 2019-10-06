s = []
x = [1, 2, 9]
y = [4, 5, 6]
def plus(x, y):
    for i in range(len(x)):
        s.append(x[i] + y[i])
plus(x,y)
s
print(s)


m = []
a = [1, 2, 3]
b = [4, 5, 6]
def minus(x, y):
    for i in range(len(a)):
        m.append(a[i] - b[i])
minus(a,b)
m
print(m)