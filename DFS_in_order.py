from typing import Any, Optional

class BinaryTree:
    def __init__(self, value: Any):
        self.value = value
        self.left_child: Optional['BinaryTree'] = None
        self.right_child: Optional['BinaryTree'] = None
    
    def insert_left(self, value: Any):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value: Any):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    # MÉTODOS DE TRAVESSIA DFS
    # In-order: Esquerda -> Raiz -> Direita
    def in_order(self) -> None:
        if self.left_child:
            self.left_child.in_order()

        print(self.value, end=" ")

        if self.right_child:
            self.right_child.in_order()
    # The result of the in-order algorithm for this tree example is 3–2–4–1–6–5–7

# Método auxiliar para visualizar a árvore (útil para verificar a construção)
    def print_tree_structure(self, level: int = 0, prefix: str = "Root: "):
        """Imprime a estrutura da árvore com indentação."""
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
# Note que a ordem das inserções importa devido à lógica de "empurrar" os filhos.

# Inserindo os filhos diretos do nó 1

root.insert_left(2)
root.insert_right(5)

# Acessando os filhos para inserir seus próprios filhos

node_2 = root.left_child
node_5 = root.right_child

# Inserindo os filhos do nó 2
if node_2:
    node_2.insert_left(3)
    node_2.insert_right(4)

# Inserindo os filhos do nó 5
if node_5:
    node_5.insert_left(6)
    node_5.insert_right(7)

# Opcional: Visualize a estrutura da árvore para confirmar que foi construída corretamente
print("--- Estrutura da Árvore Construída ---")
root.print_tree_structure()

# 4. Teste o método in_order
print("\n--- Testando a Travessia In-order ---")
print("Ordem In-order (Esquerda, Raiz, Direita):")
root.in_order()
print() # Adiciona uma nova linha para formatar a saída
# Saída esperada para in-order: 3 2 4 1 6 5 7