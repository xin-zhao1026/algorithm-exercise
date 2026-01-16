# 队列实现
'''
队列遵循FIFO原则, 基本操作：
enqueue(入队): 将数据放入队尾
dequeue(出队): 将队首数据移除
代码实现操作步骤：
-初始化
-入队
-出队
-获取队长度
-判断是否为空
-访问队首元素
-转成列表
'''

class MyQueue:
    def __init__(self):
        self.items = []
    
    def push(self, val:int) -> None:
        '''入队'''
        self.items.append(val)
    
    def pop(self) -> int:
        '''出队'''
        return self.items.pop(0)
    
    def size(self) -> int:
        '''队列大小'''
        return len(self.items)
    
    def is_empty(self) -> bool:
        '''队列是否为空'''
        return self.size() == 0

    def peek(self) -> int:
        '''获取队首元素'''
        return self.items[0]
    
    def to_list(self) -> list:
        return self.items


# 环形队列实现
'''
增加数据的索引 = (队首索引+数据大小) % 空间大小
add_index = (head + size) % capacity
下个队首索引 = (队首索引+1) % 空间大小
new_head = (head + 1) % capacity 

代码实现操作步骤：
-初始化
-获取队列容量capacity
-判断是否为空
-入队
-出队
-访问队首元素
-转成列表
'''
class ArrayQueue:
    def __init__(self, size:int):
        self.items = [0] * size
        self.size = 0
        self.head = 0   # 队首所在索引位置

    def capacity(self) -> int:
        '''返回队列容量'''
        return len(self.items)

    def is_empty(self) -> bool:
        '''判断队列是否为空'''
        return self.size == 0
    
    def peek(self) -> int:
        '''返回队首元素'''
        # 判断队列是否为空，空：抛出异常
        if self.is_empty():
            raise Exception ("Queue is empty")
        return self.items[self.head]
    
    def push(self, val:int):
        '''入队'''
        # 判断队列是否已满
        if self.size == self.capacity():
            raise Exception("Queue is full")
        # 计算新元素的位置
        index = (self.head + self.size) % self.capacity()
        self.items[index] = val   # 新元素插入队尾
        self.size += 1   # 队列元素个数+1

    def pop(self) -> int:
        '''出队'''
        data = self.peek()
        # 更新 新队首位置
        self.head = (self.head + 1) % self.capacity()
        # 更新队列元素个数
        self.size -= 1
        return data
    
    def to_list(self):
        '''将队列转换为列表'''
        # 创建列表，用于保存队列元素
        rs = [0] * self.size
        head_index = self.head
        # 遍历队列元素，从head开始
        for i in range(self.size):
            index = head_index % self.capacity()
            rs[i] = self.items[index]
            head_index += 1
        return rs


if __name__ == '__main__':
    # queue = MyQueue()
    # queue.push(1)
    # queue.push(2)
    # queue.push(3)
    # print(f'转成列表后: {queue.to_list()}')

    # print(f'出队: {queue.pop()}')
    # print(f'转成列表后: {queue.to_list()}')

    # print(f'访问队首: {queue.peek()}')
    # print(f'转成列表后: {queue.to_list()}')

    # print(f'队列是否为空: {queue.is_empty()}')
    # print(f'队列元素个数: {queue.size()}')

    queue = ArrayQueue(5)
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push(5)
    print(queue.to_list())
    print(f'出队元素是: {queue.pop()}')
    queue.push(6)
    print(queue.to_list())
