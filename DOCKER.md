# Docker

Install on linux [tutorial](https://docs.docker.com/engine/install/ubuntu/)
Install on windows [tutorial](https://docs.docker.com/docker-for-windows/install/)

## Build

    docker build -f /path/to/a/Dockerfile .

    -f - Point to dockerfile if not in current folder
    -t - Add tag
    -o - Output destination

## Run

docker run -d -p 80:80 docker/getting-started

    -d -  Run in the background
    -p 80:80 - Map port 80 of the host to port 80 in the container
    docker/getting-started - Image to use

    -i - Keep STDIN open even if not attached
    --expose - Expose a port or a range of ports
    -h - Container host name

## DOCKERFILE

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

## VS Code

Action: Add docker compose files...

## .dockerignore

    # Ignore everything
    **

    # Allow files and directories
    !/file.txt
    !/src/**

    # Ignore unnecessary files inside allowed directories
    # This should go after the allowed directories
    **/*~
    **/*.log
    **/.DS_Store
    **/Thumbs.db

    */temp* Exclude files and directories whose names start with temp in any immediate subdirectory of the root. For example, the plain file /somedir/temporary.txt is excluded, as is the directory /somedir/temp.

    temp? Exclude files and directories in the root directory whose names are a one-character extension of temp. For example, /tempa and /tempb are excluded.

## Misc

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
