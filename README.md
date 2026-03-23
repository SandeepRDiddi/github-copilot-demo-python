# Python MCP Multi-Integration Scaffold

This project is a starter scaffold for running multiple integrations behind one Python MCP server.
It now includes a production-ready baseline with startup validation, operational metadata, and a first usable local integration so you can run it immediately against your workspace.

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
