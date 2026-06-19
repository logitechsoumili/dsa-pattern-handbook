# LeetCode 977: Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/

def sortedSquares_twoPointer(arr):
    res = []
    i, j = 0, len(arr) - 1

    while i <= j:
        if arr[i]**2 >= arr[j]**2:
            res.append(arr[i]**2)
            i += 1
        else:
            res.append(arr[j]**2)
            j -= 1
    return res[::-1]

if __name__ == "__main__":
    L = list(map(int, input("Enter sorted array: ").split()))
    print(sortedSquares_twoPointer(L))
