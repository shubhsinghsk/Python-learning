# ============================================================================
# PALINDROME CHECKER - Two Approach Implementation
# ============================================================================
# Problem: Check if a given string is a palindrome
#
# Example 1:
#   Input: Str = "ABCDCBA"
#   Output: Palindrome
#   Explanation: String when reversed is the same as string.
#
# Example 2:
#   Input: Str = "TAKE U FORWARD"
#   Output: Not Palindrome
#   Explanation: String when reversed is not the same as string.
# ============================================================================

# APPROACH 1: Basic Two-Pointer Method
# ============================================================================
def check_palimdrome(s):
    """
    Check if a string is a palindrome using a simple two-pointer approach.

    This function compares characters from the start and end of the string,
    moving inward one step at a time.

    Args:
        s (str): Input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Notes:
        - This version is case-sensitive.
        - It does not ignore spaces or punctuation.
        - Use is_palindrome_comprehensive() for robust real-world strings.
    """
    l = 0
    r = len(s) - 1 

    # A single-character string is always a palindrome.
    if len(s) == 1:
        return True
    
    # Compare characters from both ends until pointers meet.
    while l < r:
        if s[l] != s[r]:
            return False
        
        l += 1
        r -= 1

    return True

# Test case for basic approach (NOTE: includes spaces, will return False)
print(check_palimdrome('A man, a plan, a canal: Panama'))


# ============================================================================
# APPROACH 2: Comprehensive Two-Pointer Method (Optimized)
# ============================================================================
# This approach handles real-world scenarios with spaces and special characters
def is_palindrome_comprehensive(s: str) -> bool:
    """
    Check if a string is a palindrome, ignoring spaces, punctuation, and case.
    
    Args:
        s (str): Input string to check (can contain spaces, special chars, mixed case)
        
    Returns:
        bool: True if palindrome (considering only alphanumeric chars), False otherwise
        
    Time Complexity: O(n) where n is the length of string
    Space Complexity: O(1) - only using pointers
    
    Algorithm:
        1. Initialize left and right pointers at start and end
        2. Skip non-alphanumeric characters
        3. Compare alphanumeric characters case-insensitively
        4. Move pointers inward until they meet
        
    Advantages over check_palimdrome():
        - Handles spaces and special characters
        - Case-insensitive comparison
        - More practical for real-world string validation
        
    Example:
        "A man, a plan, a canal: Panama" -> True (ignores punctuation and space)
        "race a car" -> False
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from the left
        # isalnum() returns True only for letters and digits
        if not s[left].isalnum():
            left += 1
            continue
        
        # Skip non-alphanumeric characters from the right
        if not s[right].isalnum():
            right -= 1
            continue
            
        # Compare characters case-insensitively using lower()
        # This handles mixed-case strings like "AaBbCc"
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True


# ============================================================================
# TEST CASES - Verify both implementations
# ============================================================================
# NOTE: Uncomment specific test cases to verify behavior

print("\n=== APPROACH 1: Basic Check (Case-sensitive, with spaces) ===")
print(f"is_palindrome('A man, a plan, a canal: Panama'): {check_palimdrome('A man, a plan, a canal: Panama')}")
print("Note: Returns False because it includes spaces and different cases\n")

print("=== APPROACH 2: Comprehensive Check (Case-insensitive, ignoring spaces/punctuation) ===")
print(f"is_palindrome_comprehensive('A man, a plan, a canal: Panama'): {is_palindrome_comprehensive('A man, a plan, a canal: Panama')}")
print(f"is_palindrome_comprehensive('race a car'): {is_palindrome_comprehensive('race a car')}")
print(f"is_palindrome_comprehensive('Was it a car or a cat I saw?'): {is_palindrome_comprehensive('Was it a car or a cat I saw?')}")
print(f"is_palindrome_comprehensive('0P'): {is_palindrome_comprehensive('0P')}")
    
    