from typing import Optional             # gain access to the Optional[X] type hint

def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # What is the value of test on each call?
                                        #Answer: the values of test; first = False (9 is out of bounds). second = True (2 is >= 0, and less than length of list)
    if test:                            # What is this check preventing?
                                        #Answer: this check prevents accessing an out of bounds index
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # What is the value of first? Answer: first = None
second = checked_access([1, 0, 1], 2)    # What is the value of second? Answer: second = 1
print()