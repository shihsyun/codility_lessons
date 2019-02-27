"""
Task:MaxNonoverlappingSegments
Find a maximal set of non-overlapping segments.

Located on a line are N segments, numbered from 0 to N − 1, whose positions are given in arrays A and B. For each I (0 ≤ I < N) the position of segment I is from A[I] to B[I] (inclusive). The segments are sorted by their ends, which means that B[K] ≤ B[K + 1] for K such that 0 ≤ K < N − 1.

Two segments I and J, such that I ≠ J, are overlapping if they share at least one common point. In other words, A[I] ≤ A[J] ≤ B[I] or A[J] ≤ A[I] ≤ B[J].

We say that the set of segments is non-overlapping if it contains no two overlapping segments. The goal is to find the size of a non-overlapping set containing the maximal number of segments.

For example, consider arrays A, B such that:

    A[0] = 1    B[0] = 5
    A[1] = 3    B[1] = 6
    A[2] = 7    B[2] = 8
    A[3] = 9    B[3] = 9
    A[4] = 9    B[4] = 10
The segments are shown in the figure below.



The size of a non-overlapping set containing a maximal number of segments is 3. For example, possible sets are {0, 2, 3}, {0, 2, 4}, {1, 2, 3} or {1, 2, 4}. There is no non-overlapping set with four segments.

Write a function:

def solution(A, B)

that, given two arrays A and B consisting of N integers, returns the size of a non-overlapping set containing a maximal number of segments.

For example, given arrays A, B shown above, the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..30,000];
each element of arrays A, B is an integer within the range [0..1,000,000,000];
A[I] ≤ B[I], for each I (0 ≤ I < N);
B[K] ≤ B[K + 1], for each K (0 ≤ K < N − 1).
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingR2WCJN-EM7/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
def solution(A, B):
    # write your code in Python 3.6
    # 只能判斷特殊狀況，拿到10%
    # 其實只要計算完全沒跟其它區段相交的區段數量就是答案了
    # more detail please check it out at http://codility-lessons.blogspot.com/2015/03/lesson-14-maxnonoverlappingsegments-max.html .
    # https://stackoverflow.com/questions/20929697/how-to-find-maximum-number-of-segments-of-a-infinite-rod-with-given-n-cuts
    
    if len(A) < 1:
        return 0

    count = 1
    prev_end = B[0]

    for idx in range(1, len(A)):
        if A[idx] > prev_end:
            count += 1
            prev_end = B[idx]

    return count

# testcase 1
A = [1, 3, 7, 9, 9]
B = [5, 6, 8, 9, 10]
print(solution(A, B))

# testcase 2
A = [0, 2, 100]
B = [0, 50, 1000]
print(solution(A, B))