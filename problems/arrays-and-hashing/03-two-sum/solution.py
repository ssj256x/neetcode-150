"""
Problem: Two Sum
Pattern: Arrays | Hash Map | Complement Lookup
Difficulty: Easy
Source: NeetCode
"""


def two_sum_naive(nums: list[int], target: int) -> list[int]:
    """
    Returns the indices of two elements in `nums` whose sum equals `target`.

    This implementation checks all possible pairs using a nested loop.
    It compares every combination of indices to find a matching sum.

    Time Complexity: O(n^2)
    Space Complexity: O(1)

    :param nums: List of integers.
    :param target: Target sum to find.
    :return: A list containing the two indices if a valid pair exists,
             otherwise [-1, -1].
    """
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]

    return [-1, -1]


def two_sum_map(nums: list[int], target: int) -> list[int]:
    """
    Returns the indices of two elements in `nums` whose sum equals `target`.

    This implementation uses a hash map to store the complement
    (target - current_value) as a key and its index as the value.
    While iterating, if the current number exists in the map,
    a matching pair has been found.

    Time Complexity: O(n)
    Space Complexity: O(n)

    :param nums: List of integers.
    :param target: Target sum to find.
    :return: A list containing the two indices if a valid pair exists,
             otherwise [-1, -1].
    """
    lookup: dict[int, int] = {}

    for i in range(len(nums)):
        if nums[i] in lookup:
            return [lookup[nums[i]], i]

        lookup[target - nums[i]] = i

    return [-1, -1]


print(two_sum_map([4, 5, 6], 10))
