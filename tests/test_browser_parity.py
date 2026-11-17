"""The browser console on GitHub Pages runs site/console/model.js. These fixtures pin the Python model's
answers; scripts/check-browser-port.mjs checks the JavaScript port against the same file."""
import json
import unittest
from pathlib import Path

from consulting.business_case import business_case

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ("freed_hours_monthly", "capacity_value_monthly_eur", "net_capacity_value_monthly_eur",
          "payback_months", "first_year_net_capacity_value_eur")


class BrowserParityFixtures(unittest.TestCase):
    def test_fixtures_match_the_python_model(self):
        cases = json.loads((ROOT / "tests/parity/business-case-cases.json").read_text())["cases"]
        self.assertGreaterEqual(len(cases), 40)
        for case in cases:
            with self.subTest(case["name"]):
                expected = case["expected"]
                if "error" in expected:
                    with self.assertRaisesRegex(ValueError, expected["error"]):
                        business_case(**case["input"])
                else:
                    result = business_case(**case["input"])
                    self.assertEqual({k: result[k] for k in FIELDS}, expected)

    def test_static_console_is_built_from_the_current_console(self):
        import importlib.util

        spec = importlib.util.spec_from_file_location("build_console_site", ROOT / "scripts/build_console_site.py")
        builder = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(builder)
        built = (ROOT / "site/console/index.html").read_text()
        self.assertEqual(builder.render(), built, "outdated: run python scripts/build_console_site.py")


if __name__ == "__main__":
    unittest.main()
