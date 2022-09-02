from collections import deque
from heapq import heappush, heappop
from itertools import count


class IterableMixin:
    "A mixin class to create an iterable and length reporting"
    def __len__(self):
        """Enable length reporting"""
        return len(self._elements)

    def __iter__(self):
        """Make the queue iterable"""
        while len(self) > 0:
            yield self.pop()


class PriorityQueue(IterableMixin):
    """A class that implements a priority queue"""

    def __init__(self):
        self._elements = []
        self._counter = count()
    
    def push(self, priority, value):
        heappush(self._elements, (-priority, next(self._counter), value))
    
    def pop(self):
        return heappop(self._elements)[-1]




PriorityQueues = PriorityQueue();
PriorityQueues.push(,5);
print(f"{PriorityQueues}");