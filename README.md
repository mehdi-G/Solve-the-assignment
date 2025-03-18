# Solve-the-assignment
Python script to validate GitHub API tokens, retrieve developer information, and identify token scopes. Includes a bonus tool for GitLab API tokens.
# Solve-the-assignment

This repository contains a Python script that solves the GitGuardian internship assignment. The script can validate GitHub and GitLab API tokens and retrieve developer information associated with those tokens.

## Features

- **GitHub API Token Validation**: Takes a GitHub API token as input and checks if it is valid.
- **GitLab API Token Validation**: Similarly, validates GitLab API tokens.
- **Developer Information Retrieval**: Identifies the corresponding developer and fetches relevant information from GitHub or GitLab.
- **Token Scope Detection**: Retrieves the scope of the provided API token (GitHub/GitLab).

## Requirements

- Python 3.x
- Requests library (can be installed via `pip`)

## Installation

To use the script, follow these steps:

Run the Python script with the appropriate command:
 -For GitHub API token validation:
      python ./easy.py github <your-github-api-token>
  -For GitLab API token validation:
      python ./easy.py gitlab <your-gitlab-api-token>
