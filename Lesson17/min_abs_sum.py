"""
Task:MinAbsSum
Given array of integers, find the lowest absolute sum of elements.

For a given array A of N integers and a sequence S of N integers from the set {−1, 1}, we define val(A, S) as follows:

val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|

(Assume that the sum of zero elements equals zero.)

For a given array A, we are looking for such a sequence S that minimizes val(A,S).

Write a function:

def solution(A)

that, given an array A of N integers, computes the minimum value of val(A,S) from all possible values of val(A,S) for all possible sequences S of N integers from the set {−1, 1}.

For example, given array:

  A[0] =  1
  A[1] =  5
  A[2] =  2
  A[3] = -2
your function should return 0, since for S = [−1, 1, −1, 1], val(A, S) = 0, which is the minimum possible value.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..20,000];
each element of array A is an integer within the range [−100..100].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingA6XJCP-6RX/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(A):
    # write your code in Python 3.6
    # 複雜度為O(N * max(abs(A))**2)，可以拿到100%
    # 官方解答 https://codility.com/media/train/solution-min-abs-sum.pdf
    # more detail please check it out at https://stackoverflow.com/questions/44897316/codility-minabssum .

    N = len(A)
    M = 0
    
    for i in range(N):
        A[i] = abs(A[i])
        M = max(A[i], M)
    
    S = sum(A)
    count = [0] * (M + 1)
    
    for i in range(N):
        count[A[i]] += 1
    
    dp = [-1] * (S + 1)
    dp[0] = 0
    
    for a in range(1, M + 1):
        if count[a] > 0:
            for j in range(S):
                if dp[j] >= 0:
                    dp[j] = count[a]
                elif (j >= a and dp[j - a] > 0):
                    dp[j] = dp[j - a] - 1
    
    result = S
    
    for i in range(S // 2 + 1):
        if dp[i] >= 0:
            result = min(result, S - 2 * i)
    return result

# testcase 1
A = [1, 5, 2, -2]
print(solution(A))    

# testcase 2
A = []
print(solution(A))

# testcase 3
A = [3, 1]
print(solution(A))