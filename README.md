Python Env Variable Loader
==========================

This program takes a list of key value pairs in a configuration file
and inserts them into the current shell environment.

Usage:

From any bash shell:

    $ eval $(./load_env.py)

You can also add the following to your .bashrc (where /path is to the directory containing your config files and python code):

    cd /path && eval $(./load_env) && cd


Assumptions
===========
There is file in the current directory named "myconfigfile.txt"
This file has only key value pairs in a format like this:

    xyzFirstName    = Frank
    xyzLastName     = Anderson
    xyzEmail        = Frank_Anderson@xyz.com

