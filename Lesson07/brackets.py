"""
Task:Brackets
Determine whether a given string of parentheses (multiple types) is properly nested.

A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.


You can check it out the result at https://app.codility.com/demo/results/trainingVYSU6A-AKU/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(S):

    # write your code in Python 3.6
    # 建立一個新List，遇到"(", "{", "["就append，反之就pop，若非成對即回傳0
    # 注意testcase要考慮先出現"]", "}", ")"
    # 最後檢查List長度，若等於0則回傳1

    check = []

    for elem in S:

        if len(check) == 0:
            check.append(elem)
            continue

        if elem == '(':
            check.append(elem)
        
        if elem == '{':
            check.append(elem)

        if elem == '[':
            check.append(elem)
        
        if elem == ')':
            pair = check.pop()
            if not pair == '(':
                return 0

        if elem == '}':
            pair = check.pop()
            if not pair == '{':
                return 0

        if elem == ']':
            pair = check.pop()
            if not pair == '[':
                return 0

    if len(check) == 0:
        return 1

    return 0


# testcase 1
S = "{[()()]}"
print(solution(S))

# testcase 2
S = "([)()]"
print(solution(S))

# testcase 3
S = ")("
print(solution(S))

# testcase 4
S = "{{{{"
print(solution(S))