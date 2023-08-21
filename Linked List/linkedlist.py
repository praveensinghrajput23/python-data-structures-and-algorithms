class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        # create a empty linked list means there is nothing 0 nodes
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def __str__(self):
        pass


L = LinkedList()
print(L)
print(len(L))
