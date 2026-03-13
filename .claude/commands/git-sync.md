# /git-sync

Synchronize the workspace with the Git repository.

## Purpose

Prepare the workspace for commit and push all changes to the configured Git remote.

## Actions

1. Validate the workspace structure and ensure no temporary or unwanted files are present.
2. Confirm `.gitignore` rules are respected.
3. Stage all relevant files.

Run:

git add .

4. Create a commit message summarizing changes.

git commit -m "workspace update"

5. Push changes to the current branch.

git push

## Optional Enhancement

If the repository has not been initialized:

git init

If remote is not configured:

git remote add origin <repo-url>

Then push:

git push -u origin master
