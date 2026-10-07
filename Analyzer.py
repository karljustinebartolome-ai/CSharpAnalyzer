# Analyzer class
# Combines lexical and validation processes

from Lexer import Lexer
from Validator import Validator


class Analyzer:

    def __init__(self):

        self.lexer = Lexer()
        self.validator = Validator()

    def analyze(self, text):

        # Get lexemes and tokens
        tokens = self.lexer.analyze(text)

        # Check for errors
        errors = self.validator.validate(tokens)

        return tokens, errors