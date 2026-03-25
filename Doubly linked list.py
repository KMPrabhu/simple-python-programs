class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = DNode(data)
        if not self.head:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
        new.prev = temp

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


dll = DoublyLL()
dll.insert(10)
dll.insert(20)
dll.insert(30)
dll.display()
