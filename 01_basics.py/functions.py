# def squared_nums(n):
#     print(n**2)
# squared_nums(9)

# def sum(a,b):
#     return a+b
# print(sum(9,10))

# def multiply(p1,p2):
#     return p1*p2
# print(multiply(1,2))

# import math

# def circle_stats(radius):
#     area = math.pi * radius **2
#     circumfernace = 2 * math.pi * radius
#     return area,circumfernace

# print(circle_stats(2))

# def greet(name="User"):
#         return "hello"+name
# print(greet("dhaminisj"))
# 
# cube = lambda x:x**3
# print(cube(3))

# def sum_all(*args):
#     print(*args)
#     return sum(args)

# print(sum_all(1,2,3,4,5,6,7))

# def print_kwargs(name,power):
#     print("Name: ",name,"Power: ",power)

# print_kwargs(power="lazer",name="shaktiman")

def even_generator(limit):
    for i in range(2,limit+1,2):
        return i
    
print(even_generator(8))