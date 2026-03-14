def product_except_self_division(nums: list[int]):
    product = 1
    zeros = 0
    z_idx = 0

    for i, n in enumerate(nums):
        if n == 0:
            zeros += 1
            z_idx = i
        else:
            product *= n

        if zeros == 2:
            return [0] * len(nums)

    if zeros == 1:
        ans = [0] * len(nums)
        ans[z_idx] = product
        return ans

    return [int(product / n) for n in nums]


def product_except_self_prefix_suffix(nums: list[int]):
    n = len(nums)
    output = [1] * n

    # prefix products
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    # suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output


numbers = [1, 2, 4, 6]
print(product_except_self_division(numbers))
numbers = [-1, 0, 1, 2, 3]
print(product_except_self_division(numbers))
