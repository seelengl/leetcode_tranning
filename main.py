

def serchInsert(nums, target):
    index = 0
    array_len = len(nums)
    last_n = 0
    # for n_min in nums:
    #     if n_min > target:
    #         return index
    for n in nums:
        if n == target:
            return index
        if last_n < target < n:
            return index
        last_n = n
        index += 1
        if index == array_len and n <= target:
            return index
        elif n > target:
            return 0


def two_sum(nums, target):
    for num in nums:
        i = nums.index(num) + 1
        while i < len(nums):
            if num + nums[i] == target:
                return [nums.index(num), i]
            i += 1
    return -1


# Press the green button in the gutter to run the script.
nums = [1, 3, 5, 6, 8, 10]
nums2 = [10, 8, 6, 5, 3, 1]
nums3 = [3, 3, 3, 3, 3, 3]
nums4 = [3, 2, 3, 4, 3, 4]
nums5 = [3, 2, 4]
if __name__ == '__main__':
    print(two_sum(nums5, 6))

