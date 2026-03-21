# --8<-- start:combination_sum
def combination_sum(nums: list[int], target: int) -> list[list[int]]:
    def find(cur: int, remaining: int, subset: list[int]):
        if remaining == 0:
            ans.append(subset[:])
        if remaining < 0:
            return

        for i in range(cur, len(nums)):
            subset.append(nums[i])
            find(i, remaining - nums[i], subset)
            subset.pop()

    ans = []
    find(0, target, [])
    return ans


# --8<-- end:combination_sum

# --8<-- start:combination_sum_with_sort
def combination_sum_with_sort(nums: list[int], target: int) -> list[list[int]]:
    def find(cur: int, remaining: int, subset: list[int]):
        if remaining == 0:
            ans.append(subset[:])

        for i in range(cur, len(nums)):
            if nums[i] > remaining:
                break

            subset.append(nums[i])
            find(i, remaining - nums[i], subset)
            subset.pop()

    nums.sort()
    ans = []
    find(0, target, [])
    return ans


# --8<-- end:combination_sum_with_sort

n = [2, 5, 6, 9]
t = 9
print(combination_sum_with_sort(n, t))
