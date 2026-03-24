# Beginner Lab: Python Order Summary

## Goal

This lab helps new GitHub Copilot users practice on a small Python problem before they touch a production codebase.

Use the starter file:

- `training/lab/starter/order_summary.py`

Use the reference tests as a target:

- `training/lab/reference/test_order_summary.py`

## What Learners Practice

- asking Copilot to explain unfamiliar Python code
- implementing functions from comments and tests
- improving edge-case handling
- generating tests and reviewing them critically
- refactoring small Python functions safely

## Suggested Flow

### Step 1: Ask Copilot to explain the starter

Prompt:

```text
Explain this file to a beginner Python developer. Tell me which functions are incomplete and what each one should probably do.
```

### Step 2: Implement the first function

Prompt:

```text
Implement normalize_order_items.
Constraints:
- input is a list of dicts
- keep only name, quantity, and unit_price
- trim whitespace in the name
- quantity must be at least 1
- unit_price cannot be negative
- return clean dictionaries
```

### Step 3: Implement the summary logic

Prompt:

```text
Implement build_order_summary.
Use clear Python.
Return subtotal, tax, total, item_count, and item_names.
Round currency values to 2 decimals.
```

### Step 4: Ask for tests

Prompt:

```text
Write pytest tests for this file.
Cover happy path, empty input, whitespace trimming, negative prices, and quantity defaults.
```

### Step 5: Review the generated code

Prompt:

```text
Review this implementation like a senior Python engineer.
What edge cases or readability issues should I improve before I keep it?
```

## Teaching Notes

- learners should compare Copilot output with the reference tests
- encourage them to reject weak suggestions and ask better follow-up prompts
- remind them that passing tests is necessary, but not enough
