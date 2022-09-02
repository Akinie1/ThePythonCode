from collections import deque 

class Stack:
    def __init__(self) :
       self._data = deque();
       self._data.append(1)
       self._data.append(2)
       self._data.append(3)
    def push(self,data):   
        self._data.append(data);
#    This pop() is used to remove an element from the last which is at the last.
# so we can say this mehod  implements LILO because the element that is inserted last is the one that is removed out.
# and we want to implement the LIFO
    def pop(self):
        return self._data.pop();    
    def getData(self):
        return self._data; 
    def peek(self):
        return self._data[len(self._data)-1];
    def see(self):
        return self._data.popleft(); 
     
stack = Stack()
print(f"{stack.getData()}");     
# popped = stack.pop()
# print(f"{popped}");
# print(f"{stack.peek()}");    
popped = stack.see();
print(f"{popped}");





#Things I have learnt
# you can import deque from collections.
# you use the deque with the queue so you can use popleft() because if we use list is o(n) which means it goes through the list.


# This class makes the queue iterable but the first one is not that needed because it just gives us the length of the queues
# class IterableMixin:
#     "A mixin class to create an iterable and length reporting"
#     def __len__(self):
#         """Enable length reporting"""
#         return len(self._elements)

#     def __iter__(self):
#         """Make the queue iterable"""
#         while len(self) > 0:
#             yield self.pop()

# I learn that the yield is just like the return keyword