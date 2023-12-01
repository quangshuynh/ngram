"""
141 Tree Lab - Derp the Interpreter

The Derp interpreter parses and evaluates prefix integer expressions 
containing basic arithmetic operators (*,//,-,+). It performs arithmetic with
integer operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, prints the infix expression with 
parentheses to denote order of operation, and evaluates the expression to
print the result.

Author: CS@RIT.EDU

file: derp.py
language: python3
Author: Quang Huynh
"""

from derp_types import *  # dataclasses for the Derp interpreter


def read_symbol_table(filename):
    """
    Opens and reads a symbol table for variables from a file
    :param filename: Path to file containing symbol table
    :return: Dictionary representing the symbol table
    :raises FileNotFoundError: If inputted file not found
    :raises ValueError: If there is an issue with file format or variable values
    """
    symbol_table = {}  # Initialize dictionary for variables & values
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.split()
                if len(parts) == 2:
                    variable, value = parts  # Dictionary key & value
                    try:
                        value = int(value)
                        symbol_table[variable] = value
                    except ValueError:
                        raise ValueError("Invalid value for variable: " + variable + ": " + value)
                else:
                    raise ValueError("Invalid line format: " + line)
    except FileNotFoundError:
        raise FileNotFoundError("File not found: " + filename)
    return symbol_table


##############################################################################
# parse
############################################################################## 

def parse(tokens):
    """parse: list(String) -> Node
    From a prefix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    precondition: tokens is a non-empty list of strings
    :param tokens: List of strings
    :return: Left, root & right nodes of an expression tree
    :raises ValueError: If invalid token is encountered during parsing
    """
    token = tokens.pop(0)  # Pop first token from list
    if token.isdigit() or (token == "-" and token[:1].isdigit()):  # Check if token is digit or a negative
        return LiteralNode(token)  # Numbers
    elif token.isidentifier():  # Check if token is a letter
        return VariableNode(token)  # Variables
    elif token in ("+", "-", "*", "//"):  # Check if token is a mathematical operator
        left = parse(tokens)  # Left string
        right = parse(tokens)  # Right string
        return MathNode(left, token, right)
    else:
        raise ValueError("Invalid token: " + token)


##############################################################################
# infix
##############################################################################

def infix(node):
    """infix: Node -> String 
    Perform an inorder traversal of the node and return a string that
    represents the infix expression.
    precondition: node is a valid derp tree node
    :param node: Nodes of the DERP tree
    :return: A string representing infix expression
    :raises ValueError: If invalid node type is encountered
    """
    if isinstance(node, LiteralNode):  # Values
        return str(node.val)
    elif isinstance(node, VariableNode):  # Variables
        return node.name
    elif isinstance(node, MathNode):  # Recursive call
        left = infix(node.left)  # Left string
        right = infix(node.right)  # Right string
        return str("(" + left + " " + node.operator + " " + right + ")")
    else:
        raise ValueError("Invalid node type: " + str(type(node)))


##############################################################################
# evaluate
##############################################################################    

def evaluate(node, sym_tbl):
    """evaluate: Node * dict(key=String, value=int) -> int 
    Return the result of evaluating the expression represented by node.
    Precondition: all variable names must exist in sym_tbl
    precondition: node is a valid derp tree node
    :param node: Nodes of the DERP tree
    :param sym_tbl: Dictionary containing variables and corresponding values
    :return: Result of expression evaluation
    :raises ValueError: If there are issues with variables, operators, or division by zero
    """
    if isinstance(node, LiteralNode):  # Values
        return int(node.val)
    elif isinstance(node, VariableNode):  # Variables
        if node.name in sym_tbl:
            return sym_tbl[node.name]
        else:
            raise ValueError("Undefined variable: " + node.name)
    elif isinstance(node, MathNode):
        left = evaluate(node.left, sym_tbl)
        right = evaluate(node.right, sym_tbl)
        if node.operator == '+':  # Addition
            return left + right
        elif node.operator == '-':  # Subtraction
            return left - right
        elif node.operator == '*':  # Multiplication
            return left * right
        elif node.operator == '//':  # Division
            if right != 0:
                return left // right
            else:
                raise ValueError("Division by zero")
        else:
            raise ValueError("Invalid operator: " + node.operator)
    else:
        raise ValueError("Invalid node type: " + str(type(node)))


##############################################################################
# main
##############################################################################

def main():
    """main: None -> None
    The main program prompts for the symbol table file, and a prefix 
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression"""

    print("Hello Herp, welcome to Derp v1.0 :)")

    in_file = input("Herp, enter symbol table file: ")

    # STUDENT: CONSTRUCT AND DISPLAY THE SYMBOL TABLE HERE
    symbol_table = read_symbol_table(in_file)
    print("\nDerping the symbol table (variable name => integer value)...")
    for variable, value in symbol_table.items():
        print(variable + " => " + str(value))
    print("")

    print("Herp, enter prefix expressions, e.g.: + 10 20 (ENTER to quit)...")

    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefix_exp = input("derp> ")
        if prefix_exp == "":
            break

        # STUDENT: GENERATE A LIST OF TOKENS FROM THE PREFIX EXPRESSION
        tokens_list = prefix_exp.split()

        # STUDENT: CALL parse WITH THE LIST OF TOKENS AND SAVE THE ROOT OF 
        # THE PARSE TREE.
        parse_tree = parse(tokens_list)

        # STUDENT: GENERATE THE INFIX EXPRESSION BY CALLING infix AND SAVING
        # THE STRING.
        infix_expression = infix(parse_tree)

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.    
        print("Derping the infix expression: " + infix_expression)

        # STUDENT: EVALUATE THE PARSE TREE BY CALLING evaluate AND SAVING THE
        # INTEGER RESULT.
        evaluation = evaluate(parse_tree, symbol_table)

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.
        print("Derping the evaluation: " + str(evaluation) + "\n")

    print("Goodbye Herp :(")


if __name__ == "__main__":
    main()
