from datetime import datetime
import ast
import operator as op

_ALLOWED = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}

def _eval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED:
        return _ALLOWED[type(node.op)](_eval(node.operand))

    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED:
        left = _eval(node.left)
        right = _eval(node.right)
        if isinstance(node.op, ast.Pow) and abs(right) > 100:
            raise ValueError("Power is too large.")
        return _ALLOWED[type(node.op)](left, right)

    raise ValueError("Only basic arithmetic is supported.")

def calculator(expression: str) -> str:
    """Calculate a basic arithmetic expression."""
    try:
        tree = ast.parse(expression, mode="eval")
        result = _eval(tree.body)
        return str(result)
    except Exception as e:
        return f"Calculator error: {e}"

def current_date() -> str:
    """Return the current server date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
