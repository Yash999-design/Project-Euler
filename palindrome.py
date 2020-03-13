def reverse(n):
    stree = str(n)
    if len(stree) == 1:
        return n
    else:
        string = str(n)
        string = string[::-1]
        string = int(string)
        return string

pal = []

for i in range(1000):
    for j in range(1000):
        a = i*j
        if a == reverse(a):
            pal.append(a)

print(max(pal))