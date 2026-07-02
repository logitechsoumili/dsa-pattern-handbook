int square(int n){
    int sum = 0;
    while (n > 0){
        int digit = n % 10;
        sum += digit * digit;
        n /= 10;
    }
    return sum;
}

class Solution {
public:
    bool isHappy(int n) {
        int slow = n, fast = n;

        while (true){
            slow = square(slow);
            fast = square(square(fast));

            if (fast == 1) return true;

            if (slow == fast) return false;
        }
    }
};