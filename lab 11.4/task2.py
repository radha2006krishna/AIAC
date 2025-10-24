import timeit
from collections import deque
# -------------------------------
# Queue Implementation Using List
# -------------------------------
class ListQueue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.items.append(item)
    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if not self.is_empty():
            return self.items.pop(0)  # O(n)
        raise IndexError("Dequeue from an empty queue")
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0
# -----------------------------------
# Optimized Queue Using collections.deque
# -----------------------------------
class DequeQueue:
    def __init__(self):
        self.items = deque()
    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.items.append(item)  # O(1)
    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if not self.is_empty():
            return self.items.popleft()  # O(1)
        raise IndexError("Dequeue from an empty queue")
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0
# -------------------------------
# Performance Comparison
# -------------------------------
def benchmark(queue_class, n=10000):
    """Benchmark enqueue and dequeue performance."""
    q = queue_class()
    # Enqueue n items
    for i in range(n):
        q.enqueue(i)
    # Dequeue n items
    for _ in range(n):
        q.dequeue()
if __name__ == "__main__":
    n = 10000  # Number of operations to test
    # Measure ListQueue time
    list_time = timeit.timeit(lambda: benchmark(ListQueue, n), number=1)
    # Measure DequeQueue time
    deque_time = timeit.timeit(lambda: benchmark(DequeQueue, n), number=1)
    print("=== Queue Performance Comparison ===")
    print(f"Operations tested: {n} enqueues + {n} dequeues\n")
    print(f"ListQueue time : {list_time:.6f} seconds")
    print(f"DequeQueue time: {deque_time:.6f} seconds")
    if list_time > deque_time:
        print("\n✅ deque-based queue is significantly faster!")
    else:
        print("\n⚠️ list-based queue performed unexpectedly better (check system noise).")