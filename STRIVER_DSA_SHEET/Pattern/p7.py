# https://takeuforward.org/pattern/pattern-7-star-pyramid

def pattern_7(n):
    
    for i in range(0,n):
        print((n-i-1)*" "+(2*i+1)*"*"+(n-i-1)*" ")
        print()


pattern_7(5)