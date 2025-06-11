# PPE - PrePrintExec

A lightweight, non-intrusive debugging tool that uses AST transformation to print debug information before executing your Python code.

## Installation

```bash
pip install ppe-debug
```

## Quick Start
```python
from ppe import ppe_debug

@ppe_debug
def my_function():
    x = 10     ## Setting x value
    y = x * 2  ## -
    return y

result = my_function()
# Output:
# PPE: Setting x value
# PPE: y = x * 2
```

## Features

- 🎯 **Non-intrusive**: Just add a decorator
- 🔧 **Multiple debug modes**: Custom messages, statement echoing, or variable inspection
- 🚀 **Zero dependencies**: Uses only Python standard library
- 🧹 **Clean**: Remove decorator to disable debugging
- 🔍 **Comprehensive**: Works with all Python statements

## Usage
### Custom Debug Messages
Use `## comments` to print your custom debug messages.
```python
@ppe_debug
def calculate():
    result = 10 + 5  ## Adding two numbers
    return result

# Output:
# PPE: Adding two numbers
```

### Statement Echoing
Use `## -` to echo the actual statement being executed.
```python
@ppe_debug
def calculate():
    result = 10 + 5  ## -
    return result

# Output:
# PPE: result = 10 + 5
```

### Variable Inspection
Use `## @var1,var2` to inspect variable values (prints after execution)  
Use `## @before:var1,var2` to inspect variables before execution   
Use `## @after:var1,var2` to explicitly inspect variables after execution  
Note that if some variables are not defined at the time of inspection, they will trigger an error.
```python
@ppe_debug
def calculate():
    a = 1  ## @a
    b = 2  ## @after:b
    c = a + b  ## @before:a,b
    d = 10  ## @before:d
    return c

# Output:
# PPE: [After] a=1
# PPE: [After] b=2
# PPE: [Before] a=1, b=2
# PPE: Variable inspection failed
```

## License
MIT License - see LICENSE file for details.