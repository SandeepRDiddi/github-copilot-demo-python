# GitHub Copilot Demo Skills

This folder contains reusable GitHub Copilot prompt files that you can demo as team "skills."

## Included Prompt Skills

- `python-onboarding.prompt.md`
  Explains a Python file for a new developer.
- `python-test-generator.prompt.md`
  Drafts pytest tests in the style of this repository.
- `python-refactor-safe.prompt.md`
  Suggests a safe readability refactor.
- `python-debug-failure.prompt.md`
  Diagnoses a failing test or bug and proposes the smallest safe fix.
- `python-code-review.prompt.md`
  Reviews code for correctness, readability, and test gaps.
- `python-docstrings.prompt.md`
  Adds concise public-facing Python docstrings.
- `python-lab-coach.prompt.md`
  Coaches a beginner through the training lab.
- `python-prompt-improver.prompt.md`
  Rewrites weak prompts into stronger ones.
- `python-feature-starter.prompt.md`
  Turns a feature request into a small Copilot-assisted plan.

## How to Demo Them

1. Open Copilot Chat in your IDE.
2. Make sure you opened the repository root so Copilot can see `.github/prompts`.
3. In a prompt-file-aware IDE client, invoke one directly with a slash command such as `/python-code-review`.
4. If the command does not appear, update to a recent Copilot-enabled IDE/extension, reload the window, and check the chat customization diagnostics.
5. Show a normal question first without a prompt file, then run the matching prompt file and compare the response quality and structure.

## Notes

- These files are repository prompt files, not built-in slash commands.
- The slash command name comes from the filename, so `python-code-review.prompt.md` becomes `/python-code-review`.
- Prompt files are supported in repository-prompt-aware IDE clients such as recent versions of VS Code and Visual Studio.
- GitHub Copilot CLI does not surface repository prompt files as `/` commands; use the matching custom agents in `.github/agents` instead.

## Recommended Demo Order

1. `python-onboarding.prompt.md`
2. `python-test-generator.prompt.md`
3. `python-refactor-safe.prompt.md`
4. `python-code-review.prompt.md`

That sequence shows explanation, generation, improvement, and review, which usually lands well with clients.
