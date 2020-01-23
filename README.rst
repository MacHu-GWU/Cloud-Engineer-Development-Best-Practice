Cloud Engineer Development Best Practice
==============================================================================



``Typing Command`` vs ``Writing Codes`` Development Pattern
------------------------------------------------------------------------------

what is ``Typing Command`` pattern:

.. code-block:: bash

    $ sudo yum -y install this
    $ sudo yum -y install that
    $ vim this
    $ ...

what is ``Writing Codes`` pattern:

.. code-block:: bash

    #!/bin/bash
    # content of my-script.sh
    yum -y install this
    yum -y install that
    python update_config.py $HOME/oracle-config.cfg ORACLE_HOME "/usr/lib/oracle"
    ...

then:

.. code-block:: bash

    bash my-script.sh

**Disadvantage of Typing Command**:

1. hard to type long command. one typo, you have to start over.
2. hard to repeat it again or on different machine.
3. unable to share knowledge with others.
4. no version control ...
5. what if you want to perform more complex works ...

Advantage of Typing Command:

1. interactive
2. fast for test

Conclusion:

1. do ``Typing Command`` when you are doing POC.
2. do ``Writing Codes`` for your development.


Problems with ``Writing Codes`` Pattern
------------------------------------------------------------------------------

1. Remote server doesn't have GUI or IDE for writing codes.
2. master VIM is hard.
3. Even if you are a VIM artist, configure VIM on every server you are working on is hard.
4. **Development on local, execute on remote is incontinent**.


Doing Development for Remote Server the Right Way
------------------------------------------------------------------------------

1. Setup development environment once on your local machine only once.
2. Scripting made easy, writing codes on your local, execute it on remote.
3. Forget about grep awk sed, leverage advance feature of Python, doing any manipulation you want.
4. More goodies.


Reference
------------------------------------------------------------------------------

- http://docs.fabfile.org/en/2.5/getting-started.html
- http://docs.pyinvoke.org/en/stable/getting-started.html
- https://fabric-patchwork.readthedocs.io/en/latest/
