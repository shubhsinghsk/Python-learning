# https://takeuforward.org/pattern/pattern-5-inverted-right-pyramid

def pattern_5(n):
    
    for i in range(n,0,-1):
        for j in range(1,i+1):
            
            print("*", end=" ")
        print()


pattern_5(5)
