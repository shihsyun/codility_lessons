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

You can check it out the result at https://app.codility.com/demo/results/training67FWFR-6JZ/ .
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    # write your code in Python 3.6
    # 依序掃描A陣列，計算每個圓圈在X軸上的左右兩端點，若左右兩端點皆沒有落在下一個圓的範圍內，則代表沒有相交。
    # 要特別注意兩圓包含的情形，分別有比下一個圓更小或更大兩種情形。
    
    intersect = 0

    for i in range(len(A)):
        for j in range(i + 1 , len(A)):
            cil = i - A[i]
            cir = i + A[i]
            cjl = j - A[j]
            cjr = j + A[j]

            if (cjl <= cil) and (cil <= cjr):
                intersect += 1
                continue

            if (cjl <= cir) and (cir <= cjr):
                intersect += 1
                continue

            if (cjl <= cil) and (cir <= cjr):
                intersect += 1
                continue

            if (cjl >= cil) and (cir >= cjr):
                intersect += 1
                continue

    if intersect >= 1e7:
        return -1

    return intersect

A = [1 ,5 ,2 ,1 ,4 ,0]
print(solution(A))

