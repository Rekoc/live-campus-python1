
# Create a new local repo (has to be pushed to be on the repo)
git init

# Add remote
git remove add <remote name (origin in general)> <repo URL>

# Clone locally the repo
git clone <URL repo> <directory>

# Add file/folder on your repo
git add <files/folders, ...>

# Remove file from your repo
git rm <files/folders, ...>

# Commit(locally) your code's change
git commit -m "<Comment>" <files to commit, ...>

# Push your commits on the repo
git push <remote name> <branch name>

# Update all branchs and remote
git fetch --all


# Crate branch (has to be pushed)
git checkout -b <branch name>

# Remove update made on file
git checkout <file's name>

# Switch branch
git switch <branch name>

# Merge two branches together
git merge <branch to merge with>