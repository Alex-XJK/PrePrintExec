from ppe import ppe_debug

def risky_division(x, y):
    return x / y

@ppe_debug
def process_data(data):
    total = sum(data)  ## Summing data
    avg = total / len(data)  ## Calculating average
    # Many other complex operations...
    result = risky_division(avg, 0)  ## -
    return result


if __name__ == "__main__":
    process_data([1, 2, 3])
    # Output:
    # PPE: Summing data
    # PPE: Calculating average
    # PPE: result = risky_division(avg, 0)
    # Traceback (most recent call last):
    #   ...
    # ZeroDivisionError: float division by zero
