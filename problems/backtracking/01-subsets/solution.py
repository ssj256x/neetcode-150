def subsets_approach_1_backtracking(nums: list[int]) -> list[list[int]]:
    def generate(idx, cur):
        if idx == i:
            ans.append(cur[:])

        for j in range(idx, n):
            cur.append(nums[j])
            generate(j + 1, cur)
            cur.pop()

    ans = []
    n = len(nums)
    for i in range(n + 1):
        generate(0, [])

    return ans


# --8<-- start:solution_backtracking
def subsets_approach_2_backtracking(nums: list[int]) -> list[list[int]]:
    def generate(start: int, path: list[int]):
        ans.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            generate(i + 1, path)
            path.pop()

    ans = []
    generate(0, [])
    return ans


# --8<-- end:solution_backtracking

# --8<-- start:solution_xor
def subsets_approach_3_xor(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    ans = []

    for mask in range(1 << n):
        subsets = []
        for i in range(n):
            print(f'{mask & (1 << i):03b} - {mask & (1 << i)}')
            if mask & (1 << i):
                subsets.append(nums[i])

        ans.append(subsets)
        print(f'--- {subsets} ---')

    return ans


# --8<-- end:solution_xor

l = [1, 2, 3]
# print(subsets_approach_2_backtracking(l))
print(subsets_approach_3_xor(l))
