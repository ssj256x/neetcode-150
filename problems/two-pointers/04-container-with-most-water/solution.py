def max_area(heights: list[int]) -> int:
    l = 0
    r = len(heights) - 1
    max_capacity = 0

    while l < r:
        width = r - l
        height = min(heights[l], heights[r])
        capacity = width * height
        max_capacity = max(capacity, max_capacity)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return max_capacity


h = [1, 7, 2, 5, 4, 7, 3, 6]
print(max_area(h))
h = [2, 2, 2]
print(max_area(h))
