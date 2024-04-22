import heapq


# made by ChatGPT!
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """Insert the element"""
        # Use (priority, index, item) tuple directly without negating priority
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        """Get the element"""
        # Pop the item with the smallest priority value (min-heap behavior)
        return heapq.heappop(self._queue)[-1]

    def __str__(self):
        items = [item[-1] for item in self._queue]  # Extract items from the heap
        return f'PriorityQueue: {items}'

    def is_empty(self):
        return len(self.queue) == 0

    @property
    def queue(self):
        return self._queue


if __name__ == '__main__':
    myQueue = PriorityQueue()
    print(myQueue)
    myQueue.push(12, 12)
    print(myQueue)
    myQueue.push(1, 1)
    print(myQueue)
    myQueue.push(14, 14)
    print(myQueue)
    myQueue.push(7, 7)
    print(myQueue) # Output: PriorityQueue: [1, 7, 14, 12]

    while myQueue.queue:  # Pop all items from the queue
        print(myQueue.pop())
