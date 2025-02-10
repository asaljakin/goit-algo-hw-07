class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []  # Список відповідей
        self.is_deleted = False

    def add_reply(self, reply):
        """
        Додає відповідь до коментаря.
        """
        self.replies.append(reply)

    def remove_reply(self):
        """
        Видаляє коментар, замінюючи текст на стандартне повідомлення.
        """
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        """
        Рекурсивно виводить коментар та всі його відповіді.
        """
        indent = "    " * level  # Відступ для ієрархії
        if self.is_deleted:
            print(f"{indent}{self.author}: {self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(level + 1)  # Рекурсивний вивід відповідей