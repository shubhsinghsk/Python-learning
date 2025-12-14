# https://takeuforward.org/pattern/pattern-12-number-crown-pattern

# def pattern12(n):
#     for i in range(1,n+1):
#         for j in range(i-1,-1,-1):
#             print(i-j, end="")
#         print((2*n-2*i)*" ",end="")
#         for j in range(0,i):
#             print(i-j, end="")
#         print()

#chatgpt

def pattern12(n):
    for i in range(1, n + 1):

        # Left side
        for j in range(1, i + 1):
            print(j, end="")

        # Spaces
        print(" " * (2 * (n - i)), end="")

        # Right side
        for j in range(i, 0, -1):
            print(j, end="")

        print()


pattern12(6)