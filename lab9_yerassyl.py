from functools import reduce
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
    if i <= 8:
        b += [i]
print(b)
'''
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
for i in a:
    for s in b:
        if i == s:
            c += [i]
print(c)
'''

'''
#2 func 9 lab
def clean(my_list):
    result = []
    for x in my_list:
        if x > 0:
            result.append(x)
    return result

def add(my_list):
    sum = 0
    for x in my_list:
        sum += x
    return sum

passengers = [1, -1, 1, 2, 2, 1, 4, 3, 7, -1, 0, 9, 11, 1, 3]
clean_list = clean(passengers)
total = add(clean_list)

print(clean_list)
print("Total number of passengers is", total)
'''

'''
#map 9 lab 1 mysal
def solution_map(s):
    return " ".join(list(map(lambda x: x[::-1], s.split())))



def solution_genx(s):
    return " ".join((x[::-1] for x in s.split()))


########################

s = 'Ерасыл'

print(solution_map(s))
print(solution_genx(s))
'''

'''
#map 9 lab 2 mysal
#map
def solution_map(nums):
    return sorted(map(lambda x: x ** 2, nums))


#2 var
def solution_lc(nums):
    return sorted([i ** 2 for i in nums])




nums = [-7, -3, 2, 3, 11]

print(solution_map(nums))
print(solution_lc(nums))
'''

'''
# 9 lab 3 mysal 
#map
def solution_map(nums):
    filter_max = list(filter(lambda num: num != max(nums), nums))

    if all(list(map(lambda num: max(nums) >= 2 * num, filter_max))):
        return nums.index(max(nums))
    else:
        return -1


#enumerate version
def solution_enum(nums):
    for i, n in enumerate(nums):
        if (nums.index(max(nums)) != i) & (n * 2 > max(nums)):
            return -1
    return nums.index(max(nums))



nums = [8, 5, 34, 17, 6]

print(solution_map(nums))
print(solution_enum(nums))
'''


'''
#9 lab 1 mysal reduce
# USING REDUCE
def solution_red(nums):
    prod = reduce(lambda x, y: x * y, nums)

    if prod > 0:
        return 1
    if prod < 0:
        return -1
    return 0

nums = [-1, 1, -2, 4, -7]

print(solution_red(nums))
'''


'''
#9 lab reduce 2 mysal
# USING reduce
from collections import Counter
from functools import reduce

def solution_red(nums1, nums2):
    res = [Counter(nums1), Counter(nums2)]
    l = reduce(lambda x, y: x & y, res)
    return list(l.elements())

#USING EXTEND
def solution_ext(nums1, nums2):
    res = []
    for k in (Counter(nums1) & Counter(nums2)).items():
        res.extend([k[0]] * k[1])
    return res

###############
nums1 = [1,3,3,1,5,5]
nums2 = [5,2,3,3]

print(solution_red(nums1, nums2))
print(solution_ext(nums1, nums2))
'''
