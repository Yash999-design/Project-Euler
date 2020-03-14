def sum_of_div_by_35(to=10):
    return sum((i for i in range(1, to) if div_by_35(i)))

def div_by_35(x):
    return x % 3 == 0 or x % 5 == 0

print(sum_of_div_by_35(1000))