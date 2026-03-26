# --8<-- [start:letter_combinations]
def letter_combinations(digits: str) -> list[str]:
    if digits == "":
        return []

    def generate(idx: int, s: list[str]):
        if len(s) == len(digits):
            ans.append(''.join(s))
            return

        for i in range(idx, len(digits)):
            for letter in lookup[digits[i]]:
                s.append(letter)
                generate(i + 1, s)
                s.pop()

    lookup = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    ans = []
    generate(0, [])
    return ans


# --8<-- [end:letter_combinations]

print(letter_combinations('594'))
