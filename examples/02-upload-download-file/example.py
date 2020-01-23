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
    # upload file to remote
    conn.put(Path(HERE, "alice.json"), "/tmp/alice.json")

    # send command, see if the test.json file already on remote
    conn.run('cat /tmp/test.json') # type: Result

    # get file from remote
    conn.run('echo "{\\"name\\": \\"Bob\\"}" > /tmp/bob.json') # create a temp file on remote
    conn.get("/tmp/bob.json", Path(HERE, "bob.json")) # download file to local
