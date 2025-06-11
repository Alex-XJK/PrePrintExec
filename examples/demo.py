from ppe import ppe_debug


# Example usage and demonstration
if __name__ == "__main__":
    print("=== PPE (PrePrintExec) Demo ===\n")

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

    # Demo 5: Variable Value Inspection
    print("\n5. Variable Value Inspection:")


    @ppe_debug
    def variable_demo():
        x = 10
        y = 20  ## @after:x,y
        z = x + y  ## @after:x,y,z
        return z


    result = variable_demo()
    print(f"variable_demo result: {result}")

    # Demo 6: Before vs After inspection
    print("\n6. Before vs After Inspection:")


    @ppe_debug
    def before_after_demo():
        existing_var = 0
        existing_var = 100 ## @before:existing_var
        new_var = existing_var * 10  ## @before:existing_var,new_var
        return new_var


    result = before_after_demo()
    print(f"before_after_demo result: {result}")

    print("\n=== PPE Demo Complete ===")