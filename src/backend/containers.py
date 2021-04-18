""" Containers module will keep all of the application components and their dependencies """

from dependency_injector import containers, providers
from github import Github
from backend.services.search import SearchService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    github_client = providers.Factory(
        Github,
        login_or_token=config.github.api_key,
        timeout=config.github.request_timeout,
    )

    search_service = providers.Factory(SearchService, github_client=github_client)
