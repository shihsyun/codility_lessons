"""
Task:PassingCars

A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingQR9HUV-P3Z/ .
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    
    # write your code in Python 3.6
    # 正規解法是將陣列翻轉後，開始搜尋陣列若遇west的車子則將數量遞增，若遇east則加總一次當前的west車子數量。
    # 較容易理解的想法是先計算所有的west車子數量，再重頭搜尋陣列若遇east則加總一次當前的west，若遇到west則遞減。
    # 演算法邏輯請參考 https://codesays.com/2014/solution-to-passing-cars-by-codility/#comment-502 
    # 圖示請參考 https://drive.google.com/file/d/0B2GSXjlcPi0lT3otZ1N5ZXhoZlE/view 
    # more detail can check it out at https://codesays.com/2014/solution-to-passing-cars-by-codility/#comment-502 .
    # prefix sum 演算法內容可參考 https://rust-algo.club/sorting/counting_sort/index.html 

    result = 0
    west = A.count(1)

    for car in A:
        if car == 0:
            result += west
            if result > 1e9:
                return -1
        else:
            west -= 1
    
    return result

    
A = [0, 1, 0, 1, 1]
print(solution(A))