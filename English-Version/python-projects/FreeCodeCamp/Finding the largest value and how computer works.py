#Iterations: Loop Idioms
#Finding the largest value and how computer works

largest_so_far = -1
print('Before', largest_so_far)
for num in [9, 41, 12, 3, 74, 15]:
    if num > largest_so_far:
        largest_so_far = num
    print(largest_so_far) 
print('After', largest_so_far)
