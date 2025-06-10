import ast
import inspect
import textwrap
from typing import Any, Callable


class PPETransformer(ast.NodeTransformer):
    """AST transformer that adds debug print statements based on comments."""

    def __init__(self, source_lines):
        self.source_lines = source_lines

    def visit_stmt_with_comment(self, node, line_no):
        """Check if a statement has a PPE comment and transform accordingly."""
        if line_no <= len(self.source_lines):
            line = self.source_lines[line_no - 1].strip()

            # Look for ## comments
            if '##' in line:
                comment_part = line.split('##', 1)[1].strip()

                if comment_part == '-':
                    # Case 2: Print the statement itself
                    stmt_text = line.split('##')[0].strip()
                    print_node = ast.Expr(
                        value=ast.Call(
                            func=ast.Name(id='print', ctx=ast.Load()),
                            args=[ast.Constant(value=f"PPE: {stmt_text}")],
                            keywords=[]
                        )
                    )
                    return [print_node, node]

                elif comment_part:
                    # Case 1: Print the comment string
                    print_node = ast.Expr(
                        value=ast.Call(
                            func=ast.Name(id='print', ctx=ast.Load()),
                            args=[ast.Constant(value=f"PPE: {comment_part}")],
                            keywords=[]
                        )
                    )
                    return [print_node, node]

        return node

    def visit_Assign(self, node):
        """Transform assignment statements."""
        result = self.visit_stmt_with_comment(node, node.lineno)
        if isinstance(result, list):
            return result
        return self.generic_visit(node)

    def visit_AnnAssign(self, node):
        """Transform annotated assignment statements."""
        result = self.visit_stmt_with_comment(node, node.lineno)
        if isinstance(result, list):
            return result
        return self.generic_visit(node)

    def visit_AugAssign(self, node):
        """Transform augmented assignment statements (+=, -=, etc.)."""
        result = self.visit_stmt_with_comment(node, node.lineno)
        if isinstance(result, list):
            return result
        return self.generic_visit(node)

    def visit_Expr(self, node):
        """Transform expression statements."""
        result = self.visit_stmt_with_comment(node, node.lineno)
        if isinstance(result, list):
            return result
        return self.generic_visit(node)

    def visit_If(self, node):
        """Transform if statements."""
        result = self.visit_stmt_with_comment(node, node.lineno)
        if isinstance(result, list):
            return result
        return self.generic_visit(node)

    def visit_For(self, node):
        """Transform for loops."""
        result = self.visit_stmt_with_comment(node, node.lineno)
        if isinstance(result, list):
            return result
        return self.generic_visit(node)

    def visit_While(self, node):
        """Transform while loops."""
        result = self.visit_stmt_with_comment(node, node.lineno)
        if isinstance(result, list):
            return result
        return self.generic_visit(node)

    def visit_Return(self, node):
        """Transform return statements."""
        result = self.visit_stmt_with_comment(node, node.lineno)
        if isinstance(result, list):
            return result
        return self.generic_visit(node)

    def visit_Break(self, node):
        """Transform break statements."""
        result = self.visit_stmt_with_comment(node, node.lineno)
        if isinstance(result, list):
            return result
        return self.generic_visit(node)

    def visit_Continue(self, node):
        """Transform continue statements."""
        result = self.visit_stmt_with_comment(node, node.lineno)
        if isinstance(result, list):
            return result
        return self.generic_visit(node)


def ppe_debug(func: Callable) -> Callable:
    """
    Decorator that enables PPE debugging for a function.

    Usage:
        @ppe_debug
        def my_function():
            a = 5  ## Initialize variable a
            b = 10 ## Initialize variable b
            c = a + b  ## -
            return c
    """

    def wrapper(*args, **kwargs):
        # Get the source code of the function
        source = inspect.getsource(func)
        source = textwrap.dedent(source)

        # Remove the decorator line
        lines = source.split('\n')
        filtered_lines = []
        skip_decorator = True

        for line in lines:
            if skip_decorator and line.strip().startswith('@'):
                continue
            elif skip_decorator and line.strip().startswith('def'):
                skip_decorator = False
                filtered_lines.append(line)
            elif not skip_decorator:
                filtered_lines.append(line)

        modified_source = '\n'.join(filtered_lines)
        source_lines = modified_source.split('\n')

        # Parse the AST
        tree = ast.parse(modified_source)

        # Transform the AST
        transformer = PPETransformer(source_lines)
        new_tree = transformer.visit(tree)

        # Fix missing locations
        ast.fix_missing_locations(new_tree)

        # Compile and execute
        code = compile(new_tree, f"<PPE:{func.__name__}>", 'exec')

        # Create execution environment
        func_globals = func.__globals__.copy()
        func_locals = {}

        # Add function arguments to locals
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        func_locals.update(bound_args.arguments)

        # Execute the transformed code
        namespace = func_globals.copy()
        namespace.update(func_locals)

        exec(code, namespace)

        # Get the transformed function and call it
        transformed_func = namespace[func.__name__]
        return transformed_func(*args, **kwargs)

    return wrapper


# Example usage and demonstration
if __name__ == "__main__":
    print("=== PPE (Python Print Enhancement) Demo ===\n")

    # Demo 1: Basic usage
    print("1. Basic Usage:")


    @ppe_debug
    def calculate_area():
        length = 10  ## Setting length
        width = 5  ## Setting width
        area = length * width  ## -
        perimeter = 2 * (length + width)  ## Calculate perimeter
        return area, perimeter


    result = calculate_area()
    print(f"Result: {result}\n")

    # Demo 2: More complex example
    print("2. Loop Example:")


    @ppe_debug
    def fibonacci_demo():
        a, b = 0, 1  ## Initialize fibonacci sequence
        for i in range(5):  ## -
            a, b = b, a + b  ## Update fibonacci values
        return a


    fib_result = fibonacci_demo()
    print(f"Fibonacci result: {fib_result}\n")

    # Demo 3: Conditional logic with elif and return
    print("3. Conditional Example with elif and return:")


    @ppe_debug
    def check_number(x):
        if x > 0:  ## Check if positive
            result = "positive"  ## -
        elif x < 0:  ## Check if negative
            result = "negative"  ## -
        else:  ## Handle zero case
            result = "zero"  ## -
        return result  ## Return the final result


    print(f"check_number(5): {check_number(5)}")
    print(f"check_number(-3): {check_number(-3)}")
    print(f"check_number(0): {check_number(0)}")

    # Demo 4: Early return example
    print("\n4. Early Return Example:")


    @ppe_debug
    def divide_numbers(a, b):
        if b == 0:  ## Check for division by zero
            return None  ## Early return for invalid input
        result = a / b  ## Perform division
        return result  ## Return division result


    print(f"divide_numbers(10, 2): {divide_numbers(10, 2)}")
    print(f"divide_numbers(10, 0): {divide_numbers(10, 0)}")

    print("\n=== PPE Demo Complete ===")

    # Usage instructions
    print("""
Usage Instructions:
1. Add @ppe_debug decorator above any function you want to debug
2. Add `## comments` with your debug message after the supported statement
3. Use `## -` to print the actual statement being executed
4. Remove the decorator when you no longer need debugging

Supported Statements:
- Assignments (=, +=, -=, etc.)
- Function calls and expressions
- if/elif/else statements  
- for/while loops
- return statements
- break/continue statements

Benefits:
- Non-intrusive debugging (no permanent code changes)
- Easy to enable/disable by adding/removing decorator
- Clear debug output with PPE prefix
- Maintains original code structure and functionality
""")