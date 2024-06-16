import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


# Клас дерева
class Node:
    def __init__(self, key, color="#808080"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


# Функція для побудови бінарної купи з масиву
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


# Функція для відображення дерева на екрані
def draw_tree(tree_root, traversal_type, step):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Значення вузла для міток

    plt.figure(figsize=(8, 5))
    plt.title(f"Обхід {traversal_type} - Крок {step}")
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2000, node_color=colors)
    plt.show()


# Зміна кольору вузла
def get_color(step, total_steps):
    intensity = int(255 * step / total_steps)
    return f"#0000{intensity:02x}"


# Функція для обходу дерева в ширину
def bfs(rut):
    name = bfs.__name__.upper()
    queue = deque([rut])
    visited = []
    steps = 0
    total_steps = count_nodes(rut)
    rut.color = get_color(steps, total_steps)
    steps += 1

    while queue:
        node = queue.popleft()
        node.color = "#FF0000"
        draw_tree(rut, name, steps)
        node.color = get_color(steps, total_steps)
        visited.append(node)
        steps += 1

        draw_tree(rut, name, steps)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Функція для обходу дерева в глибину
def dfs(rut):
    name = dfs.__name__.upper()
    stack = [rut]
    visited = []
    steps = 0
    total_steps = count_nodes(rut)
    rut.color = get_color(steps, total_steps)
    steps += 1

    while stack:
        node = stack.pop()
        node.color = "#FF0000"
        draw_tree(rut, name, steps)
        node.color = get_color(steps, total_steps)
        visited.append(node)
        steps += 1

        draw_tree(rut, name, steps)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# Функція для обчислення кількості вузлів в дереві
def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення обходу в ширину (BFS)
print("BFS обхід:")
bfs(root)

# Потрібно очистити кольори перед другим обходом
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення обходу в глибину (DFS)
print("DFS обхід:")
dfs(root)
