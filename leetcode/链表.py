# 单向链表
'''
单向链表是一个结构，可以把这个结构创建一个类，
根据这个类创建一个对象，这个对象就是具体的相应链表

单链表的基本操作:
@节点的创建
@初始化单向链表
@插入节点: 1.头节点  2.中间节点  3.尾节点
@删除节点
@访问节点
@查找节点
'''
class ListNode:
    # 创建链表前需要先建立node类
    def __init__(self, val:int):
        self.val = val      # 初始化节点值
        self.next = None    # 初始化指向下一个节点的引用

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # dummy node

    def add_at_index(self, index:int, val:int):
        '''
        将val的值增加到指定index索引的位置
        : index索引 0 <= index <= size
        '''
        # 判断索引是否有效
        if index > self.size:
            return 
        index = max(0, index)
        # 创建新节点
        add_node = ListNode(val)
        # 获取头节点
        pred = self.head   # 是dummy node, 不占据索引位置
        # 根据index找到前驱节点
        '''
        :插入index 0(实际第一个dummy node)时, 前驱节点就是self.head, 
            循环次数为0, range(0)不执行
        :插入index n时,需从头节点开始移动n次才能到达前驱节点(即index=n-1的节点)
        '''
        for _ in range(index):
            pred = pred.next
        # 将新节点的下一个节点指向前驱节点的下一个节点
        add_node.next = pred.next
        # 将前驱节点的下一个节点指向新节点
        pred.next = add_node
        # 链表长度+1
        self.size += 1

    '''
    这个方法写完了可以直接在添加头节点和添加尾节点的地方直接进行调用
    '''
    def add_at_head(self, val:int) -> None:
        self.add_at_index(0, val)

    def add_at_tail(self, val:int) -> None:
        self.add_at_index(self.size, val)

    # 获取单链表中的第index个节点
    def get_node(self, index:int) -> int:

        '''
        获取index索引位置的值
        '''
        # 判断index是否有效
        if index < 0 or index >= self.size:
            return -1
        # 获取头节点
        pred = self.head
        # 遍历链表, index次
        for _ in range(index+1):
            pred = pred.next 
        # 返回index索引位置的值
        return pred.val

    # 删除数据
    def delete_at_index(self, index:int) -> None:
        '''
        删除index索引位置
        '''
        # 判断索引是否有效
        if index < 0 or index >= self.size:
            return
        # 获取头节点
        pred = self.head
        # 遍历链表，index次，找到前驱节点
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next
        # 链表长度-1
        self.size -= 1
    
    # 遍历链表
    def traverse(self):
        # 从头节点(dummy node)的下一个节点开始遍历
        cur = self.head.next
        while cur:      # 从头节点的下一个节点开始遍历
            # 对当前节点自行特定操作，例如: 打印节点的值
            print(cur.val, end=',')
            cur = cur.next      # 移动到下一个节点


if __name__ == '__main__':
    link = MyLinkedList()

    link.add_at_tail(1)
    link.add_at_tail(2)
    link.add_at_tail(3)

    link.add_at_head(5)   

    link.add_at_index(1,6)

    link.traverse()

