# --8<-- [start:subsets_with_dup]
def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    def generate(cur: int, path: list[int]):
        ans.append(path[:])

        for i in range(cur, len(nums)):
            if i > cur and nums[i - 1] == nums[i]:
                continue

            path.append(nums[i])
            generate(i + 1, path)
            path.pop()

    ans = []
    nums.sort()
    generate(0, [])
    return ans


# --8<-- [end:subsets_with_dup]

n = [1, 2, 2]
print(subsets_with_dup(n))
