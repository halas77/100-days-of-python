def add(*args):
    sum = 0
    for n in args:
        sum += n
        
    return sum



num_sum = add(1, 2, 6, 7, 45, 567, 43) 
print(num_sum)