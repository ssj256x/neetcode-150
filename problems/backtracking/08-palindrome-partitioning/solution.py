# --8<-- [start:partition]
def partition(s: str) -> list[list[str]]:
    def is_palindrome(l: int, r: int):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def find(start: int, path: list[str]):
        if start == len(s):
            ans.append(path[:])

        for end in range(start, len(s)):
            if is_palindrome(start, end):
                path.append(s[start: end + 1])
                find(end + 1, path)
                path.pop()

    ans = []
    find(0, [])
    return ans


# --8<-- [end:partition]

# --8<-- [start:partition_dp_mem]
def partition_dp_mem(s: str) -> list[list[str]]:
    def is_palindrome(l: int, r: int):
        if dp[l][r] is not None:
            return dp[l][r]

        i, j = l, r
        while i < j:
            if s[i] != s[j]:
                dp[l][r] = False
                return False
            i += 1
            j -= 1

        dp[l][r] = True
        return True

    def find(start: int, path: list[str]):
        if start == len(s):
            ans.append(path[:])
            return

        for end in range(start, len(s)):
            if is_palindrome(start, end):
                path.append(s[start: end + 1])
                find(end + 1, path)
                path.pop()

    ans = []
    n = len(s)
    dp: list[list[None | bool]] = [[None for _ in range(n)] for _ in range(n)]
    find(0, [])
    return ans


# --8<-- [end:partition_dp_mem]

string = 'mississippi'
print(partition_dp_mem(string))
