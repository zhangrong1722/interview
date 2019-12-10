class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def build(elements):
    """
    尾插法新建链表 与输入顺序相同 也可头插法 此时与输入顺序相反
    """
    if len(elements) == 0:
        return None
    header = Node(elements[0])
    p1 = header
    for i in range(1, len(elements)):
        temp = Node(elements[i])
        p1.next = temp
        p1 = p1.next
    return header

def traverse(header):
    while header is not None:
        print(header.val)
        header = header.next


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])
