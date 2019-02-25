"""
Task:NailingPlanks
Count the minimum number of nails that allow a series of planks to be nailed.

You are given two non-empty arrays A and B consisting of N integers. These arrays represent N planks. More precisely, A[K] is the start and B[K] the end of the K−th plank.

Next, you are given a non-empty array C consisting of M integers. This array represents M nails. More precisely, C[I] is the position where you can hammer in the I−th nail.

We say that a plank (A[K], B[K]) is nailed if there exists a nail C[I] such that A[K] ≤ C[I] ≤ B[K].

The goal is to find the minimum number of nails that must be used until all the planks are nailed. In other words, you should find a value J such that all planks will be nailed after using only the first J nails. More precisely, for every plank (A[K], B[K]) such that 0 ≤ K < N, there should exist a nail C[I] such that I < J and A[K] ≤ C[I] ≤ B[K].

For example, given arrays A, B such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10
four planks are represented: [1, 4], [4, 5], [5, 9] and [8, 10].

Given array C such that:

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
if we use the following nails:

0, then planks [1, 4] and [4, 5] will both be nailed.
0, 1, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, 3, then all the planks will be nailed.
Thus, four is the minimum number of nails that, used sequentially, allow all the planks to be nailed.

Write a function:

def solution(A, B, C)

that, given two non-empty arrays A and B consisting of N integers and a non-empty array C consisting of M integers, returns the minimum number of nails that, used sequentially, allow all the planks to be nailed.

If it is not possible to nail all the planks, the function should return −1.

For example, given arrays A, B, C such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..30,000];
each element of arrays A, B, C is an integer within the range [1..2*M];
A[K] ≤ B[K].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingNSU9TF-79Y/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

    # write your code in Python 3.6
    # A與B的關係可用如下圖來表示
    # http://3.bp.blogspot.com/-Az6YwCDrGzo/VRCTc5URJjI/AAAAAAAAAtQ/ZZ43tVqr054/s1600/%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%BC%E3%83%B3%E3%82%B7%E3%83%A7%E3%83%83%E3%83%88%2B2015-03-24%2B6.27.05.png
    # 多開一個result陣列，長度為len(A)，由第一根釘子開始，對每一層木板都從頭依序判斷並紀錄是否有滿足A[K] ≤ C[I] ≤ B[K]
    # 若通通滿足(not 0 in result)則回傳當前的idx+1(也就是C的I)，若無法找到釘子可將木板全部釘住(也就是result還有0)，就回傳-1
    # 複雜度為O((N+M)*N)，拿到50%。
    # 查詢網路作法後，利用Binary Search加快搜尋速度。
    # 先利用zip將A,B合併成planks陣列，再將C按照敲的位址(HIT_POS)排序組成二維陣列nails，接著利用二分搜尋法找到釘子位置後。
    # 取出釘子數量(NAIL_COUNT_ADDRESS)，並使用while迴圈依序在nail_pos < len(nails)與
    # nails[nail_pos][HIT_POS] <= plank[END_POS]情形下取出數量的最小值，
    # 若過程中釘子數量已小於先前計算數量，則需跳出while迴圈，否則會time out，這樣只能拿到75%如下
    # https://app.codility.com/demo/results/trainingN7347P-KCK/
    # 最後取nail_count的歷次計算最大值+1(因陣列是由0開始計算)回傳即可，這樣可以拿到100%。
    # more detail please check it out at https://codesays.com/2014/solution-to-nailing-planks-by-codility/ .
    # and https://www.martinkysel.com/codility-nailingplanks-solution/

BEGIN_POS = 0
END_POS = 1
NAIL_COUNT_ADDRESS = 0
HIT_POS = 1

def binary_search_nail_pos(nails, plank):
    beg = 0
    end = len(nails) - 1
    ptr = -1

    while beg <= end:
        mid = (beg + end) // 2

        if nails[mid][HIT_POS] < plank[BEGIN_POS]:
            beg = mid + 1
        elif nails[mid][HIT_POS] > plank[END_POS]:
            end = mid - 1
        else:
            end = mid - 1
            ptr = mid

    return ptr

def solution(A, B, C):

    count = 0
    planks = zip(A, B)
    nails = sorted(enumerate(C), key =  lambda var: var [HIT_POS])

    for plank in planks:
        nail_pos =  binary_search_nail_pos(nails, plank)

        if nail_pos == -1:
            return -1

        nail_count = nails[nail_pos][NAIL_COUNT_ADDRESS]

        while nail_pos < len(nails) and nails[nail_pos][HIT_POS] <= plank[END_POS]:
            nail_count = min(nail_count, nails[nail_pos][NAIL_COUNT_ADDRESS])

            if nail_count <= count:
                break
            
            nail_pos += 1

        count = max(count, nail_count)

    return count + 1


# testcase 1
A = [1, 4, 5, 8]
B = [4, 5, 9, 10]
C = [4, 6, 7, 10, 2]
print(solution(A, B, C))

# testcase 2
A = [3, 4, 5, 8]
B = [4, 5, 9, 10]
C = [2]
print(solution(A, B, C))

# testcase 3
A = [1]
B = [1]
C = [1]
print(solution(A, B, C))

# testcase 4
A = [1, 1, 1]
B = [2, 2, 2]
C = [1, 2, 3]
print(solution(A, B, C))

# testcase 5
A = [1, 1, 1]
B = [2, 2, 2]
C = [3, 2, 1]
print(solution(A, B, C))
