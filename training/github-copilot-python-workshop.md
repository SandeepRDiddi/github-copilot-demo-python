# GitHub Copilot Workshop for Python Developers

## Outcome

By the end of this session, Python developers should be able to:

- use GitHub Copilot for code completion, chat, test generation, and refactoring
- write prompts that give Copilot enough context to be useful
- review Copilot output critically instead of accepting it blindly
- apply Copilot safely in a real Python codebase

## Audience

- developers who are new to GitHub Copilot
- Python engineers with basic familiarity in functions, classes, tests, and debugging

## Recommended Format

- Duration: 90 minutes
- Mode: live demo plus hands-on lab
- Repo for demo: this project
- Lab for practice: `training/lab/starter/order_summary.py`

## Session Flow

### 1. Foundations: what Copilot is and is not (10 min)

Key message:

- Copilot is a coding assistant, not an auto-pilot
- it is strongest when the developer provides context, constraints, and review
- it can accelerate boilerplate, tests, explanations, and refactors
- it can still hallucinate APIs, misunderstand business rules, or over-engineer

### 2. Show the interface and basic modes (10 min)

Demonstrate:

- inline code completion
- chat in the IDE
- edit / fix / explain flows
- asking for tests, docstrings, and refactors

### 3. Live demo in a real Python repo (30 min)

Use the app code so learners see Copilot in a realistic setting.

#### Demo A: Understand unfamiliar code

Open `src/app/server.py` and ask Copilot:

```text
Explain this file to a Python developer who is new to MCP. Keep it short and highlight the control flow.
```

Follow-up:

```text
Which functions here would be most important for onboarding a new engineer, and why?
```

Teaching point:

- Copilot is useful for orientation, not just generation

#### Demo B: Generate tests from existing behavior

Open `src/app/server.py` and `tests/test_registry.py`.

Prompt:

```text
Based on the patterns in this repo, draft pytest tests for server_status, list_integrations, and server_health. Reuse the style already used in tests.
```

Teaching point:

- better results come from pointing Copilot at existing repo conventions

#### Demo C: Safer refactoring

Pick a small file such as `src/app/shared/filesystem.py` or `src/app/registry.py`.

Prompt:

```text
Suggest a refactor that improves readability without changing behavior. Explain the tradeoffs before writing code.
```

Teaching point:

- ask for explanation first when the change has design consequences

#### Demo D: Improve documentation

Prompt:

```text
Add concise docstrings for public functions in this file. Match the tone of the rest of the project and avoid repeating obvious details.
```

Teaching point:

- Copilot is great for polish when you give tone and scope

### 4. Hands-on lab for beginners (25 min)

Move participants to `training/lab/README.md`.

They will practice:

- asking Copilot to explain a starter file
- generating a function implementation from tests and comments
- asking for edge cases
- improving naming and small refactors
- asking Copilot to write tests, then reviewing them

### 5. Review and guardrails (15 min)

Close with the habits that separate useful Copilot adoption from unsafe usage.

## Good Prompts for Python Developers

Use this formula:

```text
Act as a senior Python developer.
Context: <what this file does>
Goal: <what I want changed>
Constraints: <style, libraries, edge cases, no behavior change, test style>
Output: <code, explanation, tests, or both>
```

Example:

```text
Act as a senior Python developer.
Context: This file registers integrations for an MCP server.
Goal: Add tests for the server metadata tools.
Constraints: Use pytest, match the existing test style in this repo, avoid network calls, and keep tests focused on behavior.
Output: test code plus a short explanation of what each test covers.
```

## Guardrails to Teach Early

- always review generated code before accepting it
- ask Copilot to explain why a change is correct
- compare suggestions against local project patterns
- run tests after meaningful changes
- do not paste secrets, tokens, or private production data into prompts
- use small scoped prompts before broad rewrite prompts

## Common Beginner Mistakes

- asking vague prompts like "fix this"
- accepting code that introduces new abstractions with no real value
- trusting imported libraries or APIs that are not actually in the project
- skipping tests because the generated code "looks right"

## Suggested Success Criteria

After the workshop, learners should be able to:

- write one strong prompt with context and constraints
- use Copilot to explain unfamiliar Python code
- generate or improve a pytest test case
- identify one bad Copilot suggestion and reject it

## Facilitator Notes

- keep the first live prompt simple so the room sees an early win
- narrate your review process out loud
- when Copilot makes a weak suggestion, use that as a teaching moment
- emphasize that the developer owns correctness, naming, design, and security
