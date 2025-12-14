# https://takeuforward.org/pattern/pattern-4-right-angled-number-pyramid-ii

def pattern_4(n):
    
    for i in range(1,n+1):
        for j in range(1,i+1):
            
            print(i, end=" ")
        print()


pattern_4(5)