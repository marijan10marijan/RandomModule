from re import X
import secrets

## Random integer in range(0,n)
x = secrets.randbelow(10)
print(x)

## Random integer with 4 bits,range(0,15) (example: 0101=5,  1101=13, 0001=1...)
y = secrets.randbits(4)
print(y)

## Random element from list 
my_list = list('ABCDEFGHIJK')
a = secrets.choice(my_list)
print(a)

