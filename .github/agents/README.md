# GitHub Copilot CLI Agents

This folder contains repository custom agents that mirror the reusable workflows in `.github/prompts`.

## Why this folder exists

Workspace prompt files in `.github/prompts` are intended for prompt-file-aware IDE clients such as VS Code and Visual Studio. GitHub Copilot CLI does not surface those repository prompt files as slash commands in the terminal.

Repository custom agents in `.github/agents` are the CLI-native way to make those workflows reusable in Copilot CLI.

## How to use them in Copilot CLI

1. Start `copilot` from the repository root.
2. Run `/agent`.
3. Select one of the `python-*` agents from this folder.
4. Provide the target file, traceback, feature description, or other context the agent asks for.

You can also ask Copilot to use an agent by name in a normal prompt, for example `Use the python-code-review agent on src/app/server.py`.

## Agent mapping

- `python-onboarding.agent.md` mirrors `python-onboarding.prompt.md`
- `python-test-generator.agent.md` mirrors `python-test-generator.prompt.md`
- `python-refactor-safe.agent.md` mirrors `python-refactor-safe.prompt.md`
- `python-debug-failure.agent.md` mirrors `python-debug-failure.prompt.md`
- `python-code-review.agent.md` mirrors `python-code-review.prompt.md`
- `python-docstrings.agent.md` mirrors `python-docstrings.prompt.md`
- `python-lab-coach.agent.md` mirrors `python-lab-coach.prompt.md`
- `python-prompt-improver.agent.md` mirrors `python-prompt-improver.prompt.md`
- `python-feature-starter.agent.md` mirrors `python-feature-starter.prompt.md`
