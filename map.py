org_list = [1, 2, 3, 4, 5]
def cube(num):
    return num ** 3
fin_list = list(map(cube, org_list))
print(fin_list)