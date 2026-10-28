"""Reproducible scenario model. Avoids treating model output as real-world evidence."""
import argparse
import csv
import json
import math
from pathlib import Path


def business_case(*, monthly_volume, minutes_before, minutes_after, hourly_cost, adoption, automation_coverage, monthly_run_cost, implementation_cost, rework_rate=0, rework_minutes=0):
    values = locals().copy()
    if any(not isinstance(v, (int,float)) or not math.isfinite(v) or v < 0 for v in values.values()):
        raise ValueError("All assumptions must be finite non-negative numbers")
    if any(values[name] > 1 for name in ("adoption","automation_coverage","rework_rate")):
        raise ValueError("Rates must be between zero and one")
    saved_minutes = monthly_volume * adoption * automation_coverage * (minutes_before - minutes_after - rework_rate * rework_minutes)
    freed_hours = saved_minutes / 60
    capacity_value = freed_hours * hourly_cost
    net = capacity_value - monthly_run_cost
    return {
        "assumptions":values,
        "label":"Hypothetical capacity scenario; not realized cash savings",
        "freed_hours_monthly":round(freed_hours,2),
        "capacity_value_monthly_eur":round(capacity_value,2),
        "net_capacity_value_monthly_eur":round(net,2),
        "payback_months":round(implementation_cost / net,2) if net > 0 else None,
        "first_year_net_capacity_value_eur":round(net * 12 - implementation_cost,2)
    }


def prioritize(cases):
    ranked = []
    for case in cases:
        scores = {name:float(case[name]) for name in ("impact","feasibility","data_readiness","adoption_readiness","risk")}
        if any(not math.isfinite(v) or not 1 <= v <= 5 for v in scores.values()):
            raise ValueError("Use-case scores must be finite values in 1..5")
        # Risk is a separate gate; a high weighted score cannot override it.
        score = .35*scores["impact"] + .25*scores["feasibility"] + .2*scores["data_readiness"] + .2*scores["adoption_readiness"]
        ranked.append({"id":case["id"],"name":case["name"],"score":round(score,2),"gate":"specialist_review" if scores["risk"] >= 4 else "discovery", "risk":scores["risk"]})
    return sorted(ranked, key=lambda r:(-r["score"],r["id"]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenarios", default="data/scenarios.json")
    parser.add_argument("--use-cases", default="data/use-cases.csv")
    parser.add_argument("--output", default="evidence/business-case.json")
    args = parser.parse_args()
    scenarios = json.loads(Path(args.scenarios).read_text())
    with open(args.use_cases, newline="") as file:
        ranked = prioritize(list(csv.DictReader(file)))
    results = {name:business_case(**values) for name,values in scenarios.items()}
    output = Path(args.output)
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps({"scenario_results":results,"prioritization":ranked},indent=2)+"\n")
    print(json.dumps({"report":str(output),"scenarios":len(results),"use_cases":len(ranked)}))


if __name__ == "__main__":
    main()
