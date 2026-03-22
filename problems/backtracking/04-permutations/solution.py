# --8<-- [start:permute_with_seen]
def permute_with_seen(nums: list[int]) -> list[list[int]]:
    def generate(path: list[int]):
        if len(path) == len(nums):
            ans.append(path[:])
            return

        for i in range(len(nums)):
            if seen[i]:
                continue

            path.append(nums[i])
            seen[i] = True
            generate(path)
            seen[i] = False
            path.pop()

    seen = [False] * len(nums)
    ans = []
    generate([])
    return ans


# --8<-- [end:permute_with_seen]

# --8<-- [start:permute_with_swap]
def permute_with_swap(nums: list[int]) -> list[list[int]]:
    def generate(start: int):
        if start == len(nums):
            ans.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            generate(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    ans = []
    generate(0)
    return ans


# --8<-- [end:permute_with_swap]

l = [1, 2, 3, 4]
print(permute_with_swap(l))
print(permute_with_seen(l))
