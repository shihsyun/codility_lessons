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

You can check it out the result at https://app.codility.com/demo/results/trainingCWKFUT-44R/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(A):

    # write your code in Python 3.6
    # 先建立圓盤陣列，接著循序計算左右各端點的X軸座標，接著依照(1)座標(2)L/R的參數做正向排序
    # 此時圓盤陣列會如下圖所示
    # http://www.lucainvernizzi.net/img/blog/disk-intersections-thick-642f9e5c.png
    # 依序讀取圓盤陣列，若遇左端點就遞增盤子數量並加入intersections變數中
    # 反之就遞減盤子數量，最後即可求出各圓交集數量
    # more detail please check it out at https://www.martinkysel.com/codility-number-of-disc-intersections-2010-beta-solution/ .    

    circles = []
    for idx , radius in enumerate(A):
        circles.append([idx - radius , 'L'])
        circles.append([idx + radius , 'R'])

    circles.sort(key = lambda x :(x[0],x[1]))

    intersections = 0
    actives = 0

    for _, flag in circles:
        if flag == 'L':
            intersections += actives
            actives += 1
        else:
            actives -= 1
        
        if intersections > 10e6:
            return -1

    return intersections

# testcase 1
A = [1 ,5 ,2 ,1 ,4 ,0]
print(solution(A))

# testcase 2
A = [1 ,1 ,1]
print(solution(A))


