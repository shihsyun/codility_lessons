"""
Task:Nesting
Determine whether a given string of parentheses (single type) is properly nested.

A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S consists only of the characters "(" and/or ")".
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingEE6W9Z-NXG/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(S):

    # write your code in Python 3.6

    if len(S) is 0:
       return 1
    
    if len(S) % 2 == 1:
        return 0

    check = []
    for idx in S:

        if idx == "(":
            check.append(idx)
        elif len(check) == 0:
            return 0
        elif idx == ")":
            check.pop()
        else:
            return 0

    if len(check) > 0:
        return 0

    return 1

    # write your code in Python 3.6


#testcase 1
S = "(()(())())"
print(solution(S))

#testcase 2
S = "())"
print(solution(S))

#testcase 3
S = "()(()"
print(solution(S))

#testcase 4
S = "()(()()(((()())(()()))"
print(solution(S))