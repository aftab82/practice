"""https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem"""
class MyQueue(object):
    def __init__(self):
        self.q = []
        self.dq = []

    def flip_stack(self):
        if len(self.dq) == 0:
            while len(self.q) != 0:
                self.dq.append(self.q.pop())

    def peek(self):
        self.flip_stack()
        if len(self.dq) != 0:
            return self.dq[-1]
        else:
            return None

    def pop(self):
        val = self.peek()
        if val:
            self.dq.pop()
        return val

    def put(self, value):
        self.q.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
