import tkinter as tk

class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

class Edge:
    def __init__(self, id, start_node, end_node):
        self.id = id
        self.start_node = start_node
        self.end_node = end_node

class GraphEditor:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.current_start_node = None

        self.root = tk.Tk()
        self.root.title("Node Graph Editor")

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.add_node_btn = tk.Button(
            self.root, text="Add Node", command=self.add_node
        )
        self.add_node_btn.pack(side=tk.LEFT)

        self.add_edge_btn = tk.Button(
            self.root, text="Add Edge", command=self.start_adding_edge
        )
        self.add_edge_btn.pack(side=tk.LEFT)

        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def add_node(self):
        node_id = len(self.nodes) + 1
        x = self.canvas.canvasx(self.canvas.winfo_pointerx())
        y = self.canvas.canvasy(self.canvas.winfo_pointery())
        node = Node(node_id, x, y)
        self.nodes.append(node)
        self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="red")
        self.canvas.create_text(x, y, text=str(node_id))

    def start_adding_edge(self):
        self.current_start_node = None

    def add_edge(self, start_node_id, end_node_id):
        start_node = self.get_node_by_id(start_node_id)
        end_node = self.get_node_by_id(end_node_id)
        if start_node and end_node:
            edge_id = len(self.edges) + 1
            edge = Edge(edge_id, start_node, end_node)
            self.edges.append(edge)
            self.canvas.create_line(
                start_node.x, start_node.y, end_node.x, end_node.y, fill="black"
            )

    def get_node_by_id(self, node_id):
        for node in self.nodes:
            if node.id == node_id:
                return node
        return None

    def on_canvas_click(self, event):
        if self.current_start_node is None:
            self.current_start_node = self.get_closest_node(event.x, event.y)
        else:
            end_node = self.get_closest_node(event.x, event.y)
            if end_node and end_node != self.current_start_node:
                self.add_edge(self.current_start_node.id, end_node.id)
                self.current_start_node = None

    def get_closest_node(self, x, y):
        closest_node = None
        min_distance = float("inf")
        for node in self.nodes:
            distance = ((x - node.x) ** 2 + (y - node.y) ** 2) ** 0.5
            if distance < min_distance:
                closest_node = node
                min_distance = distance
        return closest_node

    def run(self):
        self.root.mainloop()

# Example usage:
editor = GraphEditor()
editor.run()
