"""
Task:StoneWall
Cover "Manhattan skyline" using the minimum number of rectangles.

You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

def solution(H)

that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:

  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8
the function should return 7. The figure shows one possible arrangement of seven blocks.



Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array H is an integer within the range [1..1,000,000,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
You can check it out the result at https://app.codility.com/demo/results/trainingK5T72F-Z6D/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(H):

    # write your code in Python 3.6
    # 將Ｈ各元素值存入並與前一個元素做比對，如果小於則將count+1

    wall = [H[0]]

    for idx in range(len(H)):

        if H[idx] == wall[-1]:
            continue
        else:
            wall.append(H[idx])

    if len(wall) == 1: return 1

    count = 0
    prev = wall[0]
    for elem in wall:
        if prev != elem:
            count += 1
        prev = elem
 
    return count

#testcase 1
H = [8, 8, 5, 7, 9, 8, 7 ,4, 8]
print(solution(H))

#testcase 2
H = [1, 1, 1]
print(solution(H))

#testcase 3
H = [3, 2, 1]
print(solution(H))
