# -*- coding: utf-8 -*-

from fabric2 import Connection
from invoke import Result
from pathlib_mate import PathCls as Path

_ = Result

HOST = "ec2-54-165-167-139.compute-1.amazonaws.com"
USER = "ec2-user"
PEM_PATH = Path.home().append_parts("ec2-pem", "eq-sanhe-dev.pem").abspath

# open a ssh session and close automatically
with Connection(host=HOST, user=USER, connect_kwargs={"key_filename": [PEM_PATH, ]}) as conn:
    # example1: send command, create a html file index.html
    # conn.run('echo "<html>Hello World</html>" > /tmp/index.html') # type: Result
    # conn.run('cat /tmp/index.html') # type: Result

    # example2: process standard output afterwards
    result = conn.run('ls /', hide=True)  # type: Result
    print(result.stdout)  # access the standard output, capture those strings and process it in Python
    # print(result.stderr)
    # print(result.encoding)
    # print(result.command)
    # print(result.shell) # the shell you use to execute this command
    # print(result.env) # environment variable you want to use for this run
    print(result.exited)
