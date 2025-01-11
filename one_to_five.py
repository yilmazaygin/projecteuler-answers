def problem_one(num: int = 1000, multiples: list = [3, 5]) -> int:
    """
    Sums numbers below `num` divisible by any of the numbers in `multiples`.

    Args:
        num (int): Upper limit (exclusive).
        multiples (list): List of divisors.

    Returns:
        int: The sum of all divisible numbers.

    Explanation:
        Iterates through numbers below `num` and checks if they are divisible by any value in `multiples`.
    """
    return sum([i for i in range(1, num) if any(i % m == 0 for m in multiples)])


def problem_two(num: int = 4000000) -> int:
    """
    Sums all even Fibonacci numbers less than `num`.

    Args:
        num (int): Upper limit (exclusive).

    Returns:
        int: The sum of even Fibonacci numbers.

    Explanation:
        Generates Fibonacci numbers and adds the even ones to the sum until the value exceeds `num`.
    """
    a, b, total = 1, 2, 0
    while b < num:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total


def problem_three(num: int = 600851475143) -> int:
    """
    Returns the largest prime factor of `num`.

    Args:
        num (int): The number to factor.

    Returns:
        int: The largest prime factor.

    Explanation:
        Iterates through potential factors and divides `num` by them, keeping the largest prime factor.
    """
    i = 2
    while i * i < num:
        while num % i == 0:
            num //= i
        i += 1
    return num


def problem_four(digits: int = 3) -> int:
    """
    Finds the largest palindrome made from the product of two `digits`-digit numbers.

    Args:
        digits (int): The number of digits.

    Returns:
        int: The largest palindrome.

    Explanation:
        Calculates the product of all pairs of numbers within the digit range and checks for palindromes.
    """
    upper_limit = 10 ** digits - 1
    lower_limit = 10 ** (digits - 1)
    max_palindrome = 0
    for i in range(upper_limit, lower_limit - 1, -1):
        for j in range(i, lower_limit - 1, -1):
            product = i * j
            if product <= max_palindrome:
                break
            if str(product) == str(product)[::-1]:
                max_palindrome = product
    return max_palindrome

def problem_five(num: int = 20) -> int:
    """
    Finds the smallest positive number that is evenly divisible by all numbers from 1 to `num`.

    Args:
        num (int): The upper limit.

    Returns:
        int: The smallest number.

    Explanation:
        Iterates through numbers and checks if they are divisible by all numbers from 1 to `num`.
    """
    i = num
    while True:
        if all(i % j == 0 for j in range(1, num + 1)):
            return i
        i += num

#print(problem_one()) # 233168
#print(problem_two()) # 4613732
#print(problem_three()) # 6857
#print(problem_four()) # 906609
#print(problem_five()) # 232792560

