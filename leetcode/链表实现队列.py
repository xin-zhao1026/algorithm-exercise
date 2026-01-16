# 链表实现队列
'''
基本操作：
初始化节点、链表队列
队列是否为空
入队
获取头节点
出队
队列转化列表
'''

class ListNode:
    def __init__(self, x:int):
        self.val = x
        self.next = None

class LinkedQueue:
    '''初始化列表'''
    def __init__(self):
        self.head = None    # 队头指针
        self.tail = None    # 队尾指针
        self.size = 0       # 队列长度
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    def push(self, val):
        '''入队：先检查队列是否为空'''
        # 创建节点
        node = ListNode(val)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail =  node
        self.size += 1

    def peek(self) -> int:
        '''获取头节点: 先检查队列是否为空'''
        if self.head is None:
            return None
        else:
            return self.head.val
    
    def pop(self) -> int:
        '''出队: 先检查队列是否为空'''
        data = self.peek()
        # 更新队头指针
        self.head = self.head.next
        self.size -= 1
        return data
    
    def to_list(self) -> list:
        '''队列为空: 返回空列表'''
        if self.is_empty():
            return []
        else:
            rs = []
            element = self.head
            while element:
                rs.append(element.val)
                element = element.next
        return rs
    

if __name__ == '__main__':
    queue = LinkedQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.to_list())
    print(queue.peek())
    print(queue.pop())
    print(queue.to_list())