
#################################################################################################

# Problem Statement:

'''
Implement Depth First Search (DFS) Algorithm and Breadth First Search (BFS) Algorithm,
Use an undirected graph or tree and develop a recursive algorithm for searching all the vertices
of that graph or tree data structure.
'''

#################################################################################################

# Solution for N-ary Tree:

# Tree Node
class Node:
    def __init__(self, key):
        self.key = key
        self.children = []

# Recursive DFS
def dfs_recursive(node, result):
    if node is None:
        return
    result.append(node.key)
    for child in node.children:
        dfs_recursive(child, result)

# Non-Recursive DFS
def dfs_non_recursive(root):
    if root is None:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.key)
        # Add children in reverse so leftmost is processed first
        for child in reversed(node.children):
            stack.append(child)
    return result

# Recursive BFS
def bfs_recursive(queue, result):
    if not queue:
        return
    next_queue = []
    for node in queue:
        result.append(node.key)
        next_queue.extend(node.children)
    bfs_recursive(next_queue, result)

# Non-Recursive BFS
def bfs_non_recursive(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.key)
        queue.extend(node.children)
    return result

# Driver-Code
def driver():
    # Create a sample N-ary tree
    root = Node(1)
    child2 = Node(2)
    child3 = Node(3)
    child4 = Node(4)
    root.children = [child2, child3, child4]

    child5 = Node(5)
    child6 = Node(6)
    child2.children = [child5, child6]

    child7 = Node(7)
    child3.children = [child7]

    child8 = Node(8)
    child9 = Node(9)
    child4.children = [child8, child9]

    dfs_result = []
    dfs_recursive(root, dfs_result)
    print("\nRecursive DFS Traversal:          ", dfs_result)

    print("\nNon-Recursive DFS Traversal:      ", dfs_non_recursive(root))

    bfs_result = []
    bfs_recursive([root], bfs_result)
    print("\nRecursive BFS Traversal:          ", bfs_result)

    print("\nNon-Recursive BFS Traversal:      ", bfs_non_recursive(root), "\n")

# Call to Driver Function
if __name__ == "__main__":
    driver()

#################################################################################################
