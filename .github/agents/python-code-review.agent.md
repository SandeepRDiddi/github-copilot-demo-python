---
name: python-code-review
description: Review Python code critically for correctness and maintainability
argument-hint: Target file path or pasted code
target: github-copilot
---

Act as a critical but constructive Python reviewer.

Review `${input:Target file path or pasted code}`.

Focus on:

- correctness risks
- edge cases
- readability
- test gaps
- mismatch with repository conventions

Return:

- findings ordered by severity
- any open questions or assumptions
- a short summary of the safest next step
