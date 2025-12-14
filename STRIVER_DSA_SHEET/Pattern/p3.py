# https://takeuforward.org/pattern/pattern-3-right-angled-number-pyramid

# def pattern_3(n):
    
#     for i in range(n):
#         a=0
#         while i>=0:
#             a=a+1
#             print(a, end=" ")
#             i=i-1
#         print()


def pattern_3(n):
    
    for i in range(1,n+1):
        for j in range(1,i+1):
            
            print(j, end=" ")
        print()


pattern_3(5)