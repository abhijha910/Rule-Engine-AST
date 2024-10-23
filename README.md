# Rule Engine with AST

## Overview
The **Rule Engine with AST** is a powerful and flexible system designed to evaluate logical rules using an Abstract Syntax Tree (AST) representation. It enables users to define complex business logic in a readable format, which can then be evaluated against input data dynamically.

## Functionality Overview

### Rule Definition and Parsing
- **Rule Syntax**: Users can define rules using a simple syntax (e.g., `"age > 20 AND name = 'John'"`).
- **AST Construction**: The system parses the rules and constructs an AST, representing the logical structure of the rules for easy evaluation.

### Evaluation Engine
- **Input Data**: Users provide data as a JSON object (e.g., `{"age": 25, "name": "John"}`).
- **Evaluation Logic**: The engine traverses the AST to evaluate the rules against the input data, returning `true` or `false` based on the evaluation results.

### Combining Rules
- Users can combine multiple rules into a single AST, allowing for complex logical expressions using operators like AND and OR.

## Features
- **Dynamic Rule Evaluation**: Allows users to define and evaluate rules at runtime.
- **Logical Operators**: Supports various operators including AND, OR, equality (`=`), and comparisons (`>`, `<`).
- **Abstract Syntax Tree Representation**: Utilizes an AST for efficient rule evaluation and easy manipulation.
- **Flexible Operand Handling**: Capable of handling different types of operands and conditions.

## Example Rule Evaluation

### Example Input
- **Rule**: `age > 20 AND name = 'John'`
- **Data**: 
  ```json
  {
      "age": 25,
      "name": "John"
  }
## Example Output
    ```json
    Evaluation Result: true

## Installation Instructions
1. **Clone the repository**:
   ```bash
  git clone https://github.com/abhijha910/rule-engine-ast.git
    
2. **Navigate to the project directory**:
    ```bash
    cd rule-engine-ast

3. **Create and activate a virtual environment**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`

4. **Install the required dependencies**:
    
    ```bash
    pip install -r requirements.txt

## Running the Rule Engine
To start the evaluation engine, you can use the provided script. Here's an example command to evaluate a rule:

      ```bash
      python src/main.py

## Authors
Abhyanand Jha - abhyanandlsc@gmail.com
