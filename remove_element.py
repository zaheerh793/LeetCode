def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    count = 0
    for v in nums:
        if v != val:
            nums[count] = v
            count += 1
    return nums


if __name__ == '__main__':
    res = removeElement([1, 2, 3, 4, 5], 3)
    print(res)
