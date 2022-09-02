# Let's create Stacks
from collections import deque
from heapq import heappush,heappop
from itertools import count
from typing import Iterable


# create a iterable class 

class IterableMixin:
    # return the length
      def __len__(self):
            return len(self._element);
      def __iter__(self):
         while len(self)>0:
             yield self.pop();


class Queue(IterableMixin):
    def __init__(self,*element):
        self._element = deque(*element);

    def push(self,element):
        self._element.append(element)

    def pop(self):
        return self._element.popleft()

class Stack(Queue):

     def pop(self):
        return self._element.pop()


class PriorityQueue(IterableMixin):
   def __init__(self): 
    self._element = [];
    self._counter = count()     

   def push(self,priority,value):
       heappush(self._element,(-priority,next(self._counter)),value); 

   def pop(self):
       return  heappop(self._element)[-1];

