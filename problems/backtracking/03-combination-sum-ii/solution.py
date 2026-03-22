# --8<-- [start:combination_sum_2]
def combination_sum_2(candidates: list[int], target: int) -> list[list[int]]:
    def find(cur: int, remaining: int, subset: list[int]):
        if remaining == 0:
            ans.append(subset[:])
            return

        for i in range(cur, size):
            if candidates[i] > remaining:
                break
            if i > cur and candidates[i] == candidates[i - 1]:
                continue

            subset.append(candidates[i])
            find(i + 1, remaining - candidates[i], subset)
            subset.pop()

    size = len(candidates)
    candidates.sort()
    ans = []
    find(0, target, [])
    return ans


# --8<-- [end:combination_sum_2]

c = [9, 2, 2, 4, 6, 1, 5]
t = 8
print(combination_sum_2(c, t))
