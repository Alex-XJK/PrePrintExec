# PPE - PrePrintExec

A lightweight, non-intrusive debugging tool that uses AST transformation to print debug information before executing your Python code.

## Why PPE?
In real-world development, inserting print statements is one of the most common debugging techniques. But doing so often clutters the codebase, requires cleanup before commits, and introduces friction in the development cycle. PPE (PrePrintExec) offers a clean, elegant alternative: reuse your existing inline comments as actionable debug logs.

With just a decorator, PPE automatically prints your comment string before executing each line—turning what used to be dead documentation into live, contextual insight. This helps you:

- 🧠 Understand complex workflows step by step
- 🔎 Instantly locate which operation failed during runtime
- 🧼 Avoid littering your code with temporary print() statements
- ⚙️ Toggle debugging on/off cleanly with a single annotation

Unlike traditional logging tools, PPE does not require you to write explicit logging code. It uses your comments—already written for humans—and makes them available at runtime when you need them most.

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

## For Researchers & Advanced Developers
At a glance, PPE might appear to be a simple utility that converts inline comments into `print()` statements. However, due to how the Python compiler works, this functionality requires much deeper intervention.

In Python, comments are **discarded during the parsing stage** and are **not included in the Abstract Syntax Tree (AST)**, which is what most static analysis or transformation tools operate on. To retain access to the comment strings, PPE synchronizes the parsed AST (`ast` module from Python’s standard library) with the original source lines by matching line numbers, effectively reattaching comments to the corresponding AST nodes.

Rather than modifying source code textually or relying on deprecated tools like `lib2to3`, PPE implements a custom `ast.NodeTransformer` that walks and transforms the AST in a **semantically-aware** and **structurally sound** manner. The transformed tree is then dynamically compiled and executed, preserving all scope, bindings, and runtime behavior.

To make this accessible, we wrap the entire transformation and execution logic inside a lightweight decorator (`@ppe_debug`), so developers can instrument their functions non-invasively—without code duplication or string parsing hacks.

This project serves not just as a debugging tool, but as a **practical demonstration of compiler-inspired instrumentation** using Python's AST. If you're interested in programming languages, interpreters, or tooling, PPE is a compact but meaningful example of source-level augmentation with runtime effects.

## License
MIT License - see LICENSE file for details.