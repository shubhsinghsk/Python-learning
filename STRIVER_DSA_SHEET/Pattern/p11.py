# https://takeuforward.org/pattern/pattern-11-binary-number-triangle-pattern

def pattern11(n):
    for i in range(n):
        for j in range(0, i+1):
            if (i+j)%2==0:
                print(1,end="")
            if (i+j)%2==1:
                print(0,end="")
        print()

pattern11(150)