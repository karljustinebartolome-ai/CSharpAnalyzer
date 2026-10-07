# Validator class
# Checks syntax and semantic errors

class Validator:

    def validate(self, tokens):

        errors = []

        # Check if input is empty
        if len(tokens) == 0:
            errors.append("Input cannot be empty.")
            return errors

        # Check for semicolon
        if tokens[-1].token_type != "SEMICOLON":
            errors.append("Syntax error: Missing semicolon (;).")

        # Check data type
        if tokens[0].token_type != "DATA_TYPE":
            errors.append("Syntax error: Missing or invalid data type.")

        # Check identifier
        if len(tokens) > 1:

            if tokens[1].token_type != "IDENTIFIER":
                errors.append(
                    "Syntax error: Invalid identifier."
                )

        # Check assignment
        if len(tokens) > 2:

            if tokens[2].token_type != "ASSIGNMENT_OPERATOR":
                errors.append(
                    "Syntax error: Expected '=' after identifier."
                )

        # Check value
        if len(tokens) > 3:

            value = tokens[3]

            if value.token_type == "UNKNOWN":
                errors.append(
                    "Syntax error: Invalid value."
                )

        # Check data type and value compatibility
        if len(tokens) > 3:

            data_type = tokens[0].lexeme
            value_type = tokens[3].token_type

            if data_type == "int":
                if value_type != "INTEGER":
                    errors.append(
                        "Semantic error: int requires an integer value."
                    )

            elif data_type == "float" or data_type == "double":
                if value_type != "INTEGER" and value_type != "DECIMAL":
                    errors.append(
                        "Semantic error: Numeric data type requires a number."
                    )

            elif data_type == "string":
                if value_type != "STRING":
                    errors.append(
                        "Semantic error: string requires a string value."
                    )

            elif data_type == "char":
                if value_type != "CHARACTER":
                    errors.append(
                        "Semantic error: char requires a character value."
                    )

            elif data_type == "bool":
                if value_type != "BOOLEAN":
                    errors.append(
                        "Semantic error: bool requires true or false."
                    )

        return errors