""" Views module """
from flask import request, render_template
from dependency_injector.wiring import inject, Provide

from .containers import Container
from backend.services.search import SearchService


@inject
def index(
    search_service: SearchService = Provide[Container.search_service],
    query: str = Provide[Container.config.default.query],
    limit: int = Provide[Container.config.default.limit],
):
    query = request.args.get("query", query)
    limit = request.args.get("limit", limit, int)

    repositories = search_service.search_repositories(query, limit)
    return render_template(
        "index.html", query=query, limit=limit, repositories=repositories
    )
