# https://takeuforward.org/pattern/pattern-13-increasing-number-triangle-pattern

def pattern13(n):
    c = 1
    for i in range(n):
        for j in range(i+1):
            print(c,end=" ")
            c=c+1
        print()

pattern13(5)