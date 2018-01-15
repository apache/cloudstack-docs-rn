.. Licensed to the Apache Software Foundation (ASF) under one
   or more contributor license agreements.  See the NOTICE file
   distributed with this work for additional information#
   regarding copyright ownership.  The ASF licenses this file
   to you under the Apache License, Version 2.0 (the
   "License"); you may not use this file except in compliance
   with the License.  You may obtain a copy of the License at
   http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing,
   software distributed under the License is distributed on an
   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
   KIND, either express or implied.  See the License for the
   specific language governing permissions and limitations
   under the License.


Validate |version| source code tarball
======================================

#. Perform the following to verify the artifacts:

   #. (optional) Install GPG keys if needed:

      .. sourcecode:: bash
      
         $ sudo apt-get install gpg

   #. Import the GPG keys stored in the source distribution's KEYS file

      .. sourcecode:: bash

         $ gpg --import KEYS

      Alternatively, download the signing keys, the IDs found in the
      KEYS file, individually by using a keyserver.

      For example:

      .. sourcecode:: bash

         $ gpg --recv-keys CC56CEA8

   #. Verify signatures and hash files:

      .. sourcecode:: bash

         $ gpg --verify apache-cloudstack-4.11-src.tar.bz2.asc
         $ gpg --print-md MD5 apache-cloudstack-4.11-src.tar.bz2 | diff - apache-cloudstack-4.11-src.tar.bz2.md5
         $ gpg --print-md SHA512 apache-cloudstack-4.11-src.tar.bz2 | diff - apache-cloudstack-4.11-src.tar.bz2.sha

      Each of these commands should return no output. Any output from
      them implies that there is a difference between the hash you
      generated locally and the hash that has been pulled from the
      server.

   #. Get the commit hash from the VOTE email.

      For example: ``1b8a532ba52127f388847690df70e65c6b46f4d4``. The
      value changes between releases.

   #. Create two new temporary directories:

      .. sourcecode:: bash

         $ mkdir /tmp/cloudstack/git
         $ mkdir /tmp/cloudstack/tree

   #. Check out the |version| branch:

      .. sourcecode:: bash

         $ git clone https://git-wip-us.apache.org/repos/asf/cloudstack.git /tmp/cloudstack/git
         $ cd /tmp/cloudstack/git
         $ git archive --format=tar --prefix=/tmp/cloudstack/tree/ <commit-hash> | tar Pxf -

   #. Unpack the release artifact:

      .. sourcecode:: bash

         $ cd /tmp/cloudstack
         $ tar xvfj apache-cloudstack-4.10-src.tar.bz2

   #. Compare the contents of the release artifact with the contents
      pulled from the repo:

      .. sourcecode:: bash

         $ diff -r /tmp/cloudstack/apache-cloudstack-4.11-src /tmp/cloudstack/tree

      Ensure that content is the same.

   #. Verify the Code License Headers:

      .. sourcecode:: bash

         $ cd /tmp/cloudstack/apache-cloudstack-4.11-src
         $ mvn --projects='org.apache.cloudstack:cloudstack' org.apache.rat:apache-rat-plugin:0.8:check

      The build fails if any non-compliant files are present that are
      not specifically excluded from the ASF license header requirement.
      You can optionally review the target/rat.txt file after the run
      completes. Passing the build implies that RAT certifies that the
      files are compliant and this test is passed.
