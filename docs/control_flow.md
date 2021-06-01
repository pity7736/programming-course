# Control flow

Control flow are statements that can change the execution flow of a process.
There are two basic statements: conditional and loops.

## Conditional

They are statements for handling decisions by evaluation expressions. 

![if conditional](https://upload.wikimedia.org/wikipedia/commons/c/c5/If-Then-Else-diagram.svg)

Python syntax for conditional:

```python
if expression:
    # code
    # the statements within conditional must be indented.
```

```python
if expression:
    # code if expression is true
else:
    # code if expression is false
```

You can also use more than 2 cases if you want by using `elif`:

```python
if expression:
    # code
elif another_expression:
    # more code
else:
    # whatever
```
