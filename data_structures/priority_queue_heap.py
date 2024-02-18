# Remove all newlines to paste into Python console


class PriorityQueueMaxHeap:

    def __init__(self) -> None:
        self._heap = []

    def _parent(self, index) -> [int | None, int | None]:
        if not index:
            return None, None
        parent_index = (index - 1) // 2
        return self._heap[parent_index], parent_index

    def _left(self, index) -> [int | None, int | None]:
        left_index = index*2 + 1
        try:
            return self._heap[left_index], left_index
        except IndexError:
            return None, None

    def _right(self, index) -> [int | None, int | None]:
        right_index = index*2 + 2
        try:
            return self._heap[right_index], right_index
        except IndexError:
            return None, None

    def _get_c(self, index) -> [int | None, int | None]:
        left, left_index = self._left(index)
        right, right_index = self._right(index)
        c, c_index = None, None
        if left is not None and right is not None:
            c, c_index = (
                left if left > right else right,
                left_index if left > right else right_index
            )
        else:
            c, c_index = (
                left if left is not None else right,
                left_index if left is not None else right_index
            )
        return c, c_index

    def size(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        return not self._heap

    def peek(self) -> int:
        if not self._heap:
            return None
        return self._heap[0]

    def push(self, item) -> None:
        self._heap.append(item)
        index = len(self._heap) - 1
        parent, parent_index = self._parent(index)
        while parent is not None and self._heap[index] > parent:
            self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            index = parent_index
            parent, parent_index = self._parent(index)

    def pop(self) -> int:
        if not self._heap:
            return None
        if len(self._heap) == 1:
            return self._heap.pop()
        result = self._heap[0]
        last = self._heap.pop()
        index = 0
        self._heap[0] = last
        c, c_index = self._get_c(index)
        while c is not None and c > self._heap[index]:
            self._heap[index], self._heap[c_index] = self._heap[c_index], self._heap[index]
            index = c_index
            c, c_index = self._get_c(index)
        return result

    def add_all(self, l) -> None:
        for item in l:
            self.push(item)


# Paste this below to try it out!
h = PriorityQueueMaxHeap()
h.add_all([45, 40, 25, 20, 35, 10, 15])

h.push(75), h._heap
h.pop(), h._heap
