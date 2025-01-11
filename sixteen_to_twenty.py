def problem_sixteen(power_of_two: int = 1000) -> int:
    """
    This Python code calculates the sum of the digits of the number 2 raised to the power of the given power_of_two.

    Args:
        power_of_two : int : 1000 : The power to which the number 2 is raised.

    Returns:
        int : The sum of the digits of the number 2 raised to the power of the given power_of_two.

    Explanation:
        The function calculates the number 2 raised to the power of the given power_of_two.
        It then calculates the sum of the digits of the number
    """
    return sum([int(x) for x in str(2**power_of_two)])



def problem_seventeen(num:int = 1000) -> int:
    """
    This Python code converts all numbers up to a given num number into text and calculates the total length of the remaining characters after removing the spaces and hyphen (-) characters in these texts.

    Args:
        num : int : 1000 : The number up to which the numbers are converted into text.

    Returns:
        int : The total length of the remaining characters after removing the spaces and hyphen (-) characters in the texts of all numbers up to the given

    Explanation:
        The function uses the num2words library to convert all numbers up to the given num number into text.
        It then calculates the total length of the remaining characters after removing the spaces and hyphen (-) characters in these texts.
    """
    from num2words import num2words # Need to install num2words
    return sum([len(num2words(x).replace(" ", "").replace("-", "")) for x in range(1, num+1)])

def problem_eighteen():
    """
    Finds the maximum path sum in a fixed triangle.
    Returns:
        int: Maximum path sum
    """
    # Triangle weights
    triangle = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
    ]

    # Calculate max path sum
    for row in range(len(triangle) - 2, -1, -1):
        for col in range(len(triangle[row])):
            triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])

    return triangle[0][0]


#print(problem_sixteen())  # 1366
#print(problem_seventeen())  # 21124
#print(problem_eighteen()) # 1074