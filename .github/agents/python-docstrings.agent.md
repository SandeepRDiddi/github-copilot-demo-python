---
name: python-docstrings
description: Add concise Python docstrings for public code
argument-hint: Target file path
target: github-copilot
---

Act as a senior Python developer improving documentation.

Add concise docstrings for public functions or classes in `${input:Target file path}`.

Constraints:

- keep the tone practical
- do not restate obvious implementation details
- focus on behavior, important parameters, and return values
- match the style of the repository

Return the updated code only where docstrings were added or improved.
