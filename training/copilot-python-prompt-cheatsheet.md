# GitHub Copilot Prompt Cheat Sheet for Python

## Explain Code

```text
Explain this Python file in plain English. Focus on control flow, key functions, and what I should read next.
```

## Write a Function

```text
Implement this function in Python.
Constraints:
- keep it readable
- handle edge cases
- avoid extra dependencies
- add a short docstring
```

## Generate Tests

```text
Write pytest tests for this function.
Cover normal cases, edge cases, and invalid inputs.
Match the style already used in this repository.
```

## Refactor Safely

```text
Refactor this code for readability without changing behavior.
First explain the refactor plan, then show the updated code.
```

## Debug a Failure

```text
This test is failing.
Explain the likely root cause, point to the risky lines, and propose the smallest safe fix.
```

## Improve Naming

```text
Suggest better names for variables, functions, and helpers in this file.
Keep the behavior exactly the same.
```

## Add Documentation

```text
Add concise Python docstrings for public functions in this file.
Do not restate the obvious. Focus on behavior and important parameters.
```

## Review Copilot Output

After Copilot suggests code, ask:

```text
Review this code critically.
What assumptions is it making?
Which edge cases are still missing?
Does it match Python best practices for this project?
```

## Strong Prompt Pattern

```text
Context: <where this code lives and what it does>
Goal: <what change you want>
Constraints: <libraries, style, behavior, tests, performance, security>
Output: <code, explanation, or both>
```
