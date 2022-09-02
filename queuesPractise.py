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

class Queue(IterableMixin):
    """A class that implements a queue (FIFO Queue)"""
    
    def __init__(self, *elements):
        self._elements = deque(*elements)

    def push(self, element):
        """Add element to end of queue"""
        self._elements.append(element)

    def pop(self):
        """Remove element from queue"""
        return self._elements.popleft()
    def see(self):
          return self._elements




Queues = Queue([1,2,3,4,5,6,7,8,9,10,11]);  
Queues.push("samuel");     
Queues.pop();
print(f"{Queues.see()}");