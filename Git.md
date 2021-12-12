# Git

## Setup

    git config --global user.name "Your name"
    git config --global user.email "yourname@provider.com"

## Delete last commit
git reset --hard <commit-id>
git push origin -f

## .gitignore

Create file called `.gitignore` on root. Only code is supposed to be on git. No binaries, libraries etc.
You can define what files will be send to git and what files will be ignored

    # Comments must beginn on new line !!!

    # Ignore one file
    readme.txt

    # Ignore only in curent folder
    /readme.txt

    # Ignore folder
    output/

    # ignore all *java files
    *.java

    # All files in directory
    abc/**

    # Zero or more directories
    a/**/b

    # Do not ignore
    !readme.txt

## Start new repo

Create repo for example on github

Init stage and commit can be done from IDE with actions

    # Create .git folder
    git init

    # Stage all
    git stage -A

    # Commit all
    git commit -a -m "new message"

    git remote add origin www.github...repopath

## Download existing repo

    git clone repo-url

## Misc

    # Print what is changed
    git status

    # Stage
    git add add.js

    # Reset to commit and keep changes in code in stage
    git reset --soft 852309

    # Reset 5 commits back
    git reset --soft 'HEAD{5}'

    # Reset to commit and delete changes
    git reset --hard 852309

    # Create branch
    git branch dev

    # Move to branch
    git checkout dev

    # Merge branches (if join master with dev branch, first checkout back to master then)
    git merge dev

    # Delete branch locally
    git branch -d dev

    # Delete branch remotely
    git push --delete origin dev

## Clean all history (create, stage, commit, push)

Delete `.git` folder

    git init
    git add .
    git commit -m "Removed history, due to sensitive data"
    git remote add origin github.com:your-project/your-repo.git
    git push -u --force origin master

## Git hooks

First setup hooks path, because normal hooks are gitignored by default

    git config core.hooksPath git_hooks_path
