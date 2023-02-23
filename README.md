# Docs, snippets

This is documentation for everything I ever needed for programming...

Describes operating system helpers, syntax for terminals, git, docker etc.

There is a folder languages, with language specific commands, snippets, examples etc...

It's open of course, you can use it, share it and edit it...

## TOC

<!-- TOC -->
- [Docs, snippets](#docs-snippets)
  - [TOC](#toc)
  - [OS](#os)
    - [Linux](#linux)
      - [Distros](#distros)
      - [Packages](#packages)
      - [Essentials](#essentials)
      - [Folder structure](#folder-structure)
      - [Do after every fresh install](#do-after-every-fresh-install)
  - [Terminals](#terminals)
    - [Linux](#linux-1)
      - [Bash](#bash)
    - [Windows](#windows)
      - [PowerShell](#powershell)
      - [Cmd](#cmd)
  - [Git](#git)
    - [Glossary](#glossary)
    - [Essentials](#essentials-1)
    - [Misc](#misc)
    - [.gitignore](#gitignore)
    - [Git hooks](#git-hooks)
  - [Docker](#docker)
    - [Installation](#installation)
    - [Commands](#commands)
    - [DOCKERFILE](#dockerfile)
  - [Misc](#misc-1)
    - [LDAP](#ldap)
<!-- TOC -->

## OS

### Linux

#### Distros

Ubuntu: Most used as desktop distro
Alpine: Tiny, used for small docker containers
RHEL (RedHat): Used in corporat production. Known for stability

Other: Arch, CentOS

#### Packages
Debian based distros like ubuntu support `apt` and `apt-get`. As a user preffer `apt` as it's more higher level

```shell
sudo apt update  # Update all packages

sudo apt edit-sources  # Change repositories from where you can download packages

apt search python  # List possible packages containing defined name

sudo apt update  # Upgrade all packages

sudo apt install python3.5-dev  # Install package

apt show package_name  # Show details about package
```

#### Essentials

Run on bash startup - `~/.bashrc`
Run on every startup - `~/.profile`

#### Folder structure
TODO add folders description, fstab description etc.

#### Do after every fresh install

```shell
sudo apt-get install build-essential  # Install all building compilers (g++ error etc...)

sudo apt-get install nautilus-open-terminal  # Open terminal in current folder
```

## Terminals

### Linux

**cat**

Stands for concatenate. If just one file, it displays the content
Append content of file to other file

	cat test >> test1

Overwrite content of file with other file

	cat test > test1


**env**

List environment variables

    env

**which**

Print where command binaries are located

    which python

**sed**

Searching, find and replace, insertion or deletion without opening file
The below simple sed command replaces the word “unix” with “linux” in the file.

	sed 's/unix/linux/' geekfile.txt

#### Bash
Restart terminal

    bash --login

### Windows
Open bat script and see result in terminal (keeping output after finishing script)

    cmd /k my_script.bat

**netstat**
count number of localhost connections

    netstat -n | findstr 127.0.0.1 | find /v /c ""

#### PowerShell
**Filter strings**

	echo $Env:PATH | Select-String  substring

Inverse filter

    echo $Env:PATH | Select-String substring -NotMatch

**Print content**

	Get-Content file


**Print env var**

	echo $Env:PATH

#### Cmd

Where command binaries are located

    where python

## Git

### Glossary
- origin - Remote url shorthand
- merge - Add changes from some branch into another in new commit
- rebase - Add changes from some branch via changing history (no new commit) !!!Use only when only you are using the branch. If already on remote, need force push!!!
- fast-forward - It's possible to do merge without new commit (only possible if there are no changes on the other branch)

### Essentials
```bash
    # Create .git folder
    git init

    # Stage all
    git stage -A

    # Commit all
    git commit -a -m "new message"

    git remote add origin www.github...repo-path

  # Download existing repo

    git clone repo-url

    # Configuration

    git config --global user.name "Your name"
    git config --global user.email "yourname@provider.com"

    git status  # Print what is changed

    git add add.js  # Stage

    git reset --soft 852309  # Reset to commit and keep changes in code in stage

    git reset --soft 'HEAD{5}'  # Reset 5 commits back

    git reset --hard 852309  # Reset to commit and delete changes

    git branch dev  # Create branch

    git checkout dev  # Move to branch

    git merge dev  # Merge branches (if join master with dev branch, first checkout back to master then)

    git branch -d dev  # Delete branch locally

    git push --delete origin dev  # Delete branch remotely

    git remote -v  # Verify whether origin and upstream both configured

```

### Misc

**Clean all history (create, stage, commit, push)**

Delete `.git` folder and

```bash
git init
git add .
git commit -m "Removed history, due to sensitive data"
git remote add origin github.com:your-project/your-repo.git
git push -u --force origin master
```

**How to contribute on gitHub**

Create fork in GitHub, clone forked repository, add upstream with

    git remote add upstream original-repo-url

Update upstream repo in your IDE, create new branch, push changes to the fork, then create pull request in GitHub, resolve comments and if it's accepted, delete branch from local repo.

**Delete last commit**

    git reset --hard <commit-id>
    git push origin -f


**Delete tag**

```bash
# Locally
git tag -d v1.0

# Remote
git push --delete origin tagname
```

### .gitignore

Create file called `.gitignore` on root. Only code is supposed to be on git. No binaries, libraries etc.
You can define what files will be sent to git and what files will be ignored

```gitignore
    # Comments must begin on new line !!!

    # Ignore one file
    readme.txt

    # Ignore only in current folder
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
```

### Git hooks

First setup hooks path, because normal hooks are gitignored by default

    git config core.hooksPath git_hooks_path


## Docker
### Installation

Install on linux [tutorial](https://docs.docker.com/engine/install/ubuntu/)
Install on windows [tutorial](https://docs.docker.com/docker-for-windows/install/)

### Commands
**Build**

    docker build -f /path/to/a/Dockerfile .

        -f - Point to dockerfile if not in current folder
        -t - Add tag
        -o - Output destination

**Run**

    docker run -d -p 80:80 docker/getting-started
    
        -d -  Run in the background
        -p 80:80 - Map port 80 of the host to port 80 in the container
        docker/getting-started - Image to use
    
        -i - Keep STDIN open even if not attached
        --expose - Expose a port or a range of ports
        -h - Container host name

**Download image**

    docker pull alpine

**Misc**
```shell
# List all your containrers
docker ps

# Remove container with it's id from docker ps
docker rm a39c259df46

# List all images
docker images

# List all running container
docker container ls

# Delete image
docker rmi 60959f29de3a

# Example - run linux
docker run --interactive --tty ubuntu bash
# Then you can use host, ls...

# Example 2 = nginx
docker run --detach --publish 80:80 --name webserver nginx
# If open http://localhost in browser, you see nginx welcome

# Stop container
docker container stop webserver

# Push container to registry
    docker image tag rhel-httpd:latest registry-host:5000/myadmin/rhel-httpd:latest
    docker image push registry-host:5000/myadmin/rhel-httpd:latest
```

### DOCKERFILE

```dockerfile
    # This is comment ignored by docker.  # Inline comment also possible

    FROM - Starting container <image>[:tag]. E.g alpine:3.4,
    RUN - Run command such as apt-get install or pip install

    # Combine RUNs into one
        RUN apk update && \
            apk add curl && \
            apk add vim && \
    ENV PG_MAJOR=9.3  # Add environment variable
    EXPOSE 80/tcp # Allow to access this port
    CMD - Run this script after docker run
    ENTRYPOINT - Similar to CMD - run this script after docker run - If user should not change the script (arguments)

    COPY - (Preferred) Add directories/files to your image
    ADD - Add directories/files to your image
```


## Misc
### LDAP
```python
from ldap3 import Server, Connection, SAFE_SYNC

server = Server('rb-gc-lb.bosch.com', port=3268)
conn = Connection(server, 'psx6fe@bosch.com', '!nPm?XyS2NowX2', client_strategy=SAFE_SYNC, auto_bind=True, auto_referrals=False)

# In search function, there are two important positional params.
# First define space to return the results and second means filter, that is applied on searched results
# Find Group by CN
status, result, response, _ = conn.search('DC=bosch,DC=com', '(CN=Bj_PS_dux_streaming_c-schicht_editor)')

# Find user
status, result, response, _ = conn.search('DC=bosch,DC=com', '(sAMAccountName=psx6fe)')

# Find type of records e.g. user
status, result, response, _ = conn.search('DC=bosch,DC=com', '(Objectclass=User)')

# Using wildcard to get all the records
status, result, response, _ = conn.search('DC=bosch,DC=com', '(sAMAccountName=*)')
```
