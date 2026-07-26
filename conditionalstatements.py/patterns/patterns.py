# Made by Learn Build Share

# 1. Square Pattern

n = 5

for i in range(n):
    print("* " * n)


# 2. Hollow Square

n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# 3. Left Triangle


n = 5

for i in range(1, n+1):
    print("* " * i)


# 4. Inverted Left Triangle


n = 5

for i in range(n,0,-1):
    print("* " * i)


# 5. Right Triangle


n=5

for i in range(1,n+1):
    print("  "(n-i)+" "*i)


# 6. Inverted Right Triangle

n=5

for i in range(n,0,-1):
    print("  "(n-i)+" "*i)


# 7. Pyramid

n=7

half=n//2
space=half
star=1

for i in range(half+1):
    print(""space+""*star+""*space)
    space-=1
    star+=2


# 8. Inverted Pyramid


n=7

half=n//2
space=0
star=n

for i in range(half+1):
    print(""space+""*star+""*space)
    space+=1
    star-=2


# 9. Diamond

n=5

for i in range(1,n+1):
    print(" "(n-i)+""*(2*i-1))

for i in range(n-1,0,-1):
    print(" "(n-i)+""*(2*i-1))


# 10. Hollow Pyramid


n=5

for i in range(n):
    print(" "*(n-i),end="")
    for j in range(2*i+1):
        if j==0 or j==2*i or i==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()


# 11. Hollow Diamond

n = 5   # Number of rows in the top half

# Top Half
outside = n - 1
inside = 0

for i in range(n):
    print(" " * outside, end="")
    print("*", end="")

    if i != 0:
        print(" " * inside, end="")
        print("*", end="")

    print()

    outside -= 1
    inside += 2

# Bottom Half
outside = 1
inside = 2 * (n - 2) - 1

for i in range(n - 1):
    print(" " * outside, end="")
    print("*", end="")

    if i != n - 2:
        print(" " * inside, end="")
        print("*", end="")

    print()

    outside += 1
    inside -= 2

# 12. X Pattern


n=5

for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()


# 13. Plus Pattern

n = 7
middle = n // 2

for i in range(n):
    for j in range(n):
        if i == middle or j == middle:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 14. Butterfly Pattern

n = 5

# Top Half
stars = 1
spaces = 2 * (n - 1)

for i in range(n):
    print("" * stars + " " * spaces + "" * stars)
    stars += 1
    spaces -= 2

# Bottom Half
stars = n - 1
spaces = 2

for i in range(n - 1):
    print("" * stars + " " * spaces + "" * stars)
    stars -= 1
    spaces += 2

# 15. Hourglass

n = 5

# Top Half
spaces = 0
stars = 2 * n - 1

for i in range(n):
    print(" " * spaces + "*" * stars)
    spaces += 1
    stars -= 2

# Bottom Half
spaces = n - 2
stars = 3

for i in range(n - 1):
    print(" " * spaces + "*" * stars)
    spaces -= 1
    stars += 2

# 16. Sandglass
n = 5

# Top
spaces = 0
stars = 2 * n - 1

for i in range(n):
    print(" " * spaces + "*" * stars)
    spaces += 1
    stars -= 2

# Bottom
spaces = n - 2
stars = 3

for i in range(n - 1):
    print(" " * spaces + "*" * stars)
    spaces -= 1
    stars += 2


# 17. Zig Zag Pattern
n = 17

for i in range(3):
    for j in range(n):

        if (i == 0 and j % 4 == 0) or \
           (i == 1 and j % 2 == 1) or \
           (i == 2 and j % 4 == 2):
            print("*", end="")
        else:
            print(" ", end="")

    print()


# 18. Checkerboard

n=5

for i in range(n):
    for j in range(n):
        print("*" if (i+j)%2==0 else "_",end=" ")
    print()


# 19. Border Rectangle
rows = 5
cols = 8

for i in range(rows):
    for j in range(cols):

        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


# 20. Cross Pattern
n = 7

for i in range(n):
    for j in r…