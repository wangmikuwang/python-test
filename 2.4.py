def print_line(n):
    for i in range(1, n + 1):
        print("{} x {} = {:2}".format(i, n, i * n), end="  ")
    print()
def print_table(m):
    for j in range(1, m + 1):
        print_line(j)
print_table(10)



