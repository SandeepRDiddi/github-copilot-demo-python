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

Imagine an engineer gets a bug report:

`"Customer invoices are not showing in the app."`

Without a setup like this, the engineer usually has to:

- open the codebase and find where invoice data is loaded
- connect to Postgres manually
- inspect tables and schema
- run SQL queries to check whether the data exists
- compare the data with what the code expects

With this MCP server, the flow is simpler and faster:

1. The engineer asks the AI assistant to investigate why invoices are missing.
2. The AI uses the workspace tools to inspect the code that loads invoice data.
3. The AI uses the Postgres tools to safely inspect tables and run read-only queries.
4. The MCP server applies limits, validation, and safe access rules before any result is returned.
5. The AI combines the code context and database results into a clear explanation.

Example outcome:

The AI might discover that the invoices do exist in Postgres, but the app only shows invoices where `status = 'active'`, while this customer's records are marked `archived`.

That means the engineer gets the likely root cause quickly, without manually jumping between multiple systems.

This is why the project exists:

- engineers spend less time gathering context
- investigations become faster and more repeatable
- database access is safer for AI-assisted workflows
- teams get one reusable platform instead of one-off scripts

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
