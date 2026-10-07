# Main program

from Analyzer import Analyzer


print("C# VARIABLE DECLARATION ANALYZER")
print("--------------------------------")

# Create Analyzer object
analyzer = Analyzer()

# Ask for C# input
text = input("Enter C# declaration or initialization: ")

# Analyze the input
tokens, errors = analyzer.analyze(text)


print("\nLEXEMES AND TOKENS")
print("------------------")

for token in tokens:
    token.display()


print("\nVALIDATION RESULT")
print("-----------------")

# Check if there are errors
if len(errors) == 0:

    print("Status: VALID")
    print("No errors detected.")

else:

    print("Status: INVALID")
    print("\nERRORS:")

    for error in errors:
        print("-", error)