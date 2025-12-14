# Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Examples:
# Example 1:

# Input: [2, 7, 11, 15], 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].

def get_idx(l,n):

    for i in range(len(l)):
        for j in range(len(l[1:])):
            print(i,j)
            if l[i]+l[j]==n:
                r = [i,j]
                return r
            

l = [3, 2, 4]
n = 6
print(get_idx(l,n))
