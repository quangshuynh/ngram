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
    if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
        return LiteralNode(token)
    elif token.isalpha():
        return VariableNode(token)
    elif token in ['+', '-', '*', '//']:
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
        left_str = infix(node.left)
        right_str = infix(node.right)
        return str(left_str + node.operator + right_str)
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
    
    pass
    
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
    
    print("Herp, enter prefix expressions, e.g.: + 10 20 (ENTER to quit)...")
    
    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefix_exp = input("derp> ")
        if prefix_exp == "":
            break
            
        # STUDENT: GENERATE A LIST OF TOKENS FROM THE PREFIX EXPRESSION
        
        # STUDENT: CALL parse WITH THE LIST OF TOKENS AND SAVE THE ROOT OF 
        # THE PARSE TREE.
            
        # STUDENT: GENERATE THE INFIX EXPRESSION BY CALLING infix AND SAVING
        # THE STRING.

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.    
        print("Derping the infix expression:")
        
        # STUDENT: EVALUTE THE PARSE TREE BY CALLING evaluate AND SAVING THE
        # INTEGER RESULT.

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.
        print("Derping the evaluation:")
         
    print("Goodbye Herp :(")
    
if __name__ == "__main__":
    main()
