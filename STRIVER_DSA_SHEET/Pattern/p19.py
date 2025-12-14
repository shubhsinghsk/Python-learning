# https://takeuforward.org/pattern/pattern-19-symmetric-void-pattern

def pattern19(n):
    for i in range(n,0,-1):
        print(i*"*", end="")
        print((2*n-i*2)*" ",end="")
        print(i*"*", end="")
        print()
    for i in range(1,n+1):
        print(i*"*", end="")
        print((2*n-i*2)*" ",end="")
        print(i*"*", end="")
        print()

pattern19(30)