"""
Task:MaxSliceSum
Find a maximum sum of a compact subsequence of array elements.

A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingFFB6YH-XKG/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(A):
        
    # write your code in Python 3.6
    # 查詢網路作法後，發現只需要分別使用兩個變數紀錄曾經擁有和到目前為止的總和，即可跑一次迴圈解決，複雜度降為O(N)。
    # more detail please check it out at https://curt-park.github.io/2018-09-13/algorithm-max-slice-sum/ .
 
    once_total = float("-inf")
    until_now = 0
    for X in A:
            until_now = max(X, until_now + Ｘ)
            once_total = max (once_total , until_now)
    
    return once_total

#testcase 1
A = [3, 2, -6, 4, 0]
print(solution(A))

#testcase 2
A = [-10]
print(solution(A))

#testcase 3
A = [0, 1]
print(solution(A))

#testcase 4
A = [-2, 1]
print(solution(A))

#testcase 5
A = [-10E5, -10E5-1, 1,10E5-1]
print(solution(A))