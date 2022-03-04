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

    def remove(self, item):
        node = self.head
        while node is not None:
            if node.data == item:
                if not node.prev:
                    self.head = node.next
                    if node.next:
                        node.next.prev = None
                elif not node.next:
                    node.prev.next = None;
                    self.tail = node.prev
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                del(node)
                self.length -= 1
                return
            node = node.next

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
for i in range(0, 16):
    ll.append("item{}" . format(i))

for i in ll:
    print(i)
print()

ll.remove("item14")
ll.remove("item0")
ll.remove("item3")
for i in ll:
    print(i)

print("again\n")

for i in reversed(ll):
    print(i)
print("again\n")

for i in ll:
    print(i)

print(len(ll))

for i in ll:
    ll.remove(i)

print(len(ll))
for i in range(0, 16):
    ll.append("list{}" . format(i))
for i in ll:
    print(i)
