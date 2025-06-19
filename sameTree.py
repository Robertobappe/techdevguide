from typing import Optional, Any

class TreeNode:
    def __init__(self, val: Any = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        """Inicializa um nó de uma árvore binária.
        Args:
            val (Any): O valor armazenado no nó. Usamos 'Any' para indicar que pode ser de qualquer tipo.
            left (Optional[TreeNode]): O nó filho esquerdo. É Optional porque pode ser None.
            right (Optional[TreeNode]): O nó filho direito. É Optional porque pode ser None."""
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        """Representação para facilitar a depuração."""
        return f"TreeNode(val={self.val})"