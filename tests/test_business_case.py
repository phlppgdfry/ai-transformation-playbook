import math
import unittest
from consulting.business_case import business_case, prioritize


class BusinessCaseTests(unittest.TestCase):
    def values(self, **changes):
        values = dict(monthly_volume=1000,minutes_before=8,minutes_after=3,hourly_cost=60,adoption=.5,automation_coverage=.8,monthly_run_cost=100,implementation_cost=9000)
        values.update(changes)
        return values

    def test_capacity_and_payback(self):
        result = business_case(**self.values())
        self.assertEqual(result["freed_hours_monthly"],33.33)
        self.assertEqual(result["net_capacity_value_monthly_eur"],1900)
        self.assertEqual(result["payback_months"],4.74)

    def test_no_adoption_no_savings(self):
        result = business_case(**self.values(adoption=0))
        self.assertEqual(result["net_capacity_value_monthly_eur"],-100)
        self.assertIsNone(result["payback_months"])

    def test_rework_can_reverse_benefits(self):
        result = business_case(**self.values(rework_rate=1,rework_minutes=10))
        self.assertLess(result["freed_hours_monthly"],0)
        self.assertIsNone(result["payback_months"])

    def test_invalid_assumptions(self):
        for changes in ({"adoption":1.1},{"hourly_cost":-1},{"monthly_volume":math.inf},{"minutes_after":math.nan}):
            with self.assertRaises(ValueError):
                business_case(**self.values(**changes))

    def test_risk_cannot_be_scored_away(self):
        case = dict(id="1",name="risky",impact=5,feasibility=5,data_readiness=5,adoption_readiness=5,risk=5)
        result = prioritize([case])[0]
        self.assertEqual(result["score"],5)
        self.assertEqual(result["gate"],"specialist_review")

    def test_invalid_priority(self):
        with self.assertRaises(ValueError):
            prioritize([dict(id="1",name="bad",impact=6,feasibility=1,data_readiness=1,adoption_readiness=1,risk=1)])
