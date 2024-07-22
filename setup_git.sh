#!/bin/bash

# Get the GitHub token from the environment variable
GITHUB_TOKEN=${GITHUB_TOKEN:?GITHUB_TOKEN environment variable not set}

# Set the repository URL with token
REPO_URL="https://${GITHUB_TOKEN}@github.com/username/repository.git"

# Update the remote URL
git remote set-url origin $REPO_URL

# Fetch from origin
git fetch -v -- origin
