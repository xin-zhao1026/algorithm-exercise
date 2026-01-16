# 删除指定位置一个元素
def remove(nums:list[int], idx:int) -> list:
    '''
    nums: 原始数据
    idx: 要删除元素的位置
    思路: 删除[idx]元素后，后面元素向前偏移一个位置
    '''
    for i in range(idx,len(nums)-1):
        nums[i] = nums[i+1]
    nums.pop()
    return nums

# 遍历数组元素：三种方法
def traverse(nums:list[int]):
    # 1.通过索引
    for i in range(len(nums)):
        print(nums[i],end=',')

    # 2.通过元素
    for num in nums:
        print(num,end=',')
    
    # 3.通过迭代器
    for idx, num in enumerate(nums):
        print(idx,num)

# 查找目标元素
def find(nums:list[int], target:int) -> int:
    for idx, num in enumerate(nums):
        if num == target:
            return idx
    return -1

# 扩容数组
def extend(nums:list[int]) -> list:
    '''
    思路: 1.创新新数组  2.复制原数组到新数组  3.返回新数组
    '''
    new_nums = [0] * (len(nums)*2)
    for idx, num in enumerate(nums):
        new_nums[idx] = num
    return new_nums

if __name__ == '__main__':
    nums:list[int] = [5,2,1,3,1,4]
    idx = 2
    # print(remove(nums,idx))
    # print(traverse(nums))
    target = 1
    # print(find(nums,target))
    print(extend(nums))