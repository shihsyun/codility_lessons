"""
Task:MaxProfit
Given a log of stock prices compute the maximum possible earning.

An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].

For example, consider the following array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

Write a function,

def solution(A)

that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days, returns the maximum possible profit from one transaction during this period. The function should return 0 if it was impossible to gain any profit.

For example, given array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
the function should return 356, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..400,000];
each element of array A is an integer within the range [0..200,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingU9QYMU-NHB/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(A):

        # write your code in Python 3.6
        # 查詢網路作法後，降低複雜度為O(N)，拿到100%。
        # more detail please check it out at https://www.martinkysel.com/codility-maxprofit-solution/ .

    once_price = 2*10E4
    once_profit = 0

    for X in A:
        once_price = min(once_price, X)
        once_profit = max(once_profit, X - once_price)

    return once_profit

#testcase 1
A = [23171, 21011, 21123, 21366, 21013, 21367]
print(solution(A))

#testcase 2
A = []
print(solution(A))

#testcase 3
A = [23000]
print(solution(A))

#testcase 4
A = [23000, 23010]
print(solution(A))

#testcase 5
A = [23010, 23000]
print(solution(A))