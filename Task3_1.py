def smallest(n: float, m: float) -> float:
    if n < m:
        return n        # For which calls below is this statement evaluated?
                        # Answer: evaluated for calls where n<m
    else:
        return m        #Answer: evaluated for calls where n>=m

first = smallest(3, 2)  # What is the value of first? #Answer: expected value is 2

second = smallest(2, 2) #What is the value of second? is this a reasonable answer?
                               #Answer: the value of second is 2. This is a reasonable answer because n=2, which renders the statement "n<m" as not true.
                               #Python then moves on to the else statement which returns m, and m is 2. n==m.
print()
