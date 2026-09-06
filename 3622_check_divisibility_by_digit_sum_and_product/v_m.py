class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_prod = 1
        total_sum = 0
        og_n = n
        while n > 0:
            digit = n % 10
            digit_sum += digit
            digit_prod *= digit
            n //= 10
        total_sum = digit_sum + digit_prod

        return (og_n / total_sum == og_n // total_sum)