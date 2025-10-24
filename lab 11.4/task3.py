class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # pointer to the next node (None when there is no next)
class LinkedList:
    def __init__(self):
        self.head = None  # head pointer: points to the first node or None if list is empty
    def insert_at_end(self, value):
        new_node = Node(value)
        # If the list is empty, set head to the new node.
        if self.head is None:
            # Pointer update: head now points to new_node.
            # Before: head = None
            # After:  head -> new_node
            self.head = new_node
            return
        # Otherwise, find the last node (node whose next is None)
        current = self.head
        while current.next is not None:
            current = current.next
        # current is now the last node. Update its next pointer to the new node.
        # Pointer update: current.next (previously None) -> new_node
        # This links the new_node into the list at the end.
        current.next = new_node
        # new_node.next remains None, marking it as the new tail.
    def delete_value(self, value):
        if self.head is None:
            # List empty, nothing to delete.
            return False
        # Special case: the head node contains the value.
        if self.head.value == value:
            # Pointer update: move head to the next node.
            # Before: head -> node_to_delete -> ...
            # After:  head -> node_to_delete.next
            # node_to_delete becomes unreachable from the list and will be garbage-collected.
            self.head = self.head.next
            return True
        # General case: track previous and current to remove current when found.
        prev = self.head
        current = self.head.next
        while current is not None:
            if current.value == value:
                # Pointer update: bypass current by linking prev.next to current.next.
                # Before: prev -> current -> current.next
                # After:  prev -> current.next
                # current is removed from the chain and becomes unreachable.
                prev.next = current.next
                return True
            # Advance both pointers: prev follows current, current moves forward.
            prev = current
            current = current.next
        # Value not found
        return False
    def traverse(self):
        """Return a list of node values from head to tail."""
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next  # move to next node
        return values
    def __repr__(self):
        return "LinkedList(" + "->".join(str(v) for v in self.traverse()) + ")"
if __name__ == "__main__":
    # Demonstration and basic checks
    ll = LinkedList()
    # Insert into empty list
    ll.insert_at_end(10)   # head was None -> head now points to Node(10)
    print("After inserting 10:", ll)
    # Insert more elements
    ll.insert_at_end(20)   # last_node.next (Node(10).next) -> Node(20)
    ll.insert_at_end(30)   # last_node.next (Node(20).next) -> Node(30)
    print("After inserting 20, 30:", ll)
    # Traverse returns list of values
    print("Traverse:", ll.traverse())
    # Delete middle value
    deleted = ll.delete_value(20)  # prev (Node(10)).next bypasses Node(20) -> Node(30)
    print("Deleted 20:", deleted, "Result:", ll)
    # Delete head
    deleted = ll.delete_value(10)  # head moves from Node(10) -> Node(30)
    print("Deleted 10 (head):", deleted, "Result:", ll)
    # Delete tail
    deleted = ll.delete_value(30)  # prev.next (if prev is Node before tail) -> None
    print("Deleted 30 (tail):", deleted, "Result:", ll)
    # Delete from empty (after removing last element)
    deleted = ll.delete_value(99)  # nothing to delete
    print("Attempt to delete from empty:", deleted, "Result:", ll)
    # Insert duplicates and delete first occurrence
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(1)
    print("Before deleting first '1':", ll)
    ll.delete_value(1)  # removes the first 1
    print("After deleting first '1':", ll)