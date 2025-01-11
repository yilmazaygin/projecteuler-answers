def problem_six(num: int = 100) -> int:
    """
    Calculates the difference between the square of the sum of the first `num` numbers
    and the sum of the squares of the first `num` numbers.

    Args:
        num (int): The number up to which to calculate.

    Returns:
        int: The difference between the square of the sum and the sum of squares.

    Explanation:
        The function first calculates the sum of squares and the sum of numbers. It then returns the 
        difference between the square of the sum and the sum of squares.
    """
    sum1, sum2 = 0, 0
    for i in range(num + 1):
        sum1 += i**2
        sum2 += i

    return sum2**2 - sum1

def problem_seven(n: int = 10001) -> int:
    """
    Returns the `n`th prime number.

    Args:
        n (int): The position of the prime number to return.

    Returns:
        int: The `n`th prime number.

    Explanation:
        This function iterates through natural numbers, checking each one for primality, 
        and counts primes until the `n`th prime is found.
    """
    import math
    start = 2
    count = 0
    while True:
        if all([start % i for i in range(2, int(math.sqrt(start)) + 1)]) != 0:
            count += 1
            if count == n:
                return start
        start += 1 

def problem_eight(digits: int = 13) -> int:
    """
    Finds the greatest product of `digits` consecutive digits in a large number.

    Args:
        digits (int): The number of consecutive digits.

    Returns:
        int: The greatest product of `digits` consecutive digits.

    Explanation:
        The function iterates through the large number in chunks of `digits` consecutive digits, 
        calculates the product for each chunk, and returns the largest product found.
    """
    examples_number = (
    "73167176531330624919225119674426574742355349194934969835203127745063262395783180"
    "16984801869478851843858615607891129494954595017379583319528532088055111254069874"
    "71585238630507156932909632952274430435576689664895044524452316173185640309871112"
    "17223831136222989342338030813533627661428280644448664523874930358907296290491560"
    "44077239071381051585930796086670172427121883998797908792274921901699720888093776"
    "65727333001053367881220235421809751254540594752243525849077116705560136048395864"
    "46706324415722155397536978179778461740649551492908625693219784686224828397224137"
    "56570560574902614079729686524145351004748216637048440319989000889524345065854122"
    "75886668811642717147992444292823086346567481391912316282458617866458359124566529"
    "47654568284891288314260769004224219022671055626321111109370544217506941658960408"
    "07198403850962455444362981230987879927244284909188845801561660979191338754992005"
    "24063689912560717606058861164671094050775410022569831552000559357297257163626956"
    "1882670428252483600823257530420752963450"
    )
    max_product = 0 
    
    for i in range(len(examples_number) - digits + 1):
        product = 1
        for j in range(digits):
            product *= int(examples_number[i + j])
        max_product = max(max_product, product)
    
    return max_product

def problem_nine(sum_value: int = 1000) -> int:
    """
    Finds the product of the Pythagorean triplet that sums to `sum_value`.

    Args:
        sum_value (int): The sum of the triplet.

    Returns:
        int: The product of the Pythagorean triplet.

    Explanation:
        The function checks all possible combinations of `a`, `b`, and `c` such that 
        `a + b + c = sum_value`, and verifies if they satisfy the Pythagorean theorem.
    """
    import math
    for a in range(1, sum_value // 3):
        for b in range(a + 1, sum_value // 2):
            c = sum_value - a - b
            if a * a + b * b == c * c:
                return a * b * c

def problem_ten(num: int = 1000000) -> int:
    """
    Calculates the sum of all prime numbers below `num`.

    Args:
        num (int): The upper limit (exclusive).

    Returns:
        int: The sum of all prime numbers below `num`.

    Explanation:
        The function iterates through all numbers below `num`, checking if they are prime and 
        adds them to the sum if they are prime.
    """
    import math
    sum_value = 0
    for i in range(2, num):
        if all([i % j for j in range(2, int(math.sqrt(i)) + 1)]) != 0:
            sum_value += i
    return sum_value

#print(problem_six()) # 25164150
#print(problem_seven()) # 104743
#print(problem_eight()) # 23514624000
#print(problem_nine()) # 31875000
#print(problem_ten()) # 142913828922
