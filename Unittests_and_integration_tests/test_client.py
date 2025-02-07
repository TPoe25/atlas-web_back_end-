#!/usr/bin/env python3
"""Unit tests for client.py"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("microsoft", {"repos_url": "https://api.github.com/orgs/microsoft/repos"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected, mock_get_json):
        """Test GithubOrgClient.org method"""
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test _public_repos_url property"""
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/test/repos"}
        client = GithubOrgClient("test")
        self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/test/repos")

    @patch("client.get_json")
    @patch("client.GithubOrgClient._public_repos_url", new_callable=PropertyMock)
    def test_repos_payload(self, mock_public_repos_url, mock_get_json):
        """Test repos_payload"""
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_public_repos_url.return_value = "https://api.github.com/orgs/test/repos"
        mock_get_json.return_value = test_payload
        client = GithubOrgClient("test")
        self.assertEqual(client.repos_payload, test_payload)
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/test/repos")

if __name__ == "__main__":
    unittest.main()
