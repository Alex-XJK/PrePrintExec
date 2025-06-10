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
- 🔧 **Two debug modes**: Custom messages or statement echoing
- 🚀 **Zero dependencies**: Uses only Python standard library
- 🧹 **Clean**: Remove decorator to disable debugging
- 🔍 **Comprehensive**: Works with all Python statements

## Usage
### Custom Debug Messages
```python
@ppe_debug
def calculate():
    result = 10 + 5  ## Adding two numbers
    return result
```

### Statement Echoing
```python
@ppe_debug
def calculate():
    result = 10 + 5  ## -
    return result
```

## License
MIT License - see LICENSE file for details.