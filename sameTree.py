from typing import Any, Optional

class BinaryTree:
    def __init__(self, value: Any):
        self.value = value
        self.left_child: Optional['BinaryTree'] = None
        self.right_child: Optional['BinaryTree'] = None
    
    def insert_left(self, value: Any):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value: Any):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node
    
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

# --- FUNÇÃO PARA COMPARAR DUAS ÁRVORES ---
class Solution:
    def compare_trees(self, tree1: Optional[BinaryTree], tree2: Optional[BinaryTree]) -> bool:
        # Caso base 1: Ambos os nós são None (chegou ao fim de um caminho em ambas)
        if tree1 is None and tree2 is None:
            return True    
        # Caso base 2: Um nó é None e o outro não (estrutura diferente)
        if tree1 is None or tree2 is None:
            return False        
        # Caso recursivo: Ambos os nós existem
        # Verifica se os valores são iguais E se os filhos esquerdos são iguais E se os filhos direitos são iguais
        sol = Solution()
        return (tree1.value == tree2.value and
                sol.compare_trees(tree1.left_child, tree2.left_child) and
                sol.compare_trees(tree1.right_child, tree2.right_child))


# --- BLOCO DE TESTE COM OS CASOS FORNECIDOS ---

print("--- Testando Comparações de Árvores com Casos Específicos ---")

# Caso de Teste 1: p = [1,2,3], q = [1,2,3] -> Output: true
# Árvore p:
#    1
#   / \
#  2   3
p1 = BinaryTree(1)
p1.insert_left(2)
p1.insert_right(3)

# Árvore q:
#    1
#   / \
#  2   3
q1 = BinaryTree(1)
q1.insert_left(2)
q1.insert_right(3)

print("\n--- Caso 1: p = [1,2,3], q = [1,2,3] ---")
print("Estrutura de P1:")
p1.print_tree_structure()
print("\nEstrutura de Q1:")
q1.print_tree_structure()
sol1 = Solution()
result1 = sol1.compare_trees(p1, q1)
print(f"Resultado: {result1}")
print(f"Esperado: True")
print("-" * 40)


# Caso de Teste 2: p = [1,2], q = [1,null,2] -> Output: false
# Árvore p:
#    1
#   /
#  2
p2 = BinaryTree(1)
p2.insert_left(2)

# Árvore q:
#    1
#     \
#      2
q2 = BinaryTree(1)
q2.insert_right(2) # Importante: usar insert_right aqui para corresponder a "null" na esquerda

print("\n--- Caso 2: p = [1,2], q = [1,null,2] ---")
print("Estrutura de P2:")
p2.print_tree_structure()
print("\nEstrutura de Q2:")
q2.print_tree_structure()
sol2 = Solution()
result2 = sol2.compare_trees(p2, q2)
print(f"Resultado: {result2}")
print(f"Esperado: False")
print("-" * 40)


# Caso de Teste 3: p = [1,2,1], q = [1,1,2] -> Output: false
# Árvore p:
#    1
#   / \
#  2   1
p3 = BinaryTree(1)
p3.insert_left(2)
p3.insert_right(1)

# Árvore q:
#    1
#   / \
#  1   2
q3 = BinaryTree(1)
q3.insert_left(1) # Valor diferente no filho esquerdo
q3.insert_right(2) # Valor diferente no filho direito

print("\n--- Caso 3: p = [1,2,1], q = [1,1,2] ---")
print("Estrutura de P3:")
p3.print_tree_structure()
print("\nEstrutura de Q3:")
q3.print_tree_structure()
sol3= Solution()
result3 = sol3.compare_trees(p3, q3)
print(f"Resultado: {result3}")
print(f"Esperado: False")
print("-" * 40)