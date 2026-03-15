def longest_consecutive_sequence_brute_force(nums: list[int]):
    longest = 0

    for num in nums:
        current = num
        length = 1

        while current + 1 in nums:
            current += 1
            length += 1

        longest = max(longest, length)

    return longest


def longest_consecutive_sequence_sub_optimal(nums: list[int]):
    if not nums:
        return 0

    nums.sort()
    longest = 1
    cur = 1

    for i in range(1, len(nums)):
        if nums[i - 1] == nums:
            continue
        elif nums[i - 1] == nums[i] - 1:
            longest += 1
        else:
            longest = max(longest, cur)
            cur = 1

    return max(longest, cur)


def longest_consecutive_sequence_optimal(nums: list[int]):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Start of sequence
        if num - 1 not in num_set:
            count = 1
            cur = num
            while cur + 1 in num_set:
                count += 1
                cur += 1

            longest = max(longest, count)

    return longest


n = [2, 20, 4, 10, 3, 4, 5]
print(longest_consecutive_sequence_optimal(n))
n = [0, 3, 2, 5, 4, 6, 1, 1]
print(longest_consecutive_sequence_optimal(n))
