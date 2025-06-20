# 30 27 24 21 18 15 12 9 
for x in range(30, 3, -3):
    print(x,end=' ')

# 2 4 6 8 10 12 14 16
for x in range(2, 16, 2):
    print(x,end=' ')

# 30 29 26 21 14 5 -6 -19
result = 30
add = 1

looping = 8

for i in range(8):
    print(result, end=' ')
    result -= add
    add += 2



# 1 1 2 3 5 8 13 21 34
a, b = 1, 1

for i in range(9):
    print(a, end=' ')
    a, b = b, a + b

a = b = c = 1

for i in range(9):
    print(c, end=' ')
    if (i >=1):
        c = a + b
        a = b
        b = c