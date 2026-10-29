import json
import unittest
from consulting.server import calculate, ROOT
from consulting.business_case import business_case


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.values = json.loads((ROOT / 'data/scenarios.json').read_text())['base']

    def test_workspace_uses_existing_model(self):
        self.assertEqual(calculate(self.values), business_case(**self.values))

    def test_invalid_and_extra_values_rejected(self):
        for change in [{'adoption': True}, {'adoption': float('nan')}, {'monthly_volume': 1e100},
                       {'adoption': 2}, {'api_key': 'never reflected'}]:
            with self.assertRaises(ValueError):
                calculate({**self.values, **change})

    def test_zero_adoption_remains_a_cost(self):
        value = calculate({**self.values, 'adoption': 0})
        self.assertEqual(value['freed_hours_monthly'], 0)
        self.assertLess(value['net_capacity_value_monthly_eur'], 0)
        self.assertIsNone(value['payback_months'])
