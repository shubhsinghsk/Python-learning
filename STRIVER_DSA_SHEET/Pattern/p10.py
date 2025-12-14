# https://takeuforward.org/pattern/pattern-10-half-diamond-star-pattern

def pattern10(n):
    for i in range(1,n):
        print(i*"*"+(n-i)*" ")
    for j in range(n-1,0,-1):
        print(j*"*"+(n-j)*" ")

pattern10(5)