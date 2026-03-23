from app.integrations.github import GitHubIntegration
from app.integrations.postgres import PostgresIntegration
from app.integrations.slack import SlackIntegration
from app.integrations.workspace import WorkspaceIntegration
from app.types import AppContext, Integration, IntegrationRegistration


def get_enabled_integrations(context: AppContext) -> list[Integration]:
    integrations: list[Integration] = []

    if context.settings.workspace_enabled:
        integrations.append(WorkspaceIntegration())

    if context.settings.postgres_enabled:
        integrations.append(PostgresIntegration())

    if context.settings.github_enabled:
        integrations.append(GitHubIntegration())

    if context.settings.slack_enabled:
        integrations.append(SlackIntegration())

    return integrations


def register_integrations(mcp: object, context: AppContext) -> list[IntegrationRegistration]:
    registered: list[IntegrationRegistration] = []

    for integration in get_enabled_integrations(context):
        registered.append(integration.register(mcp, context))

    return registered
