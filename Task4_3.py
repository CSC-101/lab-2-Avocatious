def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # What is the value of words at this point?
#Answer: the value of the words =  ["this", "is", "confusing", "code.", "AVOID", "SUCH."]
         # What are the values of first and second at this point?
#Answer: the value of first = ["this", "is", "confusing", "code.", "AVOID"]
#the value of second = ["this", "is", "confusing", "code.", "AVOID", "SUCH."]
         # What happened?
#Answer: because lists are mutable in Python, changes in one function affect the original last in later calls.
#The function appends the uppercase version of 'other'. Because the list is mutable, the change occurs in all the succeeding calls.
print()