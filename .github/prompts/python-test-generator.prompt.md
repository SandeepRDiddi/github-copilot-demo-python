---
agent: 'agent'
name: python-test-generator
description: Generate pytest tests that match this repository's style
argument-hint: Target file or function
---

Act as a senior Python engineer writing tests for this repository.

Using `${input:Target file or function}` as context, draft pytest tests.

Constraints:

- match the style already used in this repository
- cover normal behavior
- cover edge cases
- cover invalid input or failure behavior where relevant
- avoid unnecessary mocking
- avoid network calls unless explicitly required

Return:

- the test code
- a short note explaining what each test is intended to prove
