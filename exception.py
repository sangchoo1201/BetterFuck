class NotMatchedWhile(Exception):
    def __init__(self):
        super().__init__("'while' and 'end' is not matched")


class UnknownCommand(Exception):
    def __init__(self):
        super().__init__("Unknown command used")


class UnknownPrefix(Exception):
    def __init__(self):
        super().__init__("Unknown prefix used")
