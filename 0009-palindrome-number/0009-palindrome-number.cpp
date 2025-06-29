class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }

        long reversed_x = 0;
        int original_x = x;

        while (x != 0) {
            int digit = x % 10;
            reversed_x = reversed_x * 10 + digit;
            x /= 10;
        }

        return original_x == reversed_x;
    }
};
