class Node:
    def __init__(self, node_type, operator=None, value=None, left=None, right=None):
        self.type = node_type
        self.operator = operator
        self.value = value
        self.left = left
        self.right = right

    def to_dict(self):
        # Convert the Node to a dictionary for JSON serialization
        if self.type == 'operator':
            return {
                "type": self.type,
                "operator": self.operator,
                "left": self.left.to_dict() if self.left else None,
                "right": self.right.to_dict() if self.right else None
            }
        elif self.type == 'operand':
            return {
                "type": self.type,
                "left": self.left,
                "right": self.right
            }

    @classmethod
    def from_dict(cls, data):
        """Construct a Node from a dictionary."""
        node_type = data.get('type')
        operator = data.get('operator')
        if node_type == 'operator':
            left = cls.from_dict(data['left']) if 'left' in data else None
            right = cls.from_dict(data['right']) if 'right' in data else None
            return cls(node_type, operator, left=left, right=right)
        elif node_type == 'operand':
            return cls(node_type, left=data.get('left'), right=data.get('right'))

def parse_rule(rule_string):
    # Simple parser for demonstration purposes
    rule_string = rule_string.replace("AND", "&&").replace("OR", "||")
    
    def parse_expression(expr):
        expr = expr.strip()
        if '&&' in expr:
            parts = expr.split('&&')
            return Node('operator', 'AND', left=parse_expression(parts[0]), right=parse_expression(parts[1]))
        elif '||' in expr:
            parts = expr.split('||')
            return Node('operator', 'OR', left=parse_expression(parts[0]), right=parse_expression(parts[1]))
        else:
            if '=' in expr:
                var, val = expr.split('=', 1)  # Split on the first '=' only
                return Node('operand', left=var.strip(), right=val.strip().replace("'", ""))
            elif '>' in expr:
                var, val = expr.split('>', 1)
                return Node('operand', left=var.strip(), right=int(val.strip()))
            elif '<' in expr:
                var, val = expr.split('<', 1)
                return Node('operand', left=var.strip(), right=int(val.strip()))
            # Add more conditions as needed

    return parse_expression(rule_string)

def create_rule(rule_string):
    return parse_rule(rule_string).to_dict()  # Return as a dictionary for JSON response

def combine_rules(rules):
    # Implement combining rules into a single AST (simplified)
    combined_ast = None
    for rule in rules:
        current_rule = create_rule(rule)  # Create a new rule as a dictionary
        if combined_ast is None:
            combined_ast = Node.from_dict(current_rule)  # Create the first rule from the dict
        else:
            combined_ast = Node('operator', 'AND', left=combined_ast, right=Node.from_dict(current_rule))
    return combined_ast.to_dict()  # Ensure the combined AST is a dict

def evaluate_rule(ast, data):
    # Check if the AST or data is None
    if ast is None or data is None:
        return False

    if ast['type'] == 'operator':
        left_result = evaluate_rule(ast['left'], data)
        right_result = evaluate_rule(ast['right'], data)

        if ast['operator'] == 'AND':
            return left_result and right_result
        elif ast['operator'] == 'OR':
            return left_result or right_result
    elif ast['type'] == 'operand':
        var = ast['left']
        val = ast['right']
        if var in data:
            return data[var] == val  # Adjust comparison logic as needed
    return False
