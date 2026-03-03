def has_duplicate(nums: list[int]) -> bool:
    """
    Returns True if any value appears more than once in `nums`.

    This implementation uses a set to track previously seen values.
    If a number is encountered that already exists in the set,
    a duplicate has been found and the function returns True immediately.

    Time Complexity: O(n)
    Space Complexity: O(n)

    :param nums: List of integers.
    :return: True if duplicates exist, otherwise False.
    """
    seen: set[int] = set()

    for n in nums:
        if n in seen:
            return True
        seen.add(n)

    return False


l = [1, 1, 2, 3]
print(has_duplicate(l))

l = [1, 2, 3]
print(has_duplicate(l))
