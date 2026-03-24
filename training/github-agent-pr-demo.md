# GitHub Agent PR Demo Pipeline

This guide keeps the demo simple:

1. GitHub Copilot agent reads code and makes a small fix
2. the agent raises a pull request
3. GitHub Actions runs CI
4. a human approves the PR
5. GitHub auto-merges after approval and passing checks

## Files Involved

- CI workflow: `.github/workflows/ci.yml`
- Auto-merge enabler: `.github/workflows/enable-auto-merge.yml`

## One-Time GitHub Settings

Configure these once in the GitHub repository settings:

### 1. Enable auto-merge

In GitHub:

- go to `Settings` -> `General`
- enable `Allow auto-merge`

### 2. Protect `main`

In GitHub:

- go to `Settings` -> `Branches`
- add a branch protection rule for `main`

Recommended rule settings:

- require a pull request before merging
- require 1 approval
- require status checks to pass before merging
- select the `CI` workflow check

## Demo Flow

### A. Ask the agent to review and fix code

Use GitHub Copilot in VS Code or GitHub to:

- review a small file
- make a safe change
- open a PR

### B. Add the merge label

Add this label to the PR:

- `demo-auto-merge`

That label triggers the auto-merge workflow to run:

```bash
gh pr merge --auto --squash <pr-url>
```

The PR will not merge immediately.

It will wait for:

- required CI checks to pass
- required human approval

### C. Human approval

Approve the PR in GitHub UI.

This is the key human-in-the-loop checkpoint.

### D. Automatic merge

Once approval and checks are complete, GitHub merges the PR automatically.

## Recommended Live Demo Script

Say:

> "The agent can read the code, make the change, and open the PR. But the repository still enforces a human approval gate. Only after approval and passing CI does GitHub merge automatically."

## Helpful Commands

Create the label once if it does not exist yet:

```bash
gh label create demo-auto-merge --color 1d76db --description "Enable auto-merge for demo PRs"
```

Add the label to a PR:

```bash
gh pr edit <pr-number> --add-label demo-auto-merge
```

Open the PR in a browser:

```bash
gh pr view <pr-number> --web
```
