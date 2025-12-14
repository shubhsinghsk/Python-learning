# https://takeuforward.org/pattern/pattern-2-right-angled-triangle-pattern

def pattern_2(n):
    for i in range(1,n+1):
        while i>0:
            print("*", end="")
            i=i-1
        print()

pattern_2(3)