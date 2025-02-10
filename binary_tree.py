class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_max_value(root):
    """
    Знаходить найбільше значення в двійковому дереві пошуку.
    """
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.value


def find_min_value(root):
    """
    Знаходить найменше значення в двійковому дереві пошуку.
    """
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.value


def sum_of_values(root):
    """
    Знаходить суму всіх значень у двійковому дереві пошуку.
    """
    if root is None:
        return 0
    return root.value + sum_of_values(root.left) + sum_of_values(root.right)