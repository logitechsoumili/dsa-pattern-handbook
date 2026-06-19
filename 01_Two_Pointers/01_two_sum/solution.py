# LeetCode 167: Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

def optimised(arr, target):
    i, j = 0, len(arr) - 1
    while i < j:
        res = arr[i] + arr[j]
        if res == target:
            return (i, j)
        elif res < target:
            i += 1
        else:
            j -= 1

if __name__ == "__main__":
    L = list(map(int, input("Enter a sorted array: ").split()))
    target = int(input("Enter target: "))
    print(optimised(L, target))
