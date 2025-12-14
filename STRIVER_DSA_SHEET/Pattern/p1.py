# https://takeuforward.org/pattern/pattern-1-rectangular-star-pattern

def print_pattern_1(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print("")

print_pattern_1(4)