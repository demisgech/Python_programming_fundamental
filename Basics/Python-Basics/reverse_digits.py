class Solution(object):
    @staticmethod
    def reverse(x) -> int:
        negative = x < 0
        x = abs(x)
        reversed_digit = 0
        while x != 0:
            reversed_digit = reversed_digit * 10 + x % 10
            x //= 10
        if reversed_digit > 2 ** 31 - 1:
            return 0
        return reversed_digit if not negative else -reversed_digit


print(Solution.reverse(int(input('X:'))))
