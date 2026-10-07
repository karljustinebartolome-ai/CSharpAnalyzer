# Lexer class
# Identifies lexemes and tokens

from Token import Token


class Lexer:

    def analyze(self, text):

        tokens = []

        # Remove extra spaces
        text = text.strip()

        # Add spaces around symbols
        text = text.replace("=", " = ")
        text = text.replace(";", " ; ")

        # Separate the input
        parts = text.split()

        for part in parts:

            if part in ["int", "float", "double", "string", "char", "bool"]:
                token_type = "DATA_TYPE"

            elif part == "=":
                token_type = "ASSIGNMENT_OPERATOR"

            elif part == ";":
                token_type = "SEMICOLON"

            elif part.isdigit():
                token_type = "INTEGER"

            elif self.is_decimal(part):
                token_type = "DECIMAL"

            elif self.is_string(part):
                token_type = "STRING"

            elif self.is_character(part):
                token_type = "CHARACTER"

            elif part == "true" or part == "false":
                token_type = "BOOLEAN"

            elif self.is_identifier(part):
                token_type = "IDENTIFIER"

            else:
                token_type = "UNKNOWN"

            tokens.append(Token(part, token_type))

        return tokens

    # Check if the value is a decimal number
    def is_decimal(self, text):

        try:
            float(text)

            if "." in text:
                return True

        except ValueError:
            return False

        return False

    # Check if the value is a string
    def is_string(self, text):

        return len(text) >= 2 and text[0] == '"' and text[-1] == '"'

    # Check if the value is a character
    def is_character(self, text):

        return len(text) >= 3 and text[0] == "'" and text[-1] == "'"

    # Check if it is a valid identifier
    def is_identifier(self, text):

        # First character must be a letter or underscore
        if len(text) == 0:
            return False

        if not (text[0].isalpha() or text[0] == "_"):
            return False

        # Remaining characters can be letters, numbers, or underscore
        for character in text[1:]:

            if not (character.isalnum() or character == "_"):
                return False

        return True