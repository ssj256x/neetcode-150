# --8<-- [start:generate_parenthesis]
def generate_parenthesis(n: int) -> list[str]:
    def generate(s: str, open_count: int, close_count: int):
        if len(s) == 2 * n:
            ans.append(s)
            return

        if open_count < n:
            generate(s + '(', open_count + 1, close_count)
        if close_count < open_count:
            generate(s + ')', open_count, close_count + 1)

    ans = []
    generate('', 0, 0)
    return ans


# --8<-- [end:generate_parenthesis]


print(generate_parenthesis(3))
