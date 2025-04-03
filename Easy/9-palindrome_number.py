# Initial version just to Pass
def isPalindrome(x: int) -> bool:

    if x < 0:
        return False
    
    if x < 9:
        return True

    int_as_str = str(x)
    reversed_str = ""

    for i in reversed(int_as_str):
        reversed_str += i

    if int_as_str == reversed_str:
        return True
    else:
        return False
    
# Second attemmpt with numerical approach. Ended up being more slow than str due to ^2 calculations
def isPalindrome2(x: int) -> bool:

    if x < 0:
        return False
    
    if x < 9:
        return True
    
    count = 0
    num = x
    
    while num > 0:
        num //= 10
        count += 1

    i = 0
    j = count - 1
    
    while j > 0:
        if (x // 10**i) % 10 != (x // 10**j) % 10:
            return False
        i += 1
        j -= 1
    return True


# Third attemmpt was performed with the help of chatGPT's hints
def isPalindrome3(x: int) -> bool:

    # Negative cant be palindrome
    if x < 0:
        return False
    
    # Int like 100 cant be palindrome
    if x % 10 == 0 and x != 0:
        return False

    # Single digit int is automatically palindrome
    if x < 10:
        return True

    reversed_half = 0

    # Stay in loop while left half has more digits than right (reversed) half
    while x > reversed_half:

        # Get rightmost digit from current x
        rightmost_digit = x % 10

        # Append rightmost digit to reversed half
        reversed_half = reversed_half * 10 + rightmost_digit

        # Drop rightmost digit from x
        x //= 10

    # If there was a even amount of digits, check if the halves match
    if x == reversed_half:
        return True
    
    # If there was a uneven amount of digits, drop the right most digit from reversed half and compaire halves
    elif x == reversed_half // 10:
        return True
    
    # Halves do not match - not palindrome
    else:
        return False
    



print(isPalindrome3(101))