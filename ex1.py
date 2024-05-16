# philipe = "dave"
# las = "na"

# print(type(philipe))
# multiline = '''
# hey    i was just coding
#         all good

# '''
# print(multiline)
# print(philipe.lower())
# print(philipe.upper())
# print(len(multiline))

# #tit;e
# t = "menu".upper()
# print(t.center(20, "="))
# print("matcha".ljust(20, ".") + "$7".rjust(1))
# price=100
# print(type(price))
# print(abs(price))
# import math

# print(math.pi)



def hello():
    print("world")

hello()

def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2 is not int)):
        return 0
    return num1 + num2

total = sum(7, 2)
print(total)

def ml(*args):
    print(args)
    print(type(args))

ml("goldman", "bcg")
    
def mll(**argss):
    print(argss)
    print(type(argss))
    
mll(first = "bcg", last= "bainco")



    