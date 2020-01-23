# -*- coding: utf-8 -*-

from fabric2 import Connection
from invoke import Result
from patchwork.transfers import rsync
from pathlib_mate import PathCls as Path

_ = Result

HOST = "ec2-54-165-167-139.compute-1.amazonaws.com"
USER = "ec2-user"
PEM_PATH = Path.home().append_parts("ec2-pem", "eq-sanhe-dev.pem").abspath

HERE = Path(__file__).parent

# open a ssh session and close automatically
with Connection(host=HOST, user=USER, connect_kwargs={"key_filename": [PEM_PATH, ]}) as conn:
    # sync folder from local to remote, like google drive
    rsync(conn, source=Path(HERE, "test-folder"), target="/tmp")
    conn.run('cat /tmp/test-folder/index.html')

    # sync folder from remote to local, like google drive
    conn.run('mkdir -p /tmp/test-folder-on-remote')
    conn.run('echo "<html>This is a folder from remote server</html>" > /tmp/test-folder-on-remote/index.html')
    rsync(conn, source=HERE, target="/tmp/test-folder-on-remote", remote_to_local=True)  # will be available in 1.0.2
    conn.local('cat {}'.format(HERE.append_parts("test-folder-on-remote", "index.html").abspath))
