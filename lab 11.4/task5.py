from collections import deque
from typing import Dict, List, Set, Any
# File: /c:/Users/SANGEM RADHA KRISHNA/Desktop/ai coding/lab 11.4/task5.py
class Graph:
    def __init__(self):
        # adjacency list: node -> list of neighbor nodes
        self.adj: Dict[Any, List[Any]] = {}
    def add_edge(self, u, v, directed: bool = False):
        # add edge u -> v (and v -> u if undirected)
        self.adj.setdefault(u, []).append(v)
        if not directed:
            self.adj.setdefault(v, []).append(u)
    def bfs(self, start) -> List[Any]:
        """
        Breadth-First Search (BFS) traversal from 'start'.
        Returns the nodes in the order they are visited.
        """
        visited: Set[Any] = set()
        order: List[Any] = []
        q = deque()
        # Start by visiting the start node
        visited.add(start)       # mark start as visited
        q.append(start)          # enqueue start
        # AI-generated inline comments explain traversal steps:
        # While queue is not empty, pop from the front (FIFO),
        # record the node, then enqueue all unvisited neighbors.
        while q:
            node = q.popleft()   # dequeue next node to process
            order.append(node)   # visit the node
            # Explore neighbors: enqueue unvisited neighbors and mark them visited
            for nbr in self.adj.get(node, []):
                if nbr not in visited:
                    visited.add(nbr)  # mark as visited when enqueuing to avoid duplicates
                    q.append(nbr)      # enqueue neighbor for later processing
        return order
    def dfs_recursive(self, start) -> List[Any]:
        """
        Depth-First Search (DFS) using recursion.
        Returns the nodes in the order they are visited.
        Recursive DFS follows one branch as deep as possible before backtracking.
        """
        visited: Set[Any] = set()
        order: List[Any] = []
        def dfs(node):
            # mark node as visited upon entry to avoid revisiting
            visited.add(node)
            order.append(node)   # record visitation
            # recursively visit each unvisited neighbor
            for nbr in self.adj.get(node, []):
                if nbr not in visited:
                    dfs(nbr)
            # when this function returns, we've finished exploring node's subtree (backtracking)
        dfs(start)
        return order
    def dfs_iterative(self, start) -> List[Any]:
        """
        Depth-First Search (DFS) using an explicit stack (iterative).
        This simulates the recursion stack using a manual stack (LIFO).
        """
        visited: Set[Any] = set()
        order: List[Any] = []
        stack: List[Any] = [start]  # initialize stack with start
        # While stack not empty, pop the top, visit it if not visited,
        # then push its neighbors. Pushing neighbors in reversed order
        while stack:
            node = stack.pop()   # pop the top of the stack (LIFO)
            if node in visited:
                continue
            visited.add(node)    # mark as visited upon popping
            order.append(node)   # record visitation
            # push neighbors onto stack. Reverse to visit in natural order.
            neighbors = self.adj.get(node, [])
            for nbr in reversed(neighbors):
                if nbr not in visited:
                    stack.append(nbr)  # push neighbor to be visited later
        return order
if __name__ == "__main__":
    # Simple demonstration graph
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")
    g.add_edge("C", "F")
    print("Adjacency list:")
    for node, nbrs in g.adj.items():
        print(f"  {node}: {nbrs}")
    print("\nBFS starting at A:")
    print(g.bfs("A"))             # Expected: level-order traversal
    print("\nDFS (recursive) starting at A:")
    print(g.dfs_recursive("A"))   # Expected: deep-first traversal via recursion
    print("\nDFS (iterative) starting at A:")
    print(g.dfs_iterative("A"))  # Expected: deep-first traversal via stack