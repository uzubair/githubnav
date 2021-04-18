from github import Github
from github.Repository import Repository
from github.Commit import Commit


class SearchService:
    """Interacts with Github to search for repositories and return
    formatted data."""

    def __init__(self, github_client: Github):
        self._github_client = github_client

    """
    Private methods
    """

    def _format_repo(self, repo: Repository):
        """Formats repository data"""
        commits = repo.get_commits()
        return {
            "url": repo.html_url,
            "name": repo.name,
            "owner": {
                "login": repo.owner.login,
                "url": repo.owner.html_url,
                "avatar_url": repo.owner.avatar_url,
            },
            "latest_commit": self._format_commit(commits[0]) if commits else {},
        }

    def _format_commit(self, commit: Commit):
        """Formats commit data"""
        return {
            "sha": commit.sha,
            "url": commit.html_url,
            "message": commit.commit.message,
            "author_name": commit.commit.author.name,
        }

    """
    Public methods
    """

    def search_repositories(self, query, limit):
        """Search for repositories and return formatted data."""
        repositories = self._github_client.search_repositories(
            query=query, **{'in': 'name'},
        )
        return [self._format_repo(repo) for repo in repositories[:limit]]
