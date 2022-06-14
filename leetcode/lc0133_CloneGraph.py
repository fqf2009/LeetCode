# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) 
# of its neighbors.
#   class Node {
#       public int val;
#       public List<Node> neighbors;
#   }
# Test case format:
# For simplicity, each node's value is the same as the node's index (1-indexed). 
# For example, the first node with val == 1, the second node with val == 2, and 
# so on. The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a 
# finite graph. Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. You must return 
# the copy of the given node as a reference to the cloned graph.

# Constraints:
#   The number of nodes in the graph is in the range [0, 100].
#   1 <= Node.val <= 100
#   Node.val is unique for each node.
#   There are no repeated edges and no self-loops in the graph.
#   The Graph is connected and all nodes can be visited starting from the given node.
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    @staticmethod
    def from_adjacency_list(adj_list: list[list[int]]) -> 'Node':
        nodes = [Node(v) for v in range(len(adj_list)+1)]   # waste one: Node(0)
        for i, adj_values in enumerate(adj_list):
            node = nodes[i+1]
            node.neighbors = [nodes[v] for v in adj_values]
        return nodes[1]

    @staticmethod
    def to_adjacency_list(node: 'Node') -> list[list[int]]:
        res = []
        def dfs_visit(node):
            if len(res) < node.val:
                res.extend([[] for _ in range(node.val - len(res))])
            if len(res[node.val-1]) == 0:
                edges = res[node.val-1]
                for n1 in node.neighbors:
                    edges.append(n1.val)
                    dfs_visit(n1)
        
        dfs_visit(node)
        return res

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        clone_nodes = {}

        def dfs_clone(node: Node) -> Node:
            if node.val in clone_nodes:
                return clone_nodes[node.val]
            else:
                clone = Node(node.val, [])
                clone_nodes[node.val] = clone
                for n1 in node.neighbors:
                    clone.neighbors.append(dfs_clone(n1))
                return clone

        return dfs_clone(node)


# practice
class Solution1:
    def cloneGraph(self, node: 'Node') -> 'Node':
        map = {}
        def dfsClone(node: Node) -> Node:
            if not node: return node
            if node.val in map: return map[node.val]
            n1 = Node(node.val)
            map[node.val] = n1
            if node.neighbors:
                n1.neighbors = []
                for n2 in node.neighbors:
                    n1.neighbors.append(dfsClone(n2))
            return n1
        
        return dfsClone(node)


if __name__ == '__main__':
    def unit_test(sol):
        adj_list1 = [[2,4],[1,3],[2,4],[1,3]]
        node1 = Node.from_adjacency_list(adj_list1)
        node2 = sol.cloneGraph(node1)
        assert id(node1) != id(node2)
        adj_list2 = Node.to_adjacency_list(node2)
        print(adj_list2)
        assert adj_list1 == adj_list2

        adj_list1 = [[]]
        node1 = Node.from_adjacency_list(adj_list1)
        node2 = sol.cloneGraph(node1)
        assert id(node1) != id(node2)
        adj_list2 = Node.to_adjacency_list(node2)
        print(adj_list2)
        assert adj_list1 == adj_list2

        node2 = sol.cloneGraph(None)
        print(node2)
        assert node2 is None

    unit_test(Solution())
    unit_test(Solution1())
