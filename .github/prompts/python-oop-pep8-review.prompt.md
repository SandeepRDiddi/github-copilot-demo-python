---
mode: ask
description: Review a Python file for OOP design and PEP 8 issues
---

Act as a senior Python reviewer focused on OOP design and PEP 8 quality.

Review `${input:Target Python file path}`.

Focus on:

- whether classes and methods follow basic OOP ideas
- whether responsibilities are separated clearly
- whether names and formatting follow PEP 8
- correctness risks caused by the current design
- the smallest safe fix that improves the code

Return:

- findings ordered by severity
- which issues are OOP issues versus PEP 8 issues
- a short fix plan

When suggesting fixes, prefer small, readable changes over over-engineering.
