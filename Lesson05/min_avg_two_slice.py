"""
Task:MinAvgTwoSlice
Find the minimal average of any slice containing at least two elements.

A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingK5MGHJ-CAT/ .
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    
    # write your code in Python 3.6
    # The key to solve this task is these two patterns:  
    # (1) There must be some slices, with length of two or three, having the minimal average value among all the slices.
    # (2) And all the longer slices with minimal average are built up with these 2-element and/or 3-element small slices.
    # https://codesays.com/2014/solution-to-min-avg-two-slice-by-codility/
    # https://codesays.com/2014/solution-to-min-avg-two-slice-by-codility/#comment-1150
    # https://stackoverflow.com/questions/21635397/min-average-two-slice-codility
    # https://github.com/daotranminh/playground/blob/master/src/codibility/MinAvgTwoSlice/proof.pdf 

    min_idx = 0
    min_avg = (A[0]+A[1])/2.0

    for idx in range(0, len(A)-2):
        avg_2 = (A[idx] + A[idx+1]) / 2.0
        avg_3 = (A[idx] + A[idx+1] + A[idx+2]) / 3.0

        if min_avg > avg_2:
            min_avg = avg_2
            min_idx = idx

        if min_avg > avg_3:
            min_avg = avg_3
            min_idx = idx

    avg_2 = (A[-2] + A[-1]) / 2.0
    if min_avg > avg_2:
        return len(A)-2

    return min_idx

A = [4, 2, 2, 5, 1, 5, 8]
print(solution(A))