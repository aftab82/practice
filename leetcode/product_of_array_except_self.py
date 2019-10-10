"""
Solution to https://leetcode.com/problems/product-of-array-except-self/
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division and in O(n)?
Follow-up: Solve with constant space complexity? (output array can be excluded)
"""


def product_except_self1(nums):

    length = len(nums)
    answer = [0]*length
    answer[0] = 1

    for i in range(1, length):
        answer[i] = nums[i - 1] * answer[i - 1]

    r = 1
    for i in reversed(range(length)):
        answer[i] = answer[i] * r
        r *= nums[i]

    return answer


def product_except_self(nums):
    products = [1] * len(nums)
    left = 0
    left_product = 1
    right = len(nums) - 1
    right_product = 1
    for _ in range(len(nums)):
        if left != right:
            products[left] *= left_product
            products[right] *= right_product
        else:
            products[left] = left_product * right_product
        left_product *= nums[left]
        right_product *= nums[right]
        left += 1
        right -= 1

    return products


print(product_except_self1([1, 0]))  # [0, 1]
print(product_except_self1([0, 0]))  # [0, 0]
print(product_except_self1([1, 1]))  # [1, 1]
print(product_except_self1([1, 0, 1]))  # [0, 1, 0]
print(product_except_self1([1, 2, 3, 4, 5]))  # [120, 60, 40, 30, 24]
print(product_except_self1([3, 2, 1]))  # [2, 3, 6]
print(product_except_self1([1, 2, 3, 4]))  # [24, 12, 8, 6]
