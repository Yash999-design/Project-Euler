def sum_of_squares(n):
    square = [i*i for i in range(n+1)]
    # square = []
    total = 0
    # for i in range(n+1):
    #     square.append(i*i)

    # for i in range(1, n+1):
    #     yield (i*i)

    for j in square:
        total += j

    return total


def square_of_sum(n):
    total = 0

    for i in range(n+1):
        total += i
    
    return (total*total)

print(square_of_sum(100) - sum_of_squares(100))