# https://takeuforward.org/pattern/pattern-15-reverse-letter-triangle-pattern

def pattern15(n):
    for i in range(n,0,-1):
        for j in range(0, i):
            print(chr(ord('A')+j),end=" ")
        print()

pattern15(7)