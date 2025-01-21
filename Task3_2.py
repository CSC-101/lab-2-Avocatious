def function(a:int,b:int,c:int) -> int:
    if a>b and a>c:
        return a-b   #In general, when will a call to this function evaluate
                    #Answer: a call to this function will evaluate when both a>b and a>c are true
    elif b>c:
        return b+c  # In general, when will a call to this function evaluate this statement?
                    #Answer: A call to this function will evaluate if the first "if" statement evaluates as False
#thus, it will evaluate when a is not greater than both b and c, but b is greater than c. a<b, a<c, b>c
    else:
        return 2*c   # In general, when will a call to this function evaluate this statement?
                     #Answer: in general, a call to this function evaluates this statement when
        # neither "if" or "elif" statements evaluate to True:
        # a is less than or equal to b and c, and b is not greater than c
answer1=function(3,2,1) #Value of answer1 is 1
answer2=function(2,3,1) #Value of answer2 is 4
answer3=function(2,1,3) #Value of answer3 is 6
print()