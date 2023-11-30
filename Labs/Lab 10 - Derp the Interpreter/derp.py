"""
141 Tree Lab - Derp the Interpreter

The Derp interpreter parses and evaluates prefix integer expressions 
containing basic arithmetic operators (*,//,-,+). It performs arithmetic with
integer operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, prints the infix expression with 
parentheses to denote order of operation, and evaluates the expression to
print the result.

Author: CS@RIT.EDU

Author: Quang Huynh
"""

from derp_types import *        # dataclasses for the Derp interpreter


def read_symbol_table(fileName):
    symbol_table = {}
    try:
        with open(fileName, "r") as file:
            for line in file:
                parts = line.split()
                if len(parts) == 2:
                    variable_name, value_str = parts
                    try:
                        value = int(value_str)
                        symbol_table[variable_name] = value
                    except ValueError:
                        raise ValueError("Invalid value for variable " + variable_name + ":" + value_str)
                else:
                    raise ValueError("Invalid line format: " + line)
    except FileNotFoundError:
        raise FileNotFoundError("File not found: " + fileName)
    return symbol_table

##############################################################################
# parse
############################################################################## 
    
def parse(tokens):
    """parse: list(String) -> Node
    From a prefix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    precondition: tokens is a non-empty list of strings
    """
    if not tokens:
        return None
    token = tokens.pop(0)
    if token.isdigit() or (token[1:].isdigit() and token[0] == "-"):
        return LiteralNode(token)
    elif token.isalpha():
        return VariableNode(token)
    elif token in ["+", "-", "*", "//"]:
        left = parse(tokens)
        right = parse(tokens)
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
    """
    if isinstance(node, LiteralNode):
        return str(node.val)
    elif isinstance(node, VariableNode):
        return node.name
    elif isinstance(node, MathNode):
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
    """
    if isinstance(node, LiteralNode):
        return int(node.val)
    elif isinstance(node, VariableNode):
        if node.name in sym_tbl:
            return sym_tbl[node.name]
        else:
            raise ValueError("Undefined variable: " + node.name)
    elif isinstance(node, MathNode):
        left_val = evaluate(node.left, sym_tbl)
        right_val = evaluate(node.right, sym_tbl)
        if node.operator == '+':
            return left_val + right_val
        elif node.operator == '-':
            return left_val - right_val
        elif node.operator == '*':
            return left_val * right_val
        elif node.operator == '//':
            if right_val != 0:
                return left_val // right_val
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
