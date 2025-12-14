# https://takeuforward.org/pattern/pattern-9-diamond-star-pattern

def pattern9(n):
    for i in range(0,n):
        print((n-i-1)*" "+(2*i+1)*"*"+(n-i-1)*" ")
        print()

    c = 0
    for i in range(n,0,-1):
        print(int((2*c)/2)*" " + (2*i-1)*"*" +int((2*c)/2)*" ")
        print()
        c=c+1

pattern9(5)