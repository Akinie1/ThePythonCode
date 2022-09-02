class Node:
    """
    A class that implements a node of a linked list
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, item):
        self.item = item

    def set_next(self, next):
        self.next = next

    def __repr__(self):
        return self.data


class LinkedList:
    """
    A class that implements a linked list data structure
    """
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node # here node is the head and is assigned to the self.head.

            for item in nodes:
                node.next = Node(data=item)
                node = node.next  #here node is the tail

    def insert_first(self, node):
        """
        Insert new node as the head of linkedlist
        """
        node.next = self.head
        self.head = node
        linkedlist = []
        linkedlist.append(self.head)
        linkedlist.append('->');       
        linkedlist.append(node.next);
        return  linkedlist

#inserting an element at the last.
    def insert_last(self, node):
        #Note that the node that is coming is the head. 
        #because we have to insert our head and tail values in the Node class and this automatically returns the head

        """
        Insert node to the end of linkedlist
        """
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass #next.
        #since self is the head and tail, we then can assign the current_node.next to the node we pass in. 
        current_node.next = node
        return node

    def insert_after(self, target_node_data, new_node):
        """
        Insert new node after a target node in a linkedlist
        """
        if self.head is None:
            raise Exception("Linkedlist is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next # i dey bab. Just picture the man's drawing on the board. 
                node.next = new_node
                return

        raise Exception(f"Node with data {target_node_data} not found")
#Make linkedList iterable.
    def __iter__(self):
        """
        Make the linkedlist iterable
        """
        node = self.head
        while node is not None:
            yield node
            node = node.next


 #instantiating an object 
fnode = Node("Samuel","Menzgold");
# print(f"{fnode}");
NewNode  = Node("Big","small");

array = ["samuel","menzgold"];
linkedLists =  LinkedList(nodes = ["head","tail"]);

# print(f"{linkedLists.insert_first(NewNode)}");
print(f"{linkedLists.insert_first(fnode)}");
print(f"{linkedLists.insert_last('NewNodeInsertedLast')}");