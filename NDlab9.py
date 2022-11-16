from functools import reduce
'''
def cylinder(h, r=1):
    biktik = 2 * 3.14 * r * h
    audany = 3.14 * r ** 2
    kolemi = biktik + 2 * audany
    return kolemi

figure_1 = cylinder(4, 3)
figure_2 = cylinder(5)
print(figure_1)
print(figure_2)
'''



'''
def func_1(name):
    def func_2():
        print('Nursultanuly ' + name)
    return func_2
func = func_1('Daulet')
func()
'''
'''
l1 = []
san = input("butin san engiz(0 sony): ")
while san!="0":
    s = int(san)
    l1.append(s)
    san = input("butin san engiz(0 sony): ")

a = int(input("Vvedite chislo ot 1 do 3!"))
if a == 1:
    mapped = list(map(lambda x: x + 1, l1))
    print(mapped)
elif a == 2:
    filtered = list(filter(lambda x: x > 5, l1))
    print(filtered)
elif a == 3:
    def sum_s(y, z):
        return y+z
    reduced = reduce(sum_s, l1)
    print(reduced)
else:
    print("Vvedite chislo ot 1 do 3!")
'''