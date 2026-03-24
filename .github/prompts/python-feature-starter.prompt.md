---
agent: 'agent'
name: python-feature-starter
description: Break a Python coding task into a safe Copilot-assisted implementation plan
argument-hint: Describe the feature or change
---

Act as a senior Python engineer planning a feature for this repository.

Task:

`${input:Describe the feature or change}`

Return:

- a small implementation plan
- the files likely involved
- the tests that should be written or updated
- one strong Copilot prompt to start the implementation

Keep the plan incremental and safe for a developer who will review each step.
