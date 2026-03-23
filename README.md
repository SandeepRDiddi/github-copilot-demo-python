# Python MCP Multi-Integration Scaffold

This project is a starter scaffold for running multiple integrations behind one Python MCP server.
It now includes a production-ready baseline with startup validation, operational metadata, and a first usable local integration so you can run it immediately against your workspace.

## How it works

```mermaid
flowchart LR
    A["Engineer asks AI assistant a question"] --> B["AI client calls MCP tools"]
    B --> C["MCP server receives request"]
    C --> D["Safety and config layer validates access"]
    D --> E["Workspace tools read project files"]
    D --> F["Postgres tools run read-only queries"]
    E --> G["Structured results returned to AI"]
    F --> G
    G --> H["AI explains issue, data, or next action"]
```

This is the core idea of the project: the AI does not directly touch everything on its own. It goes through one controlled MCP server that applies rules, limits, and safe integrations before returning useful answers.

## Real-world example

### Story flow: missing invoices

```text
Engineer: "A customer says their invoices vanished from the app. We have a tiny billing mystery."

AI Assistant: "Detective mode on. I'll check the code path and the database safely through the MCP server."

MCP Server: "I am the careful sidekick. I can inspect the workspace, look at the Postgres schema, and run read-only queries with limits."

AI Assistant: "Clue #1: I found the invoice loading logic. The app only shows invoices where status = active."

AI Assistant: "Clue #2: I checked Postgres. The customer's invoices exist, but they are marked archived."

Engineer: "So the data is not missing. It is hiding behind a filter like a cat behind a curtain."

AI Assistant: "Exactly. Case closed. This is a business-rule or data-state issue, not a missing-record issue."
```

### What happened behind the scenes

```mermaid
sequenceDiagram
    participant E as Engineer
    participant A as AI Assistant
    participant M as MCP Server
    participant W as Workspace Tools
    participant P as Postgres Tools

    E->>A: "Why are invoices missing?"
    A->>M: Request investigation
    M->>W: Read invoice-related code files
    W-->>M: Return code context
    M->>P: Inspect schema and run read-only query
    P-->>M: Return safe query results
    M-->>A: Return structured findings
    A-->>E: Explain root cause and next step
```

### Why this matters

Without this server, an engineer often has to jump between code, database tools, and manual investigation steps.

With this server:

- the AI can gather code and database context in one place
- access stays controlled and read-only where it matters
- the engineer gets a faster explanation, not just raw data
- the team gets a repeatable troubleshooting pattern instead of one-off scripts

Small details like this matter because engineers remember systems that are both useful and pleasant to use. A little story helps the workflow stick in memory, which makes the technical value easier to explain and easier to adopt.

## What this scaffold gives you

- One `FastMCP` server process
- A small integration contract so each provider stays isolated
- Config-driven enable/disable flags per integration
- Startup validation for critical configuration
- Safer production defaults for external integrations
- Server health and status tools for operational visibility
- A built-in workspace integration with safe local file tools
- A real read-only Postgres integration for schema discovery and queries
- Two starter integrations: GitHub and Slack
- Basic tests around server registration

## Project layout

```text
src/app/
  server.py
  config.py
  registry.py
  logging.py
  types.py
  integrations/
    workspace/
    github/
    slack/
  shared/
tests/
```

## Quick start

1. Create a virtual environment.
2. Install dependencies:

```bash
pip install -e ".[dev]"
```

3. Copy the example environment file and fill in any tokens you need:

```bash
cp .env.example .env
```

4. Install the package into a Python 3.11 environment:

```bash
python3.11 -m pip install -e ".[dev]"
```

5. Run the server:

```bash
python3.11 -m app.server
```

Or use the installed console script:

```bash
mcp-multi-server
```

## CI and local stack

GitHub Actions is configured in [.github/workflows/ci.yml](/Users/sandeepdiddi/Documents/New%20project/.github/workflows/ci.yml) to:

- install the project on Python 3.11
- compile the source tree
- run the test suite

For a repeatable local setup with Postgres, use [docker-compose.yml](/Users/sandeepdiddi/Documents/New%20project/docker-compose.yml):

```bash
docker compose up --build
```

That stack starts:

- a Postgres 16 container on `localhost:5432`
- the MCP server container with the Postgres integration enabled

## First usable tools

With only the workspace integration enabled, the server is already useful. It exposes:

- `server_health`
- `server_status`
- `list_integrations`
- `workspace_list_files`
- `workspace_read_text_file`

Those tools are scoped to `MCP_WORKSPACE_ROOT`, so the server can inspect files inside your chosen project root without wandering outside it.

## Postgres integration

To enable the local Postgres integration:

```bash
export MCP_POSTGRES_ENABLED=true
export MCP_POSTGRES_DSN="postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable"
```

The Postgres tools are:

- `postgres_health`
- `postgres_list_schemas`
- `postgres_list_tables`
- `postgres_describe_table`
- `postgres_query`

`postgres_query` is intentionally read-only. It only accepts `SELECT`, `WITH`, and `EXPLAIN` statements, wraps results in a bounded `LIMIT`, uses a read-only transaction, and applies a statement timeout.

By default, the Postgres integration also validates connectivity during server startup so broken credentials or a down database fail fast.

## Production baseline

This scaffold now assumes a safer operating model:

- external integrations are disabled by default
- Postgres is disabled by default until a DSN is configured
- enabling GitHub or Slack without tokens fails at startup
- enabling Postgres without a DSN fails at startup
- workspace access is rooted to one configured directory
- hidden files can be excluded by default
- read and listing limits are configurable
- the server exposes health and registration metadata

## Architecture

Each integration exposes a class with a `register(mcp, context)` method.

- `config.py` loads environment settings
- `registry.py` decides which integrations are enabled
- `server.py` creates one `FastMCP` app and registers integrations
- `shared/` holds reusable helpers
- `integrations/<name>/` keeps API clients and MCP tools together

## Adding a new integration

1. Create `src/app/integrations/<name>/`.
2. Add `client.py`, `tools.py`, and `integration.py`.
3. Implement the integration class using the shared `Integration` protocol.
4. Register it in `src/app/registry.py`.
5. Add any new config fields to `src/app/config.py` and `.env.example`.

## Notes

- The workspace integration is the default practical starting point.
- The GitHub and Slack clients show the shape of external integrations, not a fully exhaustive API wrapper.
- Use Python 3.11+ for this project. The local default `python3` on some systems may still point to an older interpreter.
- A minimal [Dockerfile](/Users/sandeepdiddi/Documents/New%20project/Dockerfile) is included for containerized deployment.
