class Node:
    def __init__(self, _data, _next=None):
        self.data = _data
        self.next = _next


class LinkedList:
    def __init__(self, _items=[]):
        self.head = None
        self.tail = None
        self.count = 0

        for item in _items:
            self.append(item)

    def append(self, _data):
        new_node = Node(_data)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def insert(self, _data, pos):
        new_node = Node(_data)
        if pos <= 0:
            new_node.next = self.head
            self.head = new_node
        elif pos >= self.count:
            self.tail_next = new_node
            self.tail = new_node
        else:
            tmp = self.head
            for _ in range(pos-1):
                tmp = tmp.next
            new_node.next = tmp.next
            tmp.next = new_node
            
            
    def pop(self, pos=None):
        
        if pos == None:
            tmp = self.head
            for _ in range(self.count-2):
                tmp = tmp.next
            tmp1 = tmp.next
            self.tail = tmp
            tmp.next = None
        elif 0 < pos < self.count:
            tmp = self.head
            for _ in range(pos-1):
                tmp = tmp.next
            tmp1 = tmp.next
            tmp.next = tmp1.next
        elif pos <= 0:
            tmp = self.head
            tmp1 = self.head
            self.head = tmp1.next
            tmp.next = tmp1.next
        else:
            tmp = self.head
            for _ in range(self.count-2):
                tmp = tmp.next
            tmp1 = tmp.next
            self.tail = tmp
            tmp.next = None
        data = tmp1.data
        del tmp1
        self.count -= 1
        return data

    def remove(self, _data):
        tmp0 = self.head
        tmp = self.head
        pos = 0
        is_data_exist = False
        for _ in range(self.count):
            if tmp0.data == _data:
                is_data_exist = True
                break
            tmp0 = tmp0.next
            pos += 1

        for _ in range(pos - 1):
            tmp = tmp.next
        if is_data_exist:
            if pos == 0:
                tmp1 = self.head
                self.head = tmp1.next
                tmp.next = tmp1.next
                del tmp1
                self.count -= 1
            elif 0 < pos < self.count:
                tmp1 = tmp.next
                tmp.next= tmp1.next
                del tmp1
                self.count -= 1
            else:
                tmp1 = tmp
                self.tail = tmp
                tmp.next = None
                del tmp1
                self.count -= 1

            
        return

            
    def __str__(self):
        _head = self.head
        s = "head -> "

        while _head:
            s += str(_head.data) + " -> "
            _head = _head.next

        s += "None"
        return s

    def __repr__(self):
        _head = self.head
        l = []
        while _head:
            l.append(str(_head.data))
            _head = _head.next

        return "LinkedList({})".format([', '.join(l)])


if __name__ == '__main__':
    ll = LinkedList([5, 6, 2, 4, 8, 1, 9])
    # ll.pop()
    # ll.pop(4)
    ll.remove(5)
    print(ll)