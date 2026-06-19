# LeetCode 26: Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(nums):
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k

if __name__ == "__main__":
    L = list(map(int, input("Enter sorted array: ").split()))
    print("Number of unique elements:", removeDuplicates(L))