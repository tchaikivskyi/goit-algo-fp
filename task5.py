import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import matplotlib.colors as mcolors

class Node:
    def __init__(self, key, color="#D3D3D3"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_size=10)
    plt.show()

def generate_gradient_colors(n, base_color="#1296F0"):
    # Генерує кольори від темного до світлого
    base_rgb = mcolors.hex2color(base_color)
    colors = []
    for i in range(n):
        factor = 0.3 + 0.7 * (i / (n - 1))
        color = tuple(min(1, c * factor + 1 * (1 - factor)) for c in base_rgb)
        colors.append(mcolors.rgb2hex(color))
    return colors

def bfs(root):
    queue = deque([root])
    visited = []
    while queue:
        node = queue.popleft()
        if node:
            visited.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return visited

def dfs(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if node:
            visited.append(node)
            stack.append(node.right)  
            stack.append(node.left)
    return visited

def visualize_traversal(root, traversal_type="bfs"):
    if traversal_type == "bfs":
        visited_nodes = bfs(root)
    elif traversal_type == "dfs":
        visited_nodes = dfs(root)
    else:
        raise ValueError("Unknown traversal type")

    colors = generate_gradient_colors(len(visited_nodes))
    for node, color in zip(visited_nodes, colors):
        node.color = color
        draw_tree(root)  


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

print("BFS:")
visualize_traversal(root, traversal_type="bfs")

root2 = Node(0)
root2.left = Node(4)
root2.left.left = Node(5)
root2.left.right = Node(10)
root2.right = Node(1)
root2.right.left = Node(3)

print("DFS:")
visualize_traversal(root2, traversal_type="dfs")
