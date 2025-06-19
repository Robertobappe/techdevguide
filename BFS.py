from typing import Any, Optional
from queue import Queue 

class BinaryTree:
    def __init__(self, value: Any):
        self.value = value
        self.left_child: Optional['BinaryTree'] = None
        self.right_child: Optional['BinaryTree'] = None
    
    def insert_left(self, value: Any):
        # Correção: Usar 'is None'
        if self.left_child is None: 
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value: Any):
        # Correção: Usar 'is None'
        if self.right_child is None: 
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def bfs(self) -> None:
        q = Queue() 
        q.put(self)

        while not q.empty():
            current_node = q.get() # Remove o primeiro nó da fila
            print(current_node.value, end=" ") # Processa o nó (imprime o valor)

            # Adiciona os filhos do nó atual à fila
            if current_node.left_child:
                q.put(current_node.left_child)
            if current_node.right_child:
                q.put(current_node.right_child)
    
    # Método auxiliar para visualizar a árvore (útil para verificar a construção)
    def print_tree_structure(self, level: int = 0, prefix: str = "Root: "):
        """Imprime a estrutura da árvore com indentação."""
        # Correção: Usar 'is not None'
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


# --- BLOCO DE TESTE ---
# 1. Crie a raiz da árvore
root = BinaryTree(1)

# 2. Construa a árvore específica (1-2-3-4-5-6-7) usando os métodos insert
root.insert_left(2)
root.insert_right(5)

node_2 = root.left_child
node_5 = root.right_child

if node_2:
    node_2.insert_left(3)
    node_2.insert_right(4)

if node_5:
    node_5.insert_left(6)
    node_5.insert_right(7)

# Opcional: Visualize a estrutura da árvore para confirmar que foi construída corretamente
print("--- Estrutura da Árvore Construída ---")
root.print_tree_structure()

# 6. Teste o método bfs (NOVO TESTE!)
print("\n--- Testando a Travessia BFS (Breadth-First Search) ---")
print("Ordem BFS (Nível por Nível):")
root.bfs()
print()
# Saída esperada para BFS da árvore 1-2-3-4-5-6-7: 1 2 5 3 4 6 7