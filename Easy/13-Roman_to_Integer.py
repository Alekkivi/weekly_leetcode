
# Initial version
def romanToInt(s):

    total = 0
    values = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    while s:

        current_letter = s[0]
        total += values[current_letter]
        s = s[1:]

        if s:
            next_letter = s[0]

            if current_letter == "I":
                if next_letter == "V" or next_letter == "X":
                    total += (values[next_letter] - 2)
                    s = s[1:]

            elif current_letter == "X":
                if next_letter == "L" or next_letter == "C":
                    total += (values[next_letter] - 20)
                    s = s[1:]

            elif current_letter == "C":
                if next_letter == "D" or next_letter == "M":
                    total += (values[next_letter] - 200)
                    s = s[1:]

    return total
        
print("Total: ", romanToInt("MCMXCIV"))