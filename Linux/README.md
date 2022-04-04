# Linux

## Bash essentials

    # Update all packages
    sudo apt-get update

    # Print environment path
    echo $PATH

    # Restart terminal
    bash --login

    # Install package
    sudo apt-get install python3.5-dev

    # Change pythonpath
    nano ~/.bashrc

    # With opened file add line and save and exit
    export PYTHONPATH="/Users/my_user/code"

    # Print python path
    echo $PYTHONPATH

    # Where is something
    where python2.7

    # Install all building compilers (g++ error etc...)
    sudo apt-get install build-essential
