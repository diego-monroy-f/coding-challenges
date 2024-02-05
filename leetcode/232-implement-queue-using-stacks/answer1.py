# https://leetcode.com/problems/implement-queue-using-stacks/
# Own solution -- after watching course

class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if self.s2:
            return self.s2.pop()
        else:
            self._transfer()
            return self.s2.pop() if self.s2 else None

    def peek(self) -> int:
        if self.s2:
            return self.s2[-1]
        else:
            self._transfer()
            return self.s2[-1] if self.s2 else None

    def empty(self) -> bool:
        return not self.s1 and not self.s2

    def _transfer(self) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()