def square(n):
    s = 0
    while n > 0:
        d = n % 10
        s += d * d
        n = n // 10
    return s

class Solution:
    def isHappy(self, n: int) -> bool:
        slow = fast = n
        while fast != 1:
            slow = square(slow)
            fast = square(square(fast))
            if slow == fast and slow != 1:
                return False
        return True