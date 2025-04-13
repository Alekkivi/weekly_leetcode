def longestCommonPrefix(strs):
    
    longest_common_prefix = ""
    strs = sorted(strs)
    first_word = strs[0]
    last_word = strs[len(strs) - 1]

    for i, first_word_letter in enumerate(first_word):
        second_word_letter = last_word[i]

        if first_word_letter == second_word_letter:
            longest_common_prefix += first_word_letter
        else:
            return longest_common_prefix
        
    return longest_common_prefix

    

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))
