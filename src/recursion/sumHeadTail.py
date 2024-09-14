def sum(numbers: list[int]) -> int:
    """
    Calculates the sum of all numbers in the given list.
    Args:
        numbers (list[int]): A list of integers.
    Returns:
        int: The sum of all numbers in the list.
    """
    if len(numbers) == 0:
        return 0
    
    head, tail = numbers[0], numbers[1:]
    return head + sum(tail)

nums = [1, 2, 3, 4, 5]
print('Sum', nums, 'is', sum(nums))

nums = [5, 2, 4, 8]
print('Sum', nums, 'is', sum(nums))

nums = [1, 10, 100, 1000]
print('Sum', nums, 'is', sum(nums))

nums = []
print('Sum', nums, 'is', sum(nums))