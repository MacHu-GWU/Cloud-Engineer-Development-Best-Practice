# -*- coding: utf-8 -*-

from fabric2 import Connection
from invoke import Result
from pathlib_mate import PathCls as Path

_ = Result

HOST = "ec2-54-165-167-139.compute-1.amazonaws.com"
USER = "ec2-user"
PEM_PATH = Path.home().append_parts("ec2-pem", "eq-sanhe-dev.pem").abspath

HERE = Path(__file__).parent

# open a ssh session and close automatically
with Connection(host=HOST, user=USER, connect_kwargs={"key_filename": [PEM_PATH, ]}) as conn:
    # run shell script on remote
    conn.put(Path(HERE, "yum-install.sh"), "/tmp/yum-install.sh")
    conn.sudo('bash /tmp/yum-install.sh')
    conn.run('which git')

    # run python script on remote
    conn.put(Path(HERE, "download_artifacts.py"), "/tmp/download_artifacts.py")
    conn.run('python /tmp/download_artifacts.py') # standard out are captured at end of the command, it is not returned interactively
