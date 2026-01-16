# 建立数组
arr:list[int] = [0] * 8
nums:list[int] = [5,2,1,3,1,4]

# 访问随机数组的第三个元素
def random_access(nums:list[int]) -> int:
    return nums[2]


# 随机访问数组中的一个元素
def random_access2(nums:list[int]) -> int:
    from random import randint
    random_idx = randint(0,len(nums)-1)
    return nums[random_idx]


# 在指定位置insert一个元素
def insert(nums:list[int], num:int, idx:int) ->list:
    '''
    nums: 数组
    num: 插入的元素
    idx: 插入的位置
    '''
    # 插入新元素后，原数组最后一个元素被消失，因为nums容量已经满了
    # 先给数组nums最后扩容一个位置，元素: 占位符None
    nums.append(None)
    for i in range(len(nums)-1, idx, -1):
        nums[i] = nums[i-1]
    nums[idx] = num
    return nums




if __name__ == '__main__':
    # n:list[int] = [5,2,1,3,1,4,6,6,6]
    # print(random_access2(n))

    nums:list[int] = [5,2,1,3,1,4]
    num = 9
    idx = 2
    print(insert(nums,num,idx))

