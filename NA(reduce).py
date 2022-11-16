from functools import reduce
numbers = [1, 2, 3, 4]
print(reduce(lambda a, b: a + b, numbers))

...

def Square(y):
    return (y * y)

def SumofSquares(list, n):
    summa = 0
    for i in range(n):
        SquaredValue = Square(list[i])
        summa += SquaredValue
    return summa

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(list)
Total = SumofSquares(list, n)
print("квадраттарының суммасы : ", Total)