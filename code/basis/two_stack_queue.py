# -*- coding:utf-8 -*-

class Queue:
    stack1, stack2 = list(), list()
    def push(self, node):
        self.stack1.append(node)
        
    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return None
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    
class TwoStack:
    def twoStack(self, ope, n):

        q = Queue()
        res = list()
        for e in ope:
            if e == 0:
                res.append(q.pop())
            else:
                q.push(e)
        return res
    


s = TwoStack()
print s.twoStack([251,399,0,428,21,0], 6)