def find_target_element_index(nums, target):
    index = "0"
    for i in range(len(nums)):
        if nums[i] > target:
            temp = nums[i]
            nums[i] = target
            target = temp
            if type(index) == str:
                index = i
        elif nums[i] == target:
            index = i
            break
        if i >= len(nums) - 1:
            nums.append(target)
    if type(index) == str:
        index = "Not present"

    return nums, index
def find_target_element_index_2(nums, target):
    for i, tar in enumerate(nums):
        if tar == target:
            return i
    return "not found"


if __name__ == "__main__":
    print(find_target_element_index([1,3,4,5,6,7], 4))
    print(find_target_element_index_2([1,3,4,5,6,7], 4))