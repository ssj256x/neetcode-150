def two_sum(numbers: list[int], target: int) -> list[int]:
    l = 0
    r = len(numbers) - 1

    while l < r:
        sum = numbers[l] + numbers[r]

        if sum == target:
            return [l + 1, r + 1]
        if sum < target:
            l += 1
        if sum > target:
            r -= 1

    return []


nums = [1, 2, 3, 4]
t = 3
print(two_sum(nums, t))
