#basic even/odd thing
remainder = lambda x: x%2
argument = int(input("Enter a number: "))
if remainder(argument) == 0:
    print("The number you inputted is even!")
else:
    print("The number you inputted is odd!")
remainder(5)
remainder(4)

#advanced sum of list
def advanced(array):
    listsum = lambda a: sum(a)

sum([5, 7, 42 ,90])

#sorting lambda
sorting = lambda a: sorted(a)

sorted([56, 809, 31, 67, 8])

#filter lambda
blist = [67, 901, 4, 52, 67, 78]
evennumbers = filter(lambda b: b%2 ==0, blist)
print(list(evennumbers))

#map lambda to make squares
numbers = [34, 2, 121, 56]
squares = list(map(lambda x: x * x, numbers))
print(list(squares))

#reduce lambda to get sum
from functools import reduce

wisp = [23, 24, 6, 32] #the list is called wisp cuz wisp is an artist i've listened to and it sounds like list
totalsum = reduce(lambda x, y: x + y, wisp)
print(totalsum)

#enumeration
enumeration = lambda x: list(enumerate(x))
microphones = ["C414", "V7x", "WA-47jr", "I5", "D6", "AT4033a"]
print(enumeration(microphones))

#zip
players = ["Jokic", "Doncic", "Powell", "Kawamura"]
jerseynumber = [15, 77, 24, 17]

yippee = zip(players, jerseynumber)
print(list(yippee))