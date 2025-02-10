from binary_tree import TreeNode, find_max_value, find_min_value, sum_of_values
from comment_system import Comment

def test_binary_tree():
    # Створення дерева
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(30)

    # Тестування функцій
    print("Найбільше значення в дереві:", find_max_value(root))
    print("Найменше значення в дереві:", find_min_value(root))
    print("Сума всіх значень у дереві:", sum_of_values(root))


def test_comment_system():
    # Створення коментарів
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    # Видалення відповіді
    reply1.remove_reply()

    # Виведення коментарів
    root_comment.display()


if __name__ == "__main__":
    print("Тестування двійкового дерева:")
    test_binary_tree()

    print("\nТестування системи коментарів:")
    test_comment_system()