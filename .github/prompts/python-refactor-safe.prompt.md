---
agent: 'agent'
name: python-refactor-safe
description: Suggest a safe readability refactor for Python code
argument-hint: Target file path
---

Act as a senior Python developer reviewing `${input:Target file path}`.

Suggest a refactor that improves readability without changing behavior.

First provide:

- the refactor plan
- why it is safe
- any tradeoffs or risks

Then provide the updated code.

Constraints:

- keep the refactor small and understandable
- prefer clarity over cleverness
- preserve existing public behavior
- follow current repository patterns
