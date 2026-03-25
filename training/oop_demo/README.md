# OOP and PEP 8 Demo

This mini-demo is designed for a live Copilot workflow:

1. open flawed Python code
2. ask Copilot to review it for OOP and PEP 8 issues
3. ask Copilot to fix the issues
4. run tests to validate the behavior

## Files

- flawed example: `training/oop_demo/flawed_inventory.py`
- validation tests: `training/oop_demo/test_inventory_demo.py`

## Suggested Review Prompt

Use the `python-oop-pep8-review` agent or prompt file on:

- `training/oop_demo/flawed_inventory.py`

Or paste this directly:

```text
Review training/oop_demo/flawed_inventory.py for OOP design problems, PEP 8 violations, and correctness issues.

Return:
- findings ordered by severity
- which findings are OOP issues versus PEP 8 issues
- the smallest safe fix plan
```

## Suggested Fix Prompt

After the review, switch Copilot to Edit or Agent mode and use:

```text
Fix training/oop_demo/flawed_inventory.py based on your review.

Constraints:
- keep the behavior focused on a small inventory example
- improve OOP structure
- follow PEP 8 naming and formatting
- avoid unnecessary abstractions
- keep the code easy for beginners to read
- make sure training/oop_demo/test_inventory_demo.py passes
```

## Validation

Run:

```bash
pytest -q training/oop_demo/test_inventory_demo.py
```
