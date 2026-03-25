class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data, priority):
        self.queue.append((priority, data))
        self.queue.sort()

    def dequeue(self):
        if self.queue:
            print(self.queue.pop(0)[1])
        else:
            print("Empty")

    def display(self):
        print(self.queue)


pq = PriorityQueue()
pq.enqueue("A", 2)
pq.enqueue("B", 1)
pq.enqueue("C", 3)
pq.display()
pq.dequeue()
