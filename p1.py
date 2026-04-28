# Two Sum problem: Find indices of two numbers that add up to target
# Note: This implementation has a bug - j starts from 0, should start from i+1 to avoid duplicates and self-pair
def get_idx(l, n):
    for i in range(len(l)):
        for j in range(len(l[1:])):  # Bug: range(len(l[1:])) is wrong, should be range(i+1, len(l))
            print(i, j)
            if l[i] + l[j] == n:
                r = [i, j]
                return r

l = [3, 2, 4]
n = 6
print(get_idx(l, n))
