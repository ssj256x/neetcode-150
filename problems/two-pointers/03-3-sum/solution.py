def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    ans = []

    for i in range(len(nums)):

        # skip duplicate first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1
        target = -nums[i]
        while j < k:
            sum = nums[j] + nums[k]
            if sum > target:
                k -= 1
            elif sum < target:
                j += 1
            else:
                triplet = [nums[i], nums[j], nums[k]]
                ans.append(triplet)
                j += 1
                k -= 1

                # skip duplicates for j
                while j < k and nums[j] == nums[j - 1]:
                    j += 1

                # skip duplicates for k
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1

    return ans


n = [-1, 0, 1, 2, -1, -4]
print(three_sum(n))
