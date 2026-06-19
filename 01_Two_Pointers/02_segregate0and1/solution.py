# GeeksforGeeks: Segregate 0s and 1s
# https://www.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1

class Solution:
    def segregate0and1(self, arr):
        k = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                arr[k], arr[i] = arr[i], arr[k]
                k += 1
        return arr

if __name__ == "__main__":
    L = list(map(int, input("Enter array of 0's and 1's: ").split()))
    obj = Solution()
    print("Segregated array: ", obj.segregate0and1(L))