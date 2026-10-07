# Token class
# Stores the lexeme and its token type

class Token:

    def __init__(self, lexeme, token_type):
        self.lexeme = lexeme
        self.token_type = token_type

    def display(self):
        print(self.lexeme, "->", self.token_type)