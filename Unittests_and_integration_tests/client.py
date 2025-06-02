#!/usr/bin/env python3
"""A GitHub organization client"""

from typing import List, Dict
from utils import get_json, access_nested_map, memoize


class GithubOrgClient:
    """A GitHub organization client"""
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        """Initialize the client"""
        self._org_name = org_name

    @memoize
    def org(self) -> Dict:
        """Fetch and cache organization data"""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -> str:
        """Retrieve the public repositories URL"""
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -> Dict:
        """Fetch and cache repositories data"""
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -> List[str]:
        """Return a list of public repositories, optionally filtered by license"""
        json_payload = self.repos_payload
        return [
            repo["name"] for repo in json_payload
            if license is None or self.has_license(repo, license)
        ]

    @staticmethod
    def has_license(repo: Dict, license_key: str) -> bool:
        """Check if a repository has a specific license"""
        assert license_key is not None, "license_key cannot be None"
        try:
            return access_nested_map(repo, ("license", "key")) == license_key
        except KeyError:
            return False
