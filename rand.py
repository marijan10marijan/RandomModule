import random

## Random number in range(0,1) --> float number
x = random.random()
print(x)

## Random number in range(int x, int y) --> float number
a = random.uniform(1,10)
print(a)

## Random number in range(int x, int y) --> integer number(upper bound included)
b = random.randint(1,10)
print(b)

## Random number in range(int x, int y) --> integer number(upper bound excluded)
c = random.randrange(1,10)
print(c)

## Random letter from list
my_list = ['a','b','c','d','e','f','g']
x = random.choice(my_list)
print(x)

## 3 random letters from list(each letter can be display only one time, never pick same element twice)
y = random.sample(my_list, 3)
print(y)            # return elements in list
print(''.join(y))   # return elements in string

## 3 random letters from list(elements can be display multiple times)
a = random.choices(my_list, k=3)
print(a)

## Shuffle elements of list
random.shuffle(my_list)
print(my_list)





