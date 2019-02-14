"""
Task:NumberOfDiscIntersections
Compute the number of intersections in a sequence of discs.

We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingT9B7BZ-FBZ/ .
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    # write your code in Python 3.6
    # 依序掃描A陣列，將元素值轉成集合，其內容為該圓在X軸上各座標點。
    # 例如A[0] = 1則轉成{-1,0,1}，A[5] = 0則轉成{5}
    # 將該集合陣列依序做差集，若差集後之集合元素內容與原集合相同，則代表兩集合沒有相交

    intersect = 0
    N = []
    X = set()

    for idx in range(len(A)):
        for number in range(idx - A[idx], idx + A[idx] + 1):
            X.add(number)

        N.append(X)
        X = set()
    
    for i in range(len(N)):
        for j in range(i + 1 , len(N)):
            diff = N[i] - N[j]
            if not diff == N[i]:
                intersect += 1

    if intersect >= 1e7:
        return -1

    return intersect

A = [1 ,5 ,2 ,1 ,4 ,0]
print(solution(A))

