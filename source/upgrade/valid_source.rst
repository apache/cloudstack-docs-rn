Validate |version| source code tarball
--------------------------------------

#. 

   Perform the following to verify the artifacts:

   #. 

      (optional) Install GPG keys if needed:

      .. sourcecode:: bash
      
          $ sudo apt-get install gpg

   #. 

      Import the GPG keys stored in the source distribution's KEYS file

      .. sourcecode:: bash

          $ gpg --import KEYS

      Alternatively, download the signing keys, the IDs found in the
      KEYS file, individually by using a keyserver.

      For example:

      .. sourcecode:: bash

          $ gpg --recv-keys CC56CEA8

   #. 

      Verify signatures and hash files:

      .. sourcecode:: bash

          $ gpg --verify apache-cloudstack-4.4-src.tar.bz2.asc
          $ gpg --print-md MD5 apache-cloudstack-4.4-src.tar.bz2 | diff - apache-cloudstack-4.4-src.tar.bz2.md5
          $ gpg --print-md SHA512 apache-cloudstack-4.4-src.tar.bz2 | diff - apache-cloudstack-4.4-src.tar.bz2.sha

      Each of these commands should return no output. Any output from
      them implies that there is a difference between the hash you
      generated locally and the hash that has been pulled from the
      server.

   #. 

      Get the commit hash from the VOTE email.

      For example: ``4cd60f3d1683a3445c3248f48ae064fb573db2a1``. The
      value changes between releases.

   #. 

      Create two new temporary directories:

      .. sourcecode:: bash

          $ mkdir /tmp/cloudstack/git
          $ mkdir /tmp/cloudstack/tree

   #. 

      Check out the |version| branch:

      .. sourcecode:: bash

          $ git clone https://git-wip-us.apache.org/repos/asf/cloudstack.git /tmp/cloudstack/git
          $ cd /tmp/cloudstack/git
          $ git archive --format=tar --prefix=/tmp/cloudstack/tree/ <commit-hash> | tar Pxf -

   #. 

      Unpack the release artifact:

      .. sourcecode:: bash

          $ cd /tmp/cloudstack
          $ tar xvfj apache-cloudstack-4.4-src.tar.bz2

   #. 

      Compare the contents of the release artifact with the contents
      pulled from the repo:

      .. sourcecode:: bash

          $ diff -r /tmp/cloudstack/apache-cloudstack-4.4-src /tmp/cloudstack/tree

      Ensure that content is the same.

   #. 

      Verify the Code License Headers:

      .. sourcecode:: bash

          $ cd /tmp/cloudstack/apache-cloudstack-4.4-src
          $ mvn --projects='org.apache.cloudstack:cloudstack' org.apache.rat:apache-rat-plugin:0.8:check

      The build fails if any non-compliant files are present that are
      not specifically excluded from the ASF license header requirement.
      You can optionally review the target/rat.txt file after the run
      completes. Passing the build implies that RAT certifies that the
      files are compliant and this test is passed.
