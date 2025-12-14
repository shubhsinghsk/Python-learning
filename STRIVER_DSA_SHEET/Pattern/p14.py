# https://takeuforward.org/pattern/pattern-14-increasing-letter-triangle-pattern

def pattern14(n):
    for i in range(1,n+1):
        for j in range(i):
            print(chr(ord('A')+j), end=" ")
        print()

pattern14(5)