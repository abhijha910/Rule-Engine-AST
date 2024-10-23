import unittest
from app import app

class RuleEngineTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_rule(self):
        response = self.app.post('/create_rule', json={"rule_string": "age > 30 AND department = 'Sales'"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('ast', response.json)

    def test_invalid_rule(self):
        response = self.app.post('/create_rule', json={"rule_string": "age > 30 && department "})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_combine_rules(self):
        rules = [
            "age > 30 AND department = 'Sales'",
            "age < 25 AND department = 'Marketing'"
        ]
        response = self.app.post('/combine_rules', json={"rules": rules})
        self.assertEqual(response.status_code, 200)
        self.assertIn('ast', response.json)

    def test_evaluate_rule(self):
        data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
        rule_string = "age > 30 AND department = 'Sales'"
        ast = self.app.post('/create_rule', json={"rule_string": rule_string}).json['ast']
        response = self.app.post('/evaluate_rule', json={"ast": ast, **data})
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json)

    def test_evaluate_invalid_data(self):
        rule_string = "age > 30 AND department = 'Sales'"
        ast = self.app.post('/create_rule', json={"rule_string": rule_string}).json['ast']
        response = self.app.post('/evaluate_rule', json={"ast": ast})
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()
