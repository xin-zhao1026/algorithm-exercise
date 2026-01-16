'''
栈的几项基本操作：
1. 初始化
2. 入栈
3. 出栈
4. 获取栈长度
5. 判断是否为空
6. 访问栈顶元素
7. 转成列表
'''
class ArrayStack:
    # 构造一个空栈
    def __init__(self):
        self._data:list[int] = []
    
    # 入栈
    def push(self, val:int):
        self._data.append(val)
    
    # 出栈
    def pop(self):
        if self.is_empty():  # 判断栈是否为空
            raise Exception("栈为空")
        return self._data.pop()
    
    # 判断空栈
    def is_empty(self):
        return len(self._data) == 0
    
    # 获取栈长度
    def size(self):
        return len(self._data)
    
    # 访问栈顶元素
    def top(self):
        if self.is_empty():
            raise Exception("栈为空")
        return self._data[-1]
    
    # 转成列表
    def to_list(self):
        return self._data
    
if __name__ == '__main__':
    stack = ArrayStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(f'获取出栈数据: {stack.pop()}')
    print(f'栈转成列表: {stack.to_list()}')
    print(f'获取栈顶: {stack.top()}')
    print(f'获取栈长度: {stack.size()}')

