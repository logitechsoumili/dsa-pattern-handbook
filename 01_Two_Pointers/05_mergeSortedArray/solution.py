# LeetCode 88: Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

if __name__ == "__main__":
    m = int(input("Enter m: "))
    nums1_input = list(map(int, input("Enter nums1 elements: ").split()))
    n = int(input("Enter n: "))
    nums2 = list(map(int, input("Enter nums2 elements: ").split()))
    nums1 = nums1_input + [0] * n
    obj = Solution()
    obj.merge(nums1, m, nums2, n)
    print("Merged array:", nums1)