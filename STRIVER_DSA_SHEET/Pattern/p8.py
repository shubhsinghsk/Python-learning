# https://takeuforward.org/pattern/pattern-8-inverted-star-pyramid

def pattern8(n):
    c = 0
    for i in range(n,0,-1):
        print(int((2*c)/2)*" " + (2*i-1)*"*" +int((2*c)/2)*" ")
        print()
        c=c+1

pattern8(5)