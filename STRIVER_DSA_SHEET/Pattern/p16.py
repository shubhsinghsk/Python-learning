# https://takeuforward.org/pattern/pattern-16-alpha-ramp-pattern

def pattern16(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(ord('A')+i),end=" ")
        print()

pattern16(5)