---
name: python-debug-failure
description: Diagnose a failing Python test or bug with a minimal safe fix
argument-hint: Paste the failing test, traceback, or bug description
target: github-copilot
---

Act as a senior Python engineer debugging an issue in this repository.

Problem context:

`${input:Paste the failing test, traceback, or bug description}`

Analyze the likely root cause.

Return:

- the most likely cause
- the risky file or lines to inspect
- the smallest safe fix
- any test cases that should be added or updated

Keep the explanation practical and avoid speculative large rewrites.
