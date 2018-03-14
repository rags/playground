n =  5
for i in range(n):
    for j in range(n):
        print("%d%d" % (i, j), end=" ")
    print()


print("\nfor i =  range(n) j = range(n - i) ")
for k in range(n): #iterate matrix traingle including diagonal
    for i in range(n -  k):
        print ("%d%d" % (k, i),  end = ' ')
    print()

print("\nIterate the traingle diagonally")
print("for i =  range(n) j = range(n - i) print(j, i + j)")
for k in range(n): #iterate matrix traingle including diagonal
    for i in range(n - k):
        print ("%d%d" % (i,(i + k)),  end = ' ')
    print()


print("\nfor i =  range(n - 1) j = range(n - i - 1) print(ij)")
for k in range(n - 1):
    for i in range(n -  k - 1):
        print ("%d%d" % (k, i),  end = ' ')
    print()

#add 1 to (i + j) to offset -1 in for
print("\nfor i =  range(n - 1) j = range(n - i - 1) print(j, j + i + 1)")
for k in range(n - 1):
    for i in range(n -  k - 1):
        print ("%d%d" % (i, k + i + 1),  end = ' ')
    print()


print("\nfor i =  range(n - 1) j = range(n - i - 1) print(j, j + i + 1)")
for k in range(n - 1):
    for i in range(n -  k - 1):
        j = i + k + 1
        print ("%d%d aggr(" % (i, j),  end = '')
        for l in range(1, k + 2):
            print("%d%d and %d%d" % (i, j - l, i + k + 2 - l, j), end = ", ")
        print(")",  end = " ")
    print()

