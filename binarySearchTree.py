class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)

    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        return value == self.value

    def print_tree_structure(self, level: int = 0, prefix: str = "Root: "):
        if self is not None:
            print("    " * level + prefix + str(self.value))
            if self.left_child:
                self.left_child.print_tree_structure(level + 1, "L-- ")
            else:
                print("    " * (level + 1) + "L-- None")
            if self.right_child:
                self.right_child.print_tree_structure(level + 1, "R-- ")
            else:
                print("    " * (level + 1) + "R-- None")


# --- EXECUTANDO COM SEUS NÚMEROS ---
print("Construindo a Árvore Binária de Busca com os valores: 50, 76, 21, 4, 32, 100, 64, 52\n")

# O primeiro valor se torna a raiz da árvore
numbers = [50, 76, 21, 4, 32, 100, 64, 52]
root = BinarySearchTree(numbers[0])

# Inserir os valores restantes
for i in range(1, len(numbers)):
    root.insert_node(numbers[i])

print("Estrutura da Árvore:")
root.print_tree_structure()
print(root.find_node(52))