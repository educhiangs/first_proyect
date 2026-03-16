# import os; os.system('cls')
# x = 10
# y = "10"

# sum1 = x + x
# sum2 = int(y) + int(y)

# print(sum1, sum2)

# student_grades = [9.1, "Hello", [1, 2, 3, 4.33]]
# student_grades = list(range(0,11, 2))
# student_grades = [9.1, 8.8, 7.5]
# mysum = sum(student_grades)
# student_grades = {"Marry": 9.1, "Sim": 8.8, "Jhon": 7.5}
# mysum = sum(student_grades.values())
# username = "Eduardo"
# length = len(student_grades)
# # mean = mysum / length
# print(mysum)
# print(username.lower())
# print(student_grades.values())
# phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
# print(phone_numbers.keys())
# monday_temperatures = [9.1, 8.8, 7.5]
# workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
# weekend = ["Sat", "Sun"]
# workdays.append(weekend[0])
# print(workdays)
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters[1:4])
# data = {'a':[1,2,3], 'b':[4,5,6], 'c':[7,8,9]}
# temps = [221, 234, 340, -9999, 230]
# # temps_list = []
# # for temp in temps:
# #     temp = temp / 10
# #     temps_list.append(temp)
# # print(temps_list)
# # new_temp = [temp / 10 for temp in temps]
# # print(new_temp)
# new_temp = [temp / 10 for temp in temps if temp != -9999]
# print(new_temp)
# def foo(lst):
#     return [item for item in lst if item >= 3 and item <= 101]
    
# print(foo([-5, 3, -1, 101]))
# def foo(lst):
#     return [item if isinstance(item, (int, float)) else 0 for item in lst]
    
# print(foo([99, 'no data', 95, 94, 'no data']))
# def foo(lst):
#     return [sum(float(item) for item in lst)]

# print(foo(['1.2', '2.6', '3.3']))
# float_list = ['1.2', '2.6', '3.3']
# total = 0
# for num in float_list:
#     total = total + float(num)
# print(total)
# def foo(lst):
#         return sum(float(num) for item in item for lst)
# new_list = []
# def foo(lst):
#     for temp in lst:
#         if temp != 'no data':
#             new_list = new_list.replace(0)
#         else:
#             continue
# print(new_list)
# # print(foo([99, 'no data', 95, 94, 'no data']))

# def mean(*args):
#     return type(args)

# print(mean(1, 2, 3))

# def averege(*args):
#     return sum(args) / len(args)
    

# print(averege(10, 20, 30, 40))

# def foo(*args):
#     return sorted([s.upper() for s in args])

# print(foo("snow", "glacier", "iceberg"))

# def mean(**kwargs):
#     return kwargs

# print(mean(a = 1, b = 2, c = 3))
# Cheatsheet: More on Functions
# In this section, you learned that:

# Functions can have more than one parameter:

# def volume(a, b, c):
#     return a * b * c
# Functions can have default parameters (e.g. coefficient):

# def converter(feet, coefficient = 3.2808):
#     meters = feet / coefficient
#     return meters
 
# print(converter(10))
# Output: 3.0480370641306997

# Arguments can be passed as non-keyword (positional) arguments (e.g. a) or keyword arguments (e.g. b=2 and c=10):

# def volume(a, b, c):
#     return a * b * c
 
# print(volume(1, b=2, c=10))
# An *args parameter allows the  function to be called with an arbitrary number of non-keyword arguments:

# def find_max(*args):
#     return max(args)
# print(find_max(3, 99, 1001, 2, 8))
# Output: 1001

# A **kwargs parameter allows the function to be called with an arbitrary number of keyword arguments:

# def find_winner(**kwargs):
#     return max(kwargs, key = kwargs.get)
 
# print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
# Output: Sim

# Here's a summary of function elements:

