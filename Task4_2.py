def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # For which call below is this statement evaluated
                                                      #and what are the values being added?

#Answer: this statement is being evaluated for call "first".
#The values being added are the length of the first three strings. For the first call, it is adding the length
# of the words "this", "is", and "the". len 4 + 2 + 3 = 9
    elif len(L) > 1:
        result = len(L[0]) + len(L[1])                   #For which call below is this statement evaluated
                                                         #and what are the values being added?
#Answer: the third call is being evaluated.
#The values being added are the lengths of the first 2 strings: "another" "call". len = 7 + 4 = 11
    elif len(L) > 0:
        result = len(L[0])
                            # For which call below is this statement evaluated
    else:                  # and what are the values being added?
        result = 0
    return result
    #Answer: the second call is evaluated. The value being added is the length of "second call". len = 11

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()