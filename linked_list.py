import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.curr = None
        self.length = 0
 
    def append(self, data):
        item = Node(data)
        if self.head is None:
            self.head = self.tail = item
            self.length += 1
            return

        item.prev = self.tail
        self.tail.next = item
        self.tail = item
        self.length += 1

    def again(self):
        if self.curr.prev is not None:
            self.curr = self.curr.prev

    def __reversed__(self):
        node = self.tail
        while node is not None:
            yield node.data
            node = node.prev

    def __len__(self):
        return self.length

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr is None:
            self.curr = self.head
            return self.curr.data
        elif self.curr.next is not None:
            self.curr = self.curr.next
            return self.curr.data
        self.curr = None
        raise StopIteration


ll = LinkedList()
for i in range(0, 15):
    ll.append(i)

for i in ll:
    print(i)
print("rev")
for i in range(15, 20):
    ll.append(i)
for i in reversed(ll):
    print(i)

print(len(ll))
