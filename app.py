from flask import Flask, request,jsonify
from ast_engine import create_rule, combine_rules, evaluate_rule  # Import your functions

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.json
    rule_string = data.get('rule_string')
    
    if not rule_string:
        return {"error": "'rule_string' key is missing"}, 400
    
    ast = create_rule(rule_string)
    return {"ast": ast}, 200  # Return AST wrapped in a dictionary

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    try:
        data = request.json.get('data')
        ast = request.json.get('ast')

        # Call the evaluate_rule function
        result = evaluate_rule(ast, data)

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    data = request.json
    rules = data.get('rules')  # Extracting the rules from the request body

    if not rules or not isinstance(rules, list):  # Check if rules is a list and not empty
        return {"error": "'rules' key is missing or is not a list"}, 400

    combined_result = combine_rules(rules)  # Call the combine_rules function
    return {"ast": combined_result}, 200  # Return combined AST wrapped in a dictionary

if __name__ == '__main__':
    app.run(debug=True)
