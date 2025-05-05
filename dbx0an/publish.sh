#!/bin/bash

# Set default commit message if none is provided
COMMIT_MSG=${1:-"Update via publish.sh"}

# Build site and push changes
hugo && \
git add -A && \
git commit -m "$COMMIT_MSG" && \
git push && \
cd public && \
git add -A && \
git commit -m "$COMMIT_MSG" && \
git push && \
cd ..

