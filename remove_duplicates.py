def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dic = {}
    for i in sorted(nums):
        dic[i] = i
    nums[:] = sorted(dic.keys())
    return len(nums)
