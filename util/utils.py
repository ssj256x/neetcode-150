def print_dp_table(s: str, dp: list[list[bool | None]]):
    n = len(s)

    # Determine width based on largest index (for alignment)
    width = len(str(n - 1))  # handles 9 → 10 → 100 etc.
    cell_w = max(3, width)  # minimum spacing for readability

    def fmt(x):
        return str(x).rjust(cell_w)

    # Header: indices
    print(" " * (width + 5) + "| " + " ".join(fmt(i) for i in range(n)))

    # Header: characters
    print(" " * (width + 5) + "| " + " ".join(fmt(c) for c in s))

    # Divider
    total_width = (width + 5) + 2 + (cell_w + 1) * n
    print("-" * total_width)

    # Rows
    for i in range(n):
        row = f"{str(i).rjust(width)}   {s[i]} | "

        for j in range(n):
            if dp[i][j]:
                val = "T"
            elif dp[i][j] is False:
                val = "F"
            else:
                val = "."

            row += fmt(val) + " "

        print(row)
