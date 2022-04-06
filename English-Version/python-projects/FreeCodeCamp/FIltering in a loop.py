#Iterations: More Patterns
#Filtering in a loop
a = 0
print('Start')
for i in [9, 41, 12, 3, 74, 15]:
    if i > 20:
        print('Greater than 20 is', i)
        a += 1
print('There are', a,'Values that greater than 20')
