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


Upgrade Instructions for 4.3
============================

This section contains upgrade instructions from prior versions of
CloudStack to Apache CloudStack 4.3. We include instructions on
upgrading to Apache CloudStack from pre-Apache versions of Citrix
CloudStack (last version prior to Apache is 3.0.2) and from the releases
made while CloudStack was in the Apache Incubator.

If you run into any issues during upgrades, please feel free to ask
questions on users@cloudstack.apache.org or dev@cloudstack.apache.org.

Validate 4.3 source code tarball
--------------------------------

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

   #. Get files, refer to `CloudStack Download Archive Page <http://cloudstack.apache.org/archives.html>`_ for source package download.
      
      .. sourcecode:: bash
      
         $ wget http://archive.apache.org/dist/cloudstack/releases/4.3.1/apache-cloudstack-4.3.1-src.tar.bz2
         $ wget http://archive.apache.org/dist/cloudstack/releases/4.3.1/apache-cloudstack-4.3.1-src.tar.bz2.asc
         $ wget http://archive.apache.org/dist/cloudstack/releases/4.3.1/apache-cloudstack-4.3.1-src.tar.bz2.md5

   #. 

      Verify signatures and hash files:

      .. sourcecode:: bash

          $ gpg --verify apache-cloudstack-4.3.1-src.tar.bz2.asc
          $ gpg --print-md MD5 apache-cloudstack-4.3.1-src.tar.bz2 | diff - apache-cloudstack-4.3.1-src.tar.bz2.md5
          $ gpg --print-md SHA512 apache-cloudstack-4.3.1-src.tar.bz2 | diff - apache-cloudstack-4.3.1-src.tar.bz2.sha

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

      Check out the 4.3 branch:

      .. sourcecode:: bash

          $ git clone https://git-wip-us.apache.org/repos/asf/cloudstack.git /tmp/cloudstack/git
          $ cd /tmp/cloudstack/git
          $ git archive --format=tar --prefix=/tmp/cloudstack/tree/ <commit-hash> | tar Pxf -

   #. 

      Unpack the release artifact:

      .. sourcecode:: bash

          $ cd /tmp/cloudstack
          $ tar xvfj apache-cloudstack-4.3-src.tar.bz2

   #. 

      Compare the contents of the release artifact with the contents
      pulled from the repo:

      .. sourcecode:: bash

          $ diff -r /tmp/cloudstack/apache-cloudstack-4.3-src /tmp/cloudstack/tree

      Ensure that content is the same.

   #. 

      Verify the Code License Headers:

      .. sourcecode:: bash

          $ cd /tmp/cloudstack/apache-cloudstack-4.3-src
          $ mvn --projects='org.apache.cloudstack:cloudstack' org.apache.rat:apache-rat-plugin:0.8:check

      The build fails if any non-compliant files are present that are
      not specifically excluded from the ASF license header requirement.
      You can optionally review the target/rat.txt file after the run
      completes. Passing the build implies that RAT certifies that the
      files are compliant and this test is passed.


Upgrade from 4.3.1 to 4.3.2
---------------------------

This section will guide you from CloudStack 4.3.1 to CloudStack 4.3.2.

Any steps that are hypervisor-specific will be called out with a note.

We recommend reading through this section once or twice before beginning
your upgrade procedure, and working through it on a test system before
working on a production system.

.. note:: The following upgrade instructions should be performed regardless of hypervisor type.

#.

   Most users of CloudStack manage the installation and upgrades of
   CloudStack with one of Linux's predominant package systems, RPM or
   APT. This guide assumes you'll be using RPM and Yum (for Red Hat
   Enterprise Linux or CentOS), or APT and Debian packages (for Ubuntu).

#.

   Create RPM or Debian packages (as appropriate) and a repository from
   the 4.3 source, or check the Apache CloudStack downloads page at
   `http://cloudstack.apache.org/downloads.html <http://cloudstack.apache.org/downloads.html>`_
   for package repositories supplied by community members.

   Instructions for creating packages from the CloudStack source are in
   the `CloudStack Installation Guide`_.

#.

   Stop your management server or servers. Run this on all management
   server hosts:

   .. sourcecode:: bash

       $ sudo service cloudstack-management stop

#.

   If you are running a usage server or usage servers, stop those as
   well:

   .. sourcecode:: bash

       $ sudo service cloudstack-usage stop

#.

   Make a backup of your MySQL database. If you run into any issues or
   need to roll back the upgrade, this will assist in debugging or
   restoring your existing environment. You'll be prompted for your
   password.

   .. sourcecode:: bash

       $ mysqldump -u root -p cloud > cloudstack-backup.sql
       $ mysqldump -u root -p cloud_usage > cloud_usage-backup.sql

#.

   (KVM Only) If primary storage of type local storage is in use, the
   path for this storage needs to be verified to ensure it passes new
   validation. Check local storage by querying the cloud.storage\_pool
   table:

   .. sourcecode:: bash

       $ mysql -u cloud -p -e "select id,name,path from cloud.storage_pool where pool_type='Filesystem'"

   If local storage paths are found to have a trailing forward slash,
   remove it:

   .. sourcecode:: bash

       $ mysql -u cloud -p -e 'update cloud.storage_pool set path="/var/lib/libvirt/images" where path="/var/lib/libvirt/images/"';

#.

   If you are using Ubuntu, follow this procedure to upgrade your
   packages. If not, skip to step *upgrade-rpm-packages-4.3*.

   .. note::
      **Community Packages:** This section assumes you're using the community supplied packages for CloudStack.
      If you've created your own packages and APT repository, substitute your own URL for the ones used in these examples.

   #.

      Now update your apt package list:

      .. sourcecode:: bash

          $ sudo apt-get update

   #.

      Now that you have the repository configured, it's time to upgrade
      the ``cloudstack-management`` package.

      .. sourcecode:: bash

          $ sudo apt-get upgrade cloudstack-management
          $ sudo apt-get upgrade cloudstack-usage

   #.

      Now it's time to start the management server

      .. sourcecode:: bash

          $ sudo service cloudstack-management start

   #.

      If you use it, start the usage server

      .. sourcecode:: bash

          $ sudo service cloudstack-usage start

#.

   (VMware only) Additional steps are required for each VMware cluster.
   These steps will not affect running guests in the cloud. These steps
   are required only for clouds using VMware clusters:

   #.

      Stop the Management Server:

      .. sourcecode:: bash

          $ sudo service cloudstack-management stop

   #.

      Generate the encrypted equivalent of your vCenter password:

      .. sourcecode:: bash

          $ java -classpath /usr/share/cloudstack-common/lib/jasypt-1.9.0.jar org.jasypt.intf.cli.JasyptPBEStringEncryptionCLI encrypt.sh input="_your_vCenter_password_" password="`cat /etc/cloudstack/management/key`" verbose=false

      Store the output from this step, we need to add this in
      cluster\_details table and vmware\_data\_center tables in place of
      the plain text password

   #.

      Find the ID of the row of cluster\_details table that you have to
      update:

      .. sourcecode:: bash

          $ mysql -u <username> -p<password>

      .. sourcecode:: bash

          select * from cloud.cluster_details;

   #.

      Update the plain text password with the encrypted one

      .. sourcecode:: bash

          update cloud.cluster_details set value = '_ciphertext_from_step_1_' where id = _id_from_step_2_;

   #.

      Confirm that the table is updated:

      .. sourcecode:: bash

          select * from cloud.cluster_details;

   #.

      Find the ID of the correct row of vmware\_data\_center that you
      want to update

      .. sourcecode:: bash

          select * from cloud.vmware_data_center;

   #.

      update the plain text password with the encrypted one:

      .. sourcecode:: bash

          update cloud.vmware_data_center set password = '_ciphertext_from_step_1_' where id = _id_from_step_5_;

   #.

      Confirm that the table is updated:

      .. sourcecode:: bash

          select * from cloud.vmware_data_center;

   #.

      Start the CloudStack Management server

      .. sourcecode:: bash

          $ sudo service cloudstack-management start

#.

   (KVM only) Additional steps are required for each KVM host. These
   steps will not affect running guests in the cloud. These steps are
   required only for clouds using KVM as hosts and only on the KVM
   hosts.

   #.

      Configure the CloudStack apt repository as detailed above.

   #.

      Stop the running agent.

      .. sourcecode:: bash

          $ sudo service cloudstack-agent stop

   #.

      Update the agent software.

      .. sourcecode:: bash

          $ sudo apt-get update cloudstack-agent

   #.

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. sourcecode:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #.

      Start the agent.

      .. sourcecode:: bash

          $ sudo service cloudstack-agent start

#.

   If you are using CentOS or RHEL, follow this procedure to upgrade
   your packages. If not, skip to step *restart-system-vms-4.3*.

   .. note::
      **Community Packages:** This section assumes you're using the community supplied packages for CloudStack.
      If you've created your own packages and yum repository, substitute your own URL for the ones used in these examples.

   #.

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package by upgrading the older
      ``cloudstack-management`` package.

      .. sourcecode:: bash

          $ sudo yum upgrade cloudstack-management
          $ sudo yum upgrade cloudstack-usage

   #.

      Now it's time to restart the management server

      .. sourcecode:: bash

          $ sudo service cloudstack-management start

   #.

      For KVM hosts, upgrade the ``cloudstack-agent`` package

      .. sourcecode:: bash

          $ sudo yum upgrade cloudstack-agent

   #.

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. sourcecode:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #.

      Restart the agent:

      .. sourcecode:: bash

          $ sudo service cloudstack-agent stop
          $ sudo killall jsvc
          $ sudo service cloudstack-agent start

#.

   Now it's time to restart the management server

   .. sourcecode:: bash

       $ sudo service cloudstack-management start

#.

   .. note:: **For Xen Hosts: Copy vhd-utils:** This step is only for CloudStack installs that are using Xen hosts.

   Copy the file ``vhd-utils`` to
   ``/usr/share/cloudstack-common/scripts/vm/hypervisor/xenserver``.

Upgrade from 4.3.0 to 4.3.1
---------------------------

This section will guide you from CloudStack 4.3.0 to CloudStack 4.3.1.

Any steps that are hypervisor-specific will be called out with a note.

We recommend reading through this section once or twice before beginning
your upgrade procedure, and working through it on a test system before
working on a production system.

.. note:: The following upgrade instructions should be performed regardless of hypervisor type.

#. 

   Most users of CloudStack manage the installation and upgrades of
   CloudStack with one of Linux's predominant package systems, RPM or
   APT. This guide assumes you'll be using RPM and Yum (for Red Hat
   Enterprise Linux or CentOS), or APT and Debian packages (for Ubuntu).

#. 

   Create RPM or Debian packages (as appropriate) and a repository from
   the 4.3 source, or check the Apache CloudStack downloads page at
   `http://cloudstack.apache.org/downloads.html <http://cloudstack.apache.org/downloads.html>`_
   for package repositories supplied by community members. 

   Instructions for creating packages from the CloudStack source are in
   the `CloudStack Installation Guide`_.

#. 

   Stop your management server or servers. Run this on all management
   server hosts:

   .. sourcecode:: bash

       $ sudo service cloudstack-management stop

#. 

   If you are running a usage server or usage servers, stop those as
   well:

   .. sourcecode:: bash

       $ sudo service cloudstack-usage stop

#. 

   Make a backup of your MySQL database. If you run into any issues or
   need to roll back the upgrade, this will assist in debugging or
   restoring your existing environment. You'll be prompted for your
   password.

   .. sourcecode:: bash

       $ mysqldump -u root -p cloud > cloudstack-backup.sql
       $ mysqldump -u root -p cloud_usage > cloud_usage-backup.sql

#. 

   (KVM Only) If primary storage of type local storage is in use, the
   path for this storage needs to be verified to ensure it passes new
   validation. Check local storage by querying the cloud.storage\_pool
   table:

   .. sourcecode:: bash

       $ mysql -u cloud -p -e "select id,name,path from cloud.storage_pool where pool_type='Filesystem'"

   If local storage paths are found to have a trailing forward slash,
   remove it:

   .. sourcecode:: bash

       $ mysql -u cloud -p -e 'update cloud.storage_pool set path="/var/lib/libvirt/images" where path="/var/lib/libvirt/images/"';

#. 

   If you are using Ubuntu, follow this procedure to upgrade your
   packages. If not, skip to step *upgrade-rpm-packages-4.3*.

   .. note:: 
      **Community Packages:** This section assumes you're using the community supplied packages for CloudStack.
      If you've created your own packages and APT repository, substitute your own URL for the ones used in these examples.

   #. 

      Now update your apt package list:

      .. sourcecode:: bash

          $ sudo apt-get update

   #. 

      Now that you have the repository configured, it's time to upgrade
      the ``cloudstack-management`` package. 

      .. sourcecode:: bash

          $ sudo apt-get upgrade cloudstack-management
          $ sudo apt-get upgrade cloudstack-usage

   #. 

      Now it's time to start the management server

      .. sourcecode:: bash

          $ sudo service cloudstack-management start

   #. 

      If you use it, start the usage server

      .. sourcecode:: bash

          $ sudo service cloudstack-usage start

#. 

   (VMware only) Additional steps are required for each VMware cluster.
   These steps will not affect running guests in the cloud. These steps
   are required only for clouds using VMware clusters:

   #. 

      Stop the Management Server:

      .. sourcecode:: bash

          $ sudo service cloudstack-management stop

   #. 

      Generate the encrypted equivalent of your vCenter password:

      .. sourcecode:: bash

          $ java -classpath /usr/share/cloudstack-common/lib/jasypt-1.9.0.jar org.jasypt.intf.cli.JasyptPBEStringEncryptionCLI encrypt.sh input="_your_vCenter_password_" password="`cat /etc/cloudstack/management/key`" verbose=false

      Store the output from this step, we need to add this in
      cluster\_details table and vmware\_data\_center tables in place of
      the plain text password

   #. 

      Find the ID of the row of cluster\_details table that you have to
      update:

      .. sourcecode:: bash

          $ mysql -u <username> -p<password>

      .. sourcecode:: bash

          select * from cloud.cluster_details;

   #. 

      Update the plain text password with the encrypted one

      .. sourcecode:: bash

          update cloud.cluster_details set value = '_ciphertext_from_step_1_' where id = _id_from_step_2_;

   #. 

      Confirm that the table is updated:

      .. sourcecode:: bash

          select * from cloud.cluster_details;

   #. 

      Find the ID of the correct row of vmware\_data\_center that you
      want to update

      .. sourcecode:: bash

          select * from cloud.vmware_data_center;

   #. 

      update the plain text password with the encrypted one:

      .. sourcecode:: bash

          update cloud.vmware_data_center set password = '_ciphertext_from_step_1_' where id = _id_from_step_5_;

   #. 

      Confirm that the table is updated:

      .. sourcecode:: bash

          select * from cloud.vmware_data_center;

   #. 

      Start the CloudStack Management server

      .. sourcecode:: bash

          $ sudo service cloudstack-management start

#. 

   (KVM only) Additional steps are required for each KVM host. These
   steps will not affect running guests in the cloud. These steps are
   required only for clouds using KVM as hosts and only on the KVM
   hosts.

   #. 

      Configure the CloudStack apt repository as detailed above.

   #. 

      Stop the running agent.

      .. sourcecode:: bash

          $ sudo service cloudstack-agent stop

   #. 

      Update the agent software.

      .. sourcecode:: bash

          $ sudo apt-get update cloudstack-agent

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. sourcecode:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Start the agent.

      .. sourcecode:: bash

          $ sudo service cloudstack-agent start

#. 

   If you are using CentOS or RHEL, follow this procedure to upgrade
   your packages. If not, skip to step *restart-system-vms-4.3*.

   .. note::
      **Community Packages:** This section assumes you're using the community supplied packages for CloudStack.
      If you've created your own packages and yum repository, substitute your own URL for the ones used in these examples.

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package by upgrading the older
      ``cloudstack-management`` package.

      .. sourcecode:: bash

          $ sudo yum upgrade cloudstack-management
          $ sudo yum upgrade cloudstack-usage

   #. 

      Now it's time to restart the management server

      .. sourcecode:: bash

          $ sudo service cloudstack-management start

   #. 

      For KVM hosts, upgrade the ``cloudstack-agent`` package

      .. sourcecode:: bash

          $ sudo yum upgrade cloudstack-agent

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. sourcecode:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. sourcecode:: bash

          $ sudo service cloudstack-agent stop
          $ sudo killall jsvc
          $ sudo service cloudstack-agent start

#. 

   Now it's time to restart the management server

   .. sourcecode:: bash

       $ sudo service cloudstack-management start

#. 

   .. note:: **For Xen Hosts: Copy vhd-utils:** This step is only for CloudStack installs that are using Xen hosts.

   Copy the file ``vhd-utils`` to
   ``/usr/share/cloudstack-common/scripts/vm/hypervisor/xenserver``.


Upgrade from 4.2.x to 4.3
-------------------------

This section will guide you from CloudStack 4.2.x to CloudStack 4.3.

Any steps that are hypervisor-specific will be called out with a note.

We recommend reading through this section once or twice before beginning
your upgrade procedure, and working through it on a test system before
working on a production system.

.. note:: The following upgrade instructions should be performed regardless of hypervisor type.

#. 

   #. 

      While running the existing 4.2.x system, log in to the UI as root
      administrator.

   #. 

      In the left navigation bar, click Templates.

   #. 

      In Select view, click Templates.

   #. 

      Click Register template.

      The Register template dialog box is displayed.

   #. 

      In the Register template dialog box, specify the following values
      (do not change these):

      .. include:: upgrade/_templates.rst
      
   #. Watch the screen to be sure that the template downloads successfully and 
      enters the **READY** state. Do not proceed until this is successful.

#. 

   Most users of CloudStack manage the installation and upgrades of
   CloudStack with one of Linux's predominant package systems, RPM or
   APT. This guide assumes you'll be using RPM and Yum (for Red Hat
   Enterprise Linux or CentOS), or APT and Debian packages (for Ubuntu).

#. 

   Create RPM or Debian packages (as appropriate) and a repository from
   the 4.3 source, or check the Apache CloudStack downloads page at
   `http://cloudstack.apache.org/downloads.html <http://cloudstack.apache.org/downloads.html>`__
   for package repositories supplied by community members. You will need
   them for step `8 <#upgrade-deb-packages-4.3>`__ or step
   `11 <#upgrade-rpm-packages-4.3>`__.

   Instructions for creating packages from the CloudStack source are in
   the `Installation
   Guide <http://cloudstack.apache.org/docs/en-US/index.html>`__.

#. 

   Stop your management server or servers. Run this on all management
   server hosts:

   .. sourcecode:: bash

       $ sudo service cloudstack-management stop

#. 

   If you are running a usage server or usage servers, stop those as
   well:

   .. sourcecode:: bash

       $ sudo service cloudstack-usage stop

#. 

   Make a backup of your MySQL database. If you run into any issues or
   need to roll back the upgrade, this will assist in debugging or
   restoring your existing environment. You'll be prompted for your
   password.

   .. sourcecode:: bash

       $ mysqldump -u root -p cloud > cloudstack-backup.sql

#. 

   (KVM Only) If primary storage of type local storage is in use, the
   path for this storage needs to be verified to ensure it passes new
   validation. Check local storage by querying the cloud.storage\_pool
   table:

   .. sourcecode:: bash

       $ mysql -u cloud -p -e "select id,name,path from cloud.storage_pool where pool_type='Filesystem'"

   If local storage paths are found to have a trailing forward slash,
   remove it:

   .. sourcecode:: bash

       $ mysql -u cloud -p -e 'update cloud.storage_pool set path="/var/lib/libvirt/images" where path="/var/lib/libvirt/images/"';

#. 

   If you are using Ubuntu, follow this procedure to upgrade your
   packages. If not, skip to step `11 <#upgrade-rpm-packages-4.3>`__.

   .. note:: **Community Packages:** This section assumes you're using the community supplied packages for CloudStack. If you've created your own packages and APT repository, substitute your own URL for the ones used in these examples.

   #. 

      The first order of business will be to change the sources list for
      each system with CloudStack packages. This means all management
      servers, and any hosts that have the KVM agent. (No changes should
      be necessary for hosts that are running VMware or Xen.)

      Start by opening ``/etc/apt/sources.list.d/cloudstack.list`` on
      any systems that have CloudStack packages installed.

      This file should have one line, which contains:

      .. sourcecode:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.2

      We'll change it to point to the new package repository:

      .. sourcecode:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.3

      If you're using your own package repository, change this line to
      read as appropriate for your 4.3 repository.

   #. 

      Now update your apt package list:

      .. sourcecode:: bash

          $ sudo apt-get update

   #. 

      Now that you have the repository configured, it's time to upgrade
      the ``cloudstack-management`` package. 

      .. sourcecode:: bash

          $ sudo apt-get upgrade cloudstack-management

   #. 

      Now it's time to start the management server

      .. sourcecode:: bash

          $ sudo service cloudstack-management start

   #. 

      If you use it, start the usage server

      .. sourcecode:: bash

          $ sudo service cloudstack-usage start

#. 

   (VMware only) Additional steps are required for each VMware cluster.
   These steps will not affect running guests in the cloud. These steps
   are required only for clouds using VMware clusters:

   #. 

      Stop the Management Server:

      .. sourcecode:: bash

          $ sudo service cloudstack-management stop

   #. 

      Generate the encrypted equivalent of your vCenter password:

      .. sourcecode:: bash

          $ java -classpath /usr/share/cloudstack-common/lib/jasypt-1.9.0.jar org.jasypt.intf.cli.JasyptPBEStringEncryptionCLI encrypt.sh input="_your_vCenter_password_" password="`cat /etc/cloudstack/management/key`" verbose=false

      Store the output from this step, we need to add this in
      cluster\_details table and vmware\_data\_center tables in place of
      the plain text password

   #. 

      Find the ID of the row of cluster\_details table that you have to
      update:

      .. sourcecode:: bash

          $ mysql -u <username> -p<password>

      .. sourcecode:: bash

          select * from cloud.cluster_details;

   #. 

      Update the plain text password with the encrypted one

      .. sourcecode:: bash

          update cloud.cluster_details set value = '_ciphertext_from_step_1_' where id = _id_from_step_2_;

   #. 

      Confirm that the table is updated:

      .. sourcecode:: bash

          select * from cloud.cluster_details;

   #. 

      Find the ID of the correct row of vmware\_data\_center that you
      want to update

      .. sourcecode:: bash

          select * from cloud.vmware_data_center;

   #. 

      update the plain text password with the encrypted one:

      .. sourcecode:: bash

          update cloud.vmware_data_center set password = '_ciphertext_from_step_1_' where id = _id_from_step_5_;

   #. 

      Confirm that the table is updated:

      .. sourcecode:: bash

          select * from cloud.vmware_data_center;

   #. 

      Start the CloudStack Management server

      .. sourcecode:: bash

          $ sudo service cloudstack-management start

#. 

   (KVM only) Additional steps are required for each KVM host. These
   steps will not affect running guests in the cloud. These steps are
   required only for clouds using KVM as hosts and only on the KVM
   hosts.

   #. 

      Configure the CloudStack apt repository as detailed above.

   #. 

      Stop the running agent.

      .. sourcecode:: bash

          $ sudo service cloudstack-agent stop

   #. 

      Update the agent software.

      .. sourcecode:: bash

          $ sudo apt-get update cloudstack-agent

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. sourcecode:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Start the agent.

      .. sourcecode:: bash

          $ sudo service cloudstack-agent start

#. 

   If you are using CentOS or RHEL, follow this procedure to upgrade
   your packages. If not, skip to step `14 <#restart-system-vms-4.3>`__.

   .. note:: **Community Packages:** This section assumes you're using the community supplied packages for CloudStack. If you've created your own packages and yum repository, substitute your own URL for the ones used in these examples.

   #. 

      The first order of business will be to change the yum repository
      for each system with CloudStack packages. This means all
      management servers, and any hosts that have the KVM agent.

      (No changes should be necessary for hosts that are running VMware
      or Xen.)

      Start by opening ``/etc/yum.repos.d/cloudstack.repo`` on any
      systems that have CloudStack packages installed.

      This file should have content similar to the following:

      .. sourcecode:: bash

          [apache-cloudstack]
          name=Apache CloudStack
          baseurl=http://cloudstack.apt-get.eu/rhel/4.2/
          enabled=1
          gpgcheck=0

      If you are using the community provided package repository, change
      the base url to http://cloudstack.apt-get.eu/rhel/4.3/

      If you're using your own package repository, change this line to
      read as appropriate for your 4.3 repository.

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package by upgrading the older
      ``cloudstack-management`` package.

      .. sourcecode:: bash

          $ sudo yum upgrade cloudstack-management

   #. 

      Now it's time to restart the management server

      .. sourcecode:: bash

          $ sudo service cloudstack-management start

   #. 

      For KVM hosts, upgrade the ``cloudstack-agent`` package

      .. sourcecode:: bash

          $ sudo yum upgrade cloudstack-agent

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. sourcecode:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. sourcecode:: bash

          $ sudo service cloudstack-agent stop
          $ sudo killall jsvc
          $ sudo service cloudstack-agent start

#. 

   Now it's time to restart the management server

   .. sourcecode:: bash

       $ sudo service cloudstack-management start

#. 

   Once you've upgraded the packages on your management servers, you'll
   need to restart the system VMs. Ensure that the admin port is set to
   8096 by using the "integration.api.port" global parameter. This port
   is used by the cloud-sysvmadm script at the end of the upgrade
   procedure. For information about how to set this parameter, see
   "Setting Global Configuration Parameters" in the Installation Guide.
   Changing this parameter will require management server restart. Also
   make sure port 8096 is open in your local host firewall to do this.

   There is a script that will do this for you, all you need to do is
   run the script and supply the IP address for your MySQL instance and
   your MySQL credentials:

   .. sourcecode:: bash

       # nohup cloudstack-sysvmadm -d IP address -u cloud -p -a > sysvm.log 2>&1 &

   You can monitor the log for progress. The process of restarting the
   system VMs can take an hour or more.

   .. sourcecode:: bash

       # tail -f sysvm.log

   The output to ``sysvm.log`` will look something like this:

   .. sourcecode:: bash

       Stopping and starting 1 secondary storage vm(s)...
       Done stopping and starting secondary storage vm(s)
       Stopping and starting 1 console proxy vm(s)...
       Done stopping and starting console proxy vm(s).
       Stopping and starting 4 running routing vm(s)...
       Done restarting router(s).

#. 

   .. note:: **For Xen Hosts: Copy vhd-utils:** This step is only for CloudStack installs that are using Xen hosts.

   Copy the file ``vhd-utils`` to
   ``/usr/share/cloudstack-common/scripts/vm/hypervisor/xenserver``.

Upgrade from 4.1.x to 4.3
------------------------------

This section will guide you from CloudStack 4.1.x versions to CloudStack 4.3.

Any steps that are hypervisor-specific will be called out with a note.

We recommend reading through this section once or twice before beginning
your upgrade procedure, and working through it on a test system before
working on a production system.

#. 

   Most users of CloudStack manage the installation and upgrades of
   CloudStack with one of Linux's predominant package systems, RPM or
   APT. This guide assumes you'll be using RPM and Yum (for Red Hat
   Enterprise Linux or CentOS), or APT and Debian packages (for Ubuntu).

#.

   .. note:: The following upgrade instructions should be performed regardless of hypervisor type.

   #. 

      While running the existing 4.1.x system, log in to the UI as root
      administrator.

   #. 

      In the left navigation bar, click Templates.

   #. 

      In Select view, click Templates.

   #. 

      Click Register template.

      The Register template dialog box is displayed.

   #. 

      In the Register template dialog box, specify the following values
      (do not change these):

      .. include:: upgrade/_templates.rst


#. 

   Create RPM or Debian packages (as appropriate) and a repository from
   the 4.3 source, or check the Apache CloudStack downloads page at
   `http://cloudstack.apache.org/downloads.html <http://cloudstack.apache.org/downloads.html>`__
   for package repositories supplied by community members. You will need
   them for step `8 <#upgrade-deb-packages-41to42>`__ or step
   `11 <#upgrade-rpm-packages-41to42>`__.

   Instructions for creating packages from the CloudStack source are in
   the `Installation
   Guide <http://cloudstack.apache.org/docs/en-US/index.html>`__.

#. 

   Stop your management server or servers. Run this on all management
   server hosts:

   .. sourcecode:: bash

       # service cloudstack-management stop

#. 

   If you are running a usage server or usage servers, stop those as
   well:

   .. sourcecode:: bash

       # service cloudstack-usage stop

#. 

   Make a backup of your MySQL database. If you run into any issues or
   need to roll back the upgrade, this will assist in debugging or
   restoring your existing environment. You'll be prompted for your
   password.

   .. sourcecode:: bash

       # mysqldump -u root -p cloud > cloudstack-backup.sql

#. 

   (KVM Only) If primary storage of type local storage is in use, the
   path for this storage needs to be verified to ensure it passes new
   validation. Check local storage by querying the cloud.storage\_pool
   table:

   .. sourcecode:: bash

       #mysql -u cloud -p -e "select id,name,path from cloud.storage_pool where pool_type='Filesystem'"

   If local storage paths are found to have a trailing forward slash,
   remove it:

   .. sourcecode:: bash

       #mysql -u cloud -p -e 'update cloud.storage_pool set path="/var/lib/libvirt/images" where path="/var/lib/libvirt/images/"';

#. 

   If you are using Ubuntu, follow this procedure to upgrade your
   packages. If not, skip to step `11 <#upgrade-rpm-packages-41to42>`__.

   .. note::
   
      **Community Packages:** This section assumes you're using the community supplied packages for CloudStack. If you've created your own packages and APT repository, substitute your own URL for the ones used in these examples.

   #. 

      The first order of business will be to change the sources list for
      each system with CloudStack packages. This means all management
      servers, and any hosts that have the KVM agent. (No changes should
      be necessary for hosts that are running VMware or Xen.)

      Start by opening ``/etc/apt/sources.list.d/cloudstack.list`` on
      any systems that have CloudStack packages installed.

      This file should have one line, which contains:

      .. sourcecode:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.1

      We'll change it to point to the new package repository:

      .. sourcecode:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.3

      If you're using your own package repository, change this line to
      read as appropriate for your 4.3 repository.

   #. 

      Now update your apt package list:

      .. sourcecode:: bash

          $ sudo apt-get update

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package. This will pull in any other
      dependencies you need.

      .. sourcecode:: bash

          $ sudo apt-get install cloudstack-management

   #. 

      You will need to manually install the ``cloudstack-agent``
      package:

      .. sourcecode:: bash

          $ sudo apt-get install cloudstack-agent

      During the installation of ``cloudstack-agent``, APT will copy
      your ``agent.properties``, ``log4j-cloud.xml``, and
      ``environment.properties`` from ``/etc/cloud/agent`` to
      ``/etc/cloudstack/agent``.

      When prompted whether you wish to keep your configuration, say
      Yes.

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. sourcecode:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. sourcecode:: bash

          service cloudstack-agent stop
          killall jsvc
          service cloudstack-agent start

#. 

   (VMware only) Additional steps are required for each VMware cluster.
   These steps will not affect running guests in the cloud. These steps
   are required only for clouds using VMware clusters:

   #. 

      Stop the Management Server:

      .. sourcecode:: bash

          service cloudstack-management stop

   #. 

      Generate the encrypted equivalent of your vCenter password:

      .. sourcecode:: bash

          java -classpath /usr/share/cloudstack-common/lib/jasypt-1.9.0.jar org.jasypt.intf.cli.JasyptPBEStringEncryptionCLI encrypt.sh input="_your_vCenter_password_" password="`cat /etc/cloudstack/management/key`" verbose=false

      Store the output from this step, we need to add this in
      cluster\_details table and vmware\_data\_center tables in place of
      the plain text password

   #. 

      Find the ID of the row of cluster\_details table that you have to
      update:

      .. sourcecode:: bash

          mysql -u <username> -p<password>

      .. sourcecode:: bash

          select * from cloud.cluster_details;

   #. 

      Update the plain text password with the encrypted one

      .. sourcecode:: bash

          update cloud.cluster_details set value = '_ciphertext_from_step_1_' where id = _id_from_step_2_;

   #. 

      Confirm that the table is updated:

      .. sourcecode:: bash

          select * from cloud.cluster_details;

   #. 

      Find the ID of the correct row of vmware\_data\_center that you
      want to update

      .. sourcecode:: bash

          select * from cloud.vmware_data_center;

   #. 

      update the plain text password with the encrypted one:

      .. sourcecode:: bash

          update cloud.vmware_data_center set password = '_ciphertext_from_step_1_' where id = _id_from_step_5_;

   #. 

      Confirm that the table is updated:

      .. sourcecode:: bash

          select * from cloud.vmware_data_center;

   #. 

      Start the CloudStack Management server

      .. sourcecode:: bash

          service cloudstack-management start

#. 

   (KVM only) Additional steps are required for each KVM host. These
   steps will not affect running guests in the cloud. These steps are
   required only for clouds using KVM as hosts and only on the KVM
   hosts.

   #. 

      Configure the CloudStack yum repository as detailed above.

   #. 

      Stop the running agent.

      .. sourcecode:: bash

          # service cloud-agent stop

   #. 

      Update the agent software.

      .. sourcecode:: bash

          # yum update cloudstack-agent

   #. 

      Start the agent.

      .. sourcecode:: bash

          # service cloudstack-agent start

#. 

   If you are using CentOS or RHEL, follow this procedure to upgrade
   your packages. If not, skip to step
   `13 <#restart-system-vms-41to42>`__.

   .. note:: 
   
      **Community Packages:** This section assumes you're using the community supplied packages for CloudStack. If you've created your own packages and yum repository, substitute your own URL for the ones used in these examples.

   #. 

      The first order of business will be to change the yum repository
      for each system with CloudStack packages. This means all
      management servers, and any hosts that have the KVM agent.

      (No changes should be necessary for hosts that are running VMware
      or Xen.)

      Start by opening ``/etc/yum.repos.d/cloudstack.repo`` on any
      systems that have CloudStack packages installed.

      This file should have content similar to the following:

      .. sourcecode:: bash

          [apache-cloudstack]
          name=Apache CloudStack
          baseurl=http://cloudstack.apt-get.eu/rhel/4.1/
          enabled=1
          gpgcheck=0

      If you are using the community provided package repository, change
      the base url to http://cloudstack.apt-get.eu/rhel/4.3/

      If you're using your own package repository, change this line to
      read as appropriate for your 4.3 repository.

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package by upgrading the older
      ``cloudstack-management`` package.

      .. sourcecode:: bash

          $ sudo yum upgrade cloudstack-management

   #. 

      For KVM hosts, you will need to upgrade the ``cloud-agent``
      package, similarly installing the new version as
      ``cloudstack-agent``.

      .. sourcecode:: bash

          $ sudo yum upgrade cloudstack-agent

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. sourcecode:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. sourcecode:: bash

          service cloudstack-agent stop
          killall jsvc
          service cloudstack-agent start

#. 

   Now it's time to restart the management server

   .. sourcecode:: bash

       # service cloudstack-management start

#. 

   Once you've upgraded the packages on your management servers, you'll
   need to restart the system VMs. Ensure that the admin port is set to
   8096 by using the "integration.api.port" global parameter. This port
   is used by the cloud-sysvmadm script at the end of the upgrade
   procedure. For information about how to set this parameter, see
   "Setting Global Configuration Parameters" in the Installation Guide.
   Changing this parameter will require management server restart. Also
   make sure port 8096 is open in your local host firewall to do this.

   There is a script that will do this for you, all you need to do is
   run the script and supply the IP address for your MySQL instance and
   your MySQL credentials:

   .. sourcecode:: bash

       # nohup cloudstack-sysvmadm -d IP address -u cloud -p -a > sysvm.log 2>&1 &

   You can monitor the log for progress. The process of restarting the
   system VMs can take an hour or more.

   .. sourcecode:: bash

       # tail -f sysvm.log

   The output to ``sysvm.log`` will look something like this:

   .. sourcecode:: bash

       Stopping and starting 1 secondary storage vm(s)...
       Done stopping and starting secondary storage vm(s)
       Stopping and starting 1 console proxy vm(s)...
       Done stopping and starting console proxy vm(s).
       Stopping and starting 4 running routing vm(s)...
       Done restarting router(s).

#.

   .. note::
   
      **For Xen Hosts: Copy vhd-utils:** This step is only for CloudStack installs that are using Xen hosts.

   Copy the file ``vhd-utils`` to
   ``/usr/share/cloudstack-common/scripts/vm/hypervisor/xenserver``.

Upgrade from 4.0.x to 4.3
-------------------------

This section will guide you from CloudStack 4.0.x versions to CloudStack 4.3.

Any steps that are hypervisor-specific will be called out with a note.

.. warning:: **Package Structure Changes:** The package structure for CloudStack has changed significantly since the 4.0.x releases. If you've compiled your own packages, you'll notice that the package names and the number of packages has changed. This is *not* a bug. However, this *does* mean that the procedure is not as simple as an ``apt-get upgrade`` or ``yum update``, so please follow this section carefully.

We recommend reading through this section once or twice before beginning
your upgrade procedure, and working through it on a test system before
working on a production system.

#. 

   Most users of CloudStack manage the installation and upgrades of
   CloudStack with one of Linux's predominant package systems, RPM or
   APT. This guide assumes you'll be using RPM and Yum (for Red Hat
   Enterprise Linux or CentOS), or APT and Debian packages (for Ubuntu).

   Create RPM or Debian packages (as appropriate) and a repository from
   the 4.3 source, or check the Apache CloudStack downloads page at
   `http://cloudstack.apache.org/downloads.html <http://cloudstack.apache.org/downloads.html>`__
   for package repositories supplied by community members. You will need
   them for step `9 <#upgrade-deb-packages-40to41>`__ or step
   `10 <#upgrade-rpm-packages-40to41>`__.

   Instructions for creating packages from the CloudStack source are in
   the `Installation
   Guide <http://cloudstack.apache.org/docs/en-US/index.html>`__.

   .. note:: The following upgrade instructions should be performed regardless of hypervisor type.

   #. 

      While running the existing 4.0.0 system, log in to the UI as root
      administrator.

   #. 

      In the left navigation bar, click Templates.

   #. 

      In Select view, click Templates.

   #. 

      Click Register template.

      The Register template dialog box is displayed.

   #. 

      In the Register template dialog box, specify the following values
      (do not change these):

      .. include:: upgrade/_templates.rst

#. 

   Stop your management server or servers. Run this on all management
   server hosts:

   .. sourcecode:: bash

       # service cloud-management stop

#. 

   If you are running a usage server or usage servers, stop those as
   well:

   .. sourcecode:: bash

       # service cloud-usage stop

#. 

   Make a backup of your MySQL database. If you run into any issues or
   need to roll back the upgrade, this will assist in debugging or
   restoring your existing environment. You'll be prompted for your
   password.

   .. sourcecode:: bash

       # mysqldump -u root -p cloud > cloudstack-backup.sql

#. 

   Whether you're upgrading a Red Hat/CentOS based system or Ubuntu
   based system, you're going to need to stop the CloudStack management
   server before proceeding.

   .. sourcecode:: bash

       # service cloud-management stop

#. 

   If you have made changes to ``/etc/cloud/management/components.xml``,
   you'll need to carry these over manually to the new file,
   ``/etc/cloudstack/management/componentContext.xml``. This is not done
   automatically. (If you're unsure, we recommend making a backup of the
   original ``components.xml`` to be on the safe side.

#. 

   After upgrading to 4.3, API clients are expected to send plain text
   passwords for login and user creation, instead of MD5 hash. Incase,
   api client changes are not acceptable, following changes are to be
   made for backward compatibility:

   Modify componentContext.xml, and make PlainTextUserAuthenticator as
   the default authenticator (1st entry in the userAuthenticators
   adapter list is default)

   .. sourcecode:: bash

       <!-- Security adapters -->
       <bean id="userAuthenticators" class="com.cloud.utils.component.AdapterList">
         <property name="Adapters">
           <list>
             <ref bean="PlainTextUserAuthenticator"/>
             <ref bean="MD5UserAuthenticator"/>
             <ref bean="LDAPUserAuthenticator"/>
           </list>
         </property>
       </bean>

   PlainTextUserAuthenticator works the same way MD5UserAuthenticator
   worked prior to 4.3.

#. 

   If you are using Ubuntu, follow this procedure to upgrade your
   packages. If not, skip to step `10 <#upgrade-rpm-packages-40to41>`__.

   .. note:: **Community Packages:** This section assumes you're using the community supplied packages for CloudStack. If you've created your own packages and APT repository, substitute your own URL for the ones used in these examples.

   #. 

      The first order of business will be to change the sources list for
      each system with CloudStack packages. This means all management
      servers, and any hosts that have the KVM agent. (No changes should
      be necessary for hosts that are running VMware or Xen.)

      Start by opening ``/etc/apt/sources.list.d/cloudstack.list`` on
      any systems that have CloudStack packages installed.

      This file should have one line, which contains:

      .. sourcecode:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.0

      We'll change it to point to the new package repository:

      .. sourcecode:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.3

      If you're using your own package repository, change this line to
      read as appropriate for your 4.3 repository.

   #. 

      Now update your apt package list:

      .. sourcecode:: bash

          $ sudo apt-get update

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package. This will pull in any other
      dependencies you need.

      .. sourcecode:: bash

          $ sudo apt-get install cloudstack-management

   #. 

      You will need to manually install the ``cloudstack-agent``
      package:

      .. sourcecode:: bash

          $ sudo apt-get install cloudstack-agent

      During the installation of ``cloudstack-agent``, APT will copy
      your ``agent.properties``, ``log4j-cloud.xml``, and
      ``environment.properties`` from ``/etc/cloud/agent`` to
      ``/etc/cloudstack/agent``.

      When prompted whether you wish to keep your configuration, say
      Yes.

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. sourcecode:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. sourcecode:: bash

                                          service cloud-agent stop
                                          killall jsvc
                                          service cloudstack-agent start

   #. 

      During the upgrade, ``log4j-cloud.xml`` was simply copied over, so
      the logs will continue to be added to
      ``/var/log/cloud/agent/agent.log``. There's nothing *wrong* with
      this, but if you prefer to be consistent, you can change this by
      copying over the sample configuration file:

      .. sourcecode:: bash

                                          cd /etc/cloudstack/agent
                                          mv log4j-cloud.xml.dpkg-dist log4j-cloud.xml
                                          service cloudstack-agent restart

   #. 

      Once the agent is running, you can uninstall the old cloud-\*
      packages from your system:

      .. sourcecode:: bash

          sudo dpkg --purge cloud-agent

#. 

   If you are using CentOS or RHEL, follow this procedure to upgrade
   your packages. If not, skip to step
   `11 <#restart-system-vms-40to41>`__.

   .. note:: **Community Packages:** This section assumes you're using the community supplied packages for CloudStack. If you've created your own packages and yum repository, substitute your own URL for the ones used in these examples.

   #. 

      The first order of business will be to change the yum repository
      for each system with CloudStack packages. This means all
      management servers, and any hosts that have the KVM agent. (No
      changes should be necessary for hosts that are running VMware or
      Xen.)

      Start by opening ``/etc/yum.repos.d/cloudstack.repo`` on any
      systems that have CloudStack packages installed.

      This file should have content similar to the following:

      .. sourcecode:: bash

                                          [apache-cloudstack]
                                          name=Apache CloudStack
                                          baseurl=http://cloudstack.apt-get.eu/rhel/4.0/
                                          enabled=1
                                          gpgcheck=0

      If you are using the community provided package repository, change
      the baseurl to http://cloudstack.apt-get.eu/rhel/4.3/

      If you're using your own package repository, change this line to
      read as appropriate for your 4.3 repository.

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package by upgrading the older
      ``cloud-client`` package.

      .. sourcecode:: bash

          $ sudo yum upgrade cloud-client

   #. 

      For KVM hosts, you will need to upgrade the ``cloud-agent``
      package, similarly installing the new version as
      ``cloudstack-agent``.

      .. sourcecode:: bash

          $ sudo yum upgrade cloud-agent

      During the installation of ``cloudstack-agent``, the RPM will copy
      your ``agent.properties``, ``log4j-cloud.xml``, and
      ``environment.properties`` from ``/etc/cloud/agent`` to
      ``/etc/cloudstack/agent``.

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. sourcecode:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. sourcecode:: bash

                                          service cloud-agent stop
                                          killall jsvc
                                          service cloudstack-agent start

#. 

   Once you've upgraded the packages on your management servers, you'll
   need to restart the system VMs. Make sure port 8096 is open in your
   local host firewall to do this.

   There is a script that will do this for you, all you need to do is
   run the script and supply the IP address for your MySQL instance and
   your MySQL credentials:

   .. sourcecode:: bash

       # nohup cloudstack-sysvmadm -d IP address -u cloud -p -a > sysvm.log 2>&1 &

   You can monitor the log for progress. The process of restarting the
   system VMs can take an hour or more.

   .. sourcecode:: bash

       # tail -f sysvm.log

   The output to ``sysvm.log`` will look something like this:

   .. sourcecode:: bash

                               Stopping and starting 1 secondary storage vm(s)...
                               Done stopping and starting secondary storage vm(s)
                               Stopping and starting 1 console proxy vm(s)...
                               Done stopping and starting console proxy vm(s).
                               Stopping and starting 4 running routing vm(s)...
                               Done restarting router(s).

#. .. note:: *For Xen Hosts: Copy vhd-utils:** This step is only for CloudStack installs that are using Xen hosts.

   Copy the file ``vhd-utils`` to
   ``/usr/share/cloudstack-common/scripts/vm/hypervisor/xenserver``.

Upgrade from 3.0.x to 4.3
-------------------------

This section will guide you from Citrix CloudStack 3.0.x to Apache
CloudStack 4.3. Sections that are hypervisor-specific will be called out
with a note.

   .. note::  The following upgrade instructions should be performed regardless of hypervisor type.

   #. 

      While running the existing 3.0.x system, log in to the UI as root
      administrator.

   #. 

      In the left navigation bar, click Templates.

   #. 

      In Select view, click Templates.

   #. 

      Click Register template.

      The Register template dialog box is displayed.

   #. 

      In the Register template dialog box, specify the following values
      (do not change these):
      
      .. include:: upgrade/_templates.rst
	   
   #. 

      Watch the screen to be sure that the template downloads
      successfully and enters the READY state. Do not proceed until this
      is successful.

#. 

   (KVM on RHEL 6.0/6.1 only) If your existing CloudStack deployment
   includes one or more clusters of KVM hosts running RHEL 6.0 or RHEL
   6.1, perform the following:

   #. 

      Ensure that you upgrade the operating system version on those
      hosts before upgrading CloudStack

      To do that, change the yum repository for each system with
      CloudStack packages, that implies that all the Management Servers
      and any hosts that have the KVM agent.

   #. 

      Open ``/etc/yum.repos.d/cloudstack.repo`` on any systems that have
      CloudStack packages installed.

   #. 

      Edit as follows:

      .. sourcecode:: bash

                      [upgrade]
                      name=rhel63
                      baseurl=url-of-your-rhel6.3-repo
                      enabled=1
                      gpgcheck=0
                      [apache CloudStack]
                      name= Apache CloudStack
                      baseurl= http://cloudstack.apt-get.eu/rhel/4.3/
                      enabled=1
                      gpgcheck=0

      If you are using the community provided package repository, change
      the baseurl to http:// cloudstack.apt-get.eu/rhel/4.3/

      If you are using your own package repository, change this line to
      read as appropriate for your 4.3 repository.

   #. 

      Now that you have the repository configured, upgrade the host
      operating system from RHEL 6.0 to 6.3:

      .. sourcecode:: bash

          # yum upgrade

#. 

   Stop all Usage Servers if running. Run this on all Usage Server
   hosts.

   .. sourcecode:: bash

       # service cloud-usage stop

#. 

   Stop the Management Servers. Run this on all Management Server hosts.

   .. sourcecode:: bash

       # service cloud-management stop

#. 

   On the MySQL master, take a backup of the MySQL databases. We
   recommend performing this step even in test upgrades. If there is an
   issue, this will assist with debugging.

   In the following commands, it is assumed that you have set the root
   password on the database, which is a CloudStack recommended best
   practice. Substitute your own MySQL root password.

   .. sourcecode:: bash

       # mysqldump -u root -pmysql_password cloud > cloud-backup.dmp
                               # mysqldump -u root -pmysql_password cloud_usage > cloud-usage-backup.dmp

#. 

   Either build RPM/DEB packages as detailed in the Installation Guide,
   or use one of the community provided yum/apt repositories to gain
   access to the CloudStack binaries.

#. 

   If you are using Ubuntu, follow this procedure to upgrade your
   packages. If not, skip to step `8 <#upgrade-rpm-packages-302>`__.

   .. note:: **Community Packages:** This section assumes you're using the community supplied packages for CloudStack. If you've created your own packages and APT repository, substitute your own URL for the ones used in these examples.

   #. 

      The first order of business will be to change the sources list for
      each system with CloudStack packages. This means all management
      servers, and any hosts that have the KVM agent. (No changes should
      be necessary for hosts that are running VMware or Xen.)

      Start by opening ``/etc/apt/sources.list.d/cloudstack.list`` on
      any systems that have CloudStack packages installed.

      This file should have one line, which contains:

      .. sourcecode:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.0

      We'll change it to point to the new package repository:

      .. sourcecode:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.3

      If you're using your own package repository, change this line to
      read as appropriate for your 4.3 repository.

   #. 

      Now update your apt package list:

      .. sourcecode:: bash

          $ sudo apt-get update

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package. This will pull in any other
      dependencies you need.

      .. sourcecode:: bash

          $ sudo apt-get install cloudstack-management

   #. 

      You will need to manually install the ``cloudstack-agent``
      package:

      .. sourcecode:: bash

          $ sudo apt-get install cloudstack-agent

      During the installation of ``cloudstack-agent``, APT will copy
      your ``agent.properties``, ``log4j-cloud.xml``, and
      ``environment.properties`` from ``/etc/cloud/agent`` to
      ``/etc/cloudstack/agent``.

      When prompted whether you wish to keep your configuration, say
      Yes.

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. sourcecode:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. sourcecode:: bash

          service cloud-agent stop
          killall jsvc
          service cloudstack-agent start

   #. 

      During the upgrade, ``log4j-cloud.xml`` was simply copied over, so
      the logs will continue to be added to
      ``/var/log/cloud/agent/agent.log``. There's nothing *wrong* with
      this, but if you prefer to be consistent, you can change this by
      copying over the sample configuration file:

      .. sourcecode:: bash

          cd /etc/cloudstack/agent
          mv log4j-cloud.xml.dpkg-dist log4j-cloud.xml
          service cloudstack-agent restart

   #. 

      Once the agent is running, you can uninstall the old cloud-\*
      packages from your system:

      .. sourcecode:: bash

          sudo dpkg --purge cloud-agent

#. 

   If you are using CentOS or RHEL, follow this procedure to upgrade
   your packages. If not, skip to step
   `9 <#correct-components-xml-302>`__.

   .. note:: **Community Packages:** This section assumes you're using the community supplied packages for CloudStack. If you've created your own packages and yum repository, substitute your own URL for the ones used in these examples.

   #. 

      The first order of business will be to change the yum repository
      for each system with CloudStack packages. This means all
      management servers, and any hosts that have the KVM agent. (No
      changes should be necessary for hosts that are running VMware or
      Xen.)

      Start by opening ``/etc/yum.repos.d/cloudstack.repo`` on any
      systems that have CloudStack packages installed.

      This file should have content similar to the following:

      .. sourcecode:: bash

          [apache-cloudstack]
          name=Apache CloudStack
          baseurl=http://cloudstack.apt-get.eu/rhel/4.3/
          enabled=1
          gpgcheck=0

      If you are using the community provided package repository, change
      the baseurl to http://cloudstack.apt-get.eu/rhel/4.3/

      If you're using your own package repository, change this line to
      read as appropriate for your 4.3 repository.

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package by upgrading the older
      ``cloud-client`` package.

      .. sourcecode:: bash

          $ sudo yum upgrade cloud-client

   #. 

      For KVM hosts, you will need to upgrade the ``cloud-agent``
      package, similarly installing the new version as
      ``cloudstack-agent``.

      .. sourcecode:: bash

          $ sudo yum upgrade cloud-agent

      During the installation of ``cloudstack-agent``, the RPM will copy
      your ``agent.properties``, ``log4j-cloud.xml``, and
      ``environment.properties`` from ``/etc/cloud/agent`` to
      ``/etc/cloudstack/agent``.

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. sourcecode:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. sourcecode:: bash

          service cloud-agent stop
          killall jsvc
          service cloudstack-agent start

#. 

   If you have made changes to your copy of
   ``/etc/cloud/management/components.xml`` the changes will be
   preserved in the upgrade. However, you need to do the following steps
   to place these changes in a new version of the file which is
   compatible with version 4.2.x.

   #. 

      Make a backup copy of ``/etc/cloud/management/components.xml``.
      For example:

      .. sourcecode:: bash

          # mv /etc/cloud/management/components.xml /etc/cloud/management/components.xml-backup

   #. 

      Copy ``/etc/cloud/management/components.xml.rpmnew`` to create a
      new ``/etc/cloud/management/components.xml``:

      .. sourcecode:: bash

          # cp -ap /etc/cloud/management/components.xml.rpmnew /etc/cloud/management/components.xml

   #. 

      Merge your changes from the backup file into the new
      ``components.xml``.

      .. sourcecode:: bash

          # vi /etc/cloudstack/management/components.xml

   .. note::  If you have more than one management server node, repeat the upgrade steps on each node.

#. 

   After upgrading to 4.3, API clients are expected to send plain text
   passwords for login and user creation, instead of MD5 hash. Incase,
   api client changes are not acceptable, following changes are to be
   made for backward compatibility:

   Modify componentContext.xml, and make PlainTextUserAuthenticator as
   the default authenticator (1st entry in the userAuthenticators
   adapter list is default)

   .. sourcecode:: bash

       <!-- Security adapters -->
       <bean id="userAuthenticators" class="com.cloud.utils.component.AdapterList">
         <property name="Adapters">
           <list>
             <ref bean="PlainTextUserAuthenticator"/>
             <ref bean="MD5UserAuthenticator"/>
             <ref bean="LDAPUserAuthenticator"/>
           </list>
         </property>
       </bean>

   PlainTextUserAuthenticator works the same way MD5UserAuthenticator
   worked prior to 4.3

#. 

   Start the first Management Server. Do not start any other Management
   Server nodes yet.

   .. sourcecode:: bash

       # service cloudstack-management start

   Wait until the databases are upgraded. Ensure that the database
   upgrade is complete. After confirmation, start the other Management
   Servers one at a time by running the same command on each node.

   .. note:: Failing to restart the Management Server indicates a problem in the upgrade. Having the Management Server restarted without any issues indicates that the upgrade is successfully completed.

#. 

   Start all Usage Servers (if they were running on your previous
   version). Perform this on each Usage Server host.

   ``# service cloudstack-usage start``

#. 

   Additional steps are required for each KVM host. These steps will not
   affect running guests in the cloud. These steps are required only for
   clouds using KVM as hosts and only on the KVM hosts.

   #. 

      Configure a yum or apt repository containing the CloudStack
      packages as outlined in the Installation Guide.

   #. 

      Stop the running agent.

      ``# service cloud-agent stop``

   #. 

      Update the agent software with one of the following command sets
      as appropriate for your environment.

      ``# yum update cloud-*``

      ``# apt-get update``

      ``# apt-get upgrade cloud-*``

   #. 

      Edit ``/etc/cloudstack/agent/agent.properties`` to change the
      resource parameter from
      "com.cloud.agent.resource.computing.LibvirtComputingResource" to
      "com.cloud.hypervisor.kvm.resource.LibvirtComputingResource".

   #. 

      Upgrade all the existing bridge names to new bridge names by
      running this script:

      .. sourcecode:: bash

           # cloudstack-agent-upgrade

   #. 

      Install a libvirt hook with the following commands:

      .. sourcecode:: bash

           # mkdir /etc/libvirt/hooks
           # cp /usr/share/cloudstack-agent/lib/libvirtqemuhook /etc/libvirt/hooks/qemu
           # chmod +x /etc/libvirt/hooks/qemu

   #. 

      Restart libvirtd.

      .. sourcecode:: bash

          # service libvirtd restart

   #. 

      Start the agent.

      .. sourcecode:: bash

          # service cloudstack-agent start

   #. 

      When the Management Server is up and running, log in to the
      CloudStack UI and restart the virtual router for proper
      functioning of all the features.

#. 

   Log in to the CloudStack UI as administrator, and check the status of
   the hosts. All hosts should come to Up state (except those that you
   know to be offline). You may need to wait 20 or 30 minutes, depending
   on the number of hosts.

   .. note:: Troubleshooting: If login fails, clear your browser cache and reload the page.

   Do not proceed to the next step until the hosts show in Up state.

#. 

   If you are upgrading from 3.0.x, perform the following:

   #. 

      Ensure that the admin port is set to 8096 by using the
      "integration.api.port" global parameter.

      This port is used by the cloud-sysvmadm script at the end of the
      upgrade procedure. For information about how to set this
      parameter, see "Setting Global Configuration Parameters" in the
      Installation Guide.

   #. 

      Restart the Management Server.

      .. note:: If you don't want the admin port to remain open, you can set it to null after the upgrade is done and restart the management server.

#. 

   Run the ``cloudstack-sysvmadm`` script to stop, then start, all
   Secondary Storage VMs, Console Proxy VMs, and virtual routers. Run
   the script once on each management server. Substitute your own IP
   address of the MySQL instance, the MySQL user to connect as, and the
   password to use for that user. In addition to those parameters,
   provide the ``-c`` and ``-r`` arguments. For example:

   ``# nohup cloudstack-sysvmadm -d 192.168.1.5 -u cloud -p password -c -r > sysvm.log 2>&1 &``

   ``# tail -f sysvm.log``

   This might take up to an hour or more to run, depending on the number
   of accounts in the system.

#. 

   If needed, upgrade all Citrix XenServer hypervisor hosts in your
   cloud to a version supported by CloudStack 4.3. The supported
   versions are XenServer 5.6 SP2 and 6.0.2. Instructions for upgrade
   can be found in the CloudStack 4.3 Installation Guide under
   "Upgrading XenServer Versions."

#. 

   Now apply the XenServer hotfix XS602E003 (and any other needed
   hotfixes) to XenServer v6.0.2 hypervisor hosts.

   #. 

      Disconnect the XenServer cluster from CloudStack.

      In the left navigation bar of the CloudStack UI, select
      Infrastructure. Under Clusters, click View All. Select the
      XenServer cluster and click Actions - Unmanage.

      This may fail if there are hosts not in one of the states Up,
      Down, Disconnected, or Alert. You may need to fix that before
      unmanaging this cluster.

      Wait until the status of the cluster has reached Unmanaged. Use
      the CloudStack UI to check on the status. When the cluster is in
      the unmanaged state, there is no connection to the hosts in the
      cluster.

   #. 

      To clean up the VLAN, log in to one XenServer host and run:

      ``/opt/xensource/bin/cloud-clean-vlan.sh``

   #. 

      Now prepare the upgrade by running the following on one XenServer
      host:

      ``/opt/xensource/bin/cloud-prepare-upgrade.sh``

      If you see a message like "can't eject CD", log in to the VM and
      unmount the CD, then run this script again.

   #. 

      Upload the hotfix to the XenServer hosts. Always start with the
      Xen pool master, then the slaves. Using your favorite file copy
      utility (e.g. WinSCP), copy the hotfixes to the host. Place them
      in a temporary folder such as /tmp.

      On the Xen pool master, upload the hotfix with this command:

      ``xe patch-upload file-name=XS602E003.xsupdate``

      Make a note of the output from this command, which is a UUID for
      the hotfix file. You'll need it in another step later.

      .. note:: (Optional) If you are applying other hotfixes as well, you can repeat the commands in this section with the appropriate hotfix number. For example, XS602E004.xsupdate.

   #. 

      Manually live migrate all VMs on this host to another host. First,
      get a list of the VMs on this host:

      ``# xe vm-list``

      Then use this command to migrate each VM. Replace the example host
      name and VM name with your own:

      ``# xe vm-migrate live=true host=host-name`` vm=\ *``VM-name``*

      .. note:: **Troubleshooting:** If you see a message like "You attempted an operation on a VM which requires PV drivers to be installed but the drivers were not detected," run: ``/opt/xensource/bin/make_migratable.sh b6cf79c8-02ee-050b-922f-49583d9f1a14``.

   #. 

      Apply the hotfix. First, get the UUID of this host:

      .. sourcecode:: bash

          # xe host-list

      Then use the following command to apply the hotfix. Replace the
      example host UUID with the current host ID, and replace the hotfix
      UUID with the output from the patch-upload command you ran on this
      machine earlier. You can also get the hotfix UUID by running xe
      patch-list.

      .. sourcecode:: bash

          xe patch-apply host-uuid=host-uuid uuid=hotfix-uuid

   #. 

      Copy the following files from the CloudStack Management Server to
      the host.


       +-------------------------+-------------------------------------------------+
       | Copy from here...       | ...to here                                      |
       +=========================+=================================================+
       | /usr/lib64/cloud/common | /opt/xensource/sm/NFSSR.py                      |
       | /scripts/vm/hypervisor/ |                                                 |
       | xenserver/xenserver60/N |                                                 |
       | FSSR.py                 |                                                 |
       +-------------------------+-------------------------------------------------+
       | /usr/lib64/cloud/common | /opt/xensource/bin/setupxenserver.sh            |
       | /scripts/vm/hypervisor/ |                                                 |
       | xenserver/setupxenserve |                                                 |
       | r.sh                    |                                                 |
       +-------------------------+-------------------------------------------------+
       | /usr/lib64/cloud/common | /opt/xensource/bin/make\_migratable.sh          |
       | /scripts/vm/hypervisor/ |                                                 |
       | xenserver/make\_migrata |                                                 |
       | ble.sh                  |                                                 |
       +-------------------------+-------------------------------------------------+


   #. 

      (Only for hotfixes XS602E005 and XS602E007) You need to apply a
      new Cloud Support Pack.

      -  

         Download the CSP software onto the XenServer host from one of
         the following links:

         For hotfix XS602E005:
         `http://coltrane.eng.hq.xensource.com/release/XenServer-6.x/XS-6.0.2/hotfixes/XS602E005/56710/xe-phase-2/xenserver-cloud-supp.tgz <http://coltrane.eng.hq.xensource.com/release/XenServer-6.x/XS-6.0.2/hotfixes/XS602E005/56710/xe-phase-2/xenserver-cloud-supp.tgz>`__

         For hotfix XS602E007:
         `http://coltrane.eng.hq.xensource.com/release/XenServer-6.x/XS-6.0.2/hotfixes/XS602E007/57824/xe-phase-2/xenserver-cloud-supp.tgz <http://coltrane.eng.hq.xensource.com/release/XenServer-6.x/XS-6.0.2/hotfixes/XS602E007/57824/xe-phase-2/xenserver-cloud-supp.tgz>`__

      -  

         Extract the file:

         .. sourcecode:: bash

             # tar xf xenserver-cloud-supp.tgz

      -  

         Run the following script:

         .. sourcecode:: bash

             # xe-install-supplemental-pack xenserver-cloud-supp.iso

      -  

         If the XenServer host is part of a zone that uses basic
         networking, disable Open vSwitch (OVS):

         .. sourcecode:: bash

             # xe-switch-network-backend  bridge

   #. 

      Reboot this XenServer host.

   #. 

      Run the following:

      .. sourcecode:: bash

          /opt/xensource/bin/setupxenserver.sh

      .. note:: If the message "mv: cannot stat \`/etc/cron.daily/logrotate': No such file or directory" appears, you can safely ignore it.

   #. 

      Run the following:

      .. sourcecode:: bash

          for pbd in `xe pbd-list currently-attached=false| grep ^uuid | awk '{print $NF}'`; do xe pbd-plug uuid=$pbd ;

   #. 

      On each slave host in the Xen pool, repeat these steps, starting
      from "manually live migrate VMs."

.. note:: **Troubleshooting Tip:** If passwords which you know to be valid appear not to work after upgrade, or other UI issues are seen, try clearing your browser cache and reloading the UI page.

Upgrade from 2.2.14 to 4.3
--------------------------

#. 

   Ensure that you query your IPaddress usage records and process them;
   for example, issue invoices for any usage that you have not yet
   billed users for.

   Starting in 3.0.2, the usage record format for IP addresses is the
   same as the rest of the usage types. Instead of a single record with
   the assignment and release dates, separate records are generated per
   aggregation period with start and end dates. After upgrading to 4.3,
   any existing IP address usage records in the old format will no
   longer be available.

#. 

   If you are using version 2.2.0 - 2.2.13, first upgrade to 2.2.14 by
   using the instructions in the `2.2.14 Release
   Notes <http://download.cloud.com/releases/2.2.0/CloudStack2.2.14ReleaseNotes.pdf>`__.

   .. warning:: **KVM Hosts:** If KVM hypervisor is used in your cloud, be sure you completed the step to insert a valid username and password into the host\_details table on each KVM node as described in the 2.2.14 Release Notes. This step is critical, as the database will be encrypted after the upgrade to 4.3.

#. 

   While running the 2.2.14 system, log in to the UI as root
   administrator.

#. 

   Using the UI, add a new System VM template for each hypervisor type
   that is used in your cloud. In each zone, add a system VM template
   for each hypervisor used in that zone

   #. 

      In the left navigation bar, click Templates.

   #. 

      In Select view, click Templates.

   #. 

      Click Register template.

      The Register template dialog box is displayed.

   #. 

      In the Register template dialog box, specify the following values
      depending on the hypervisor type (do not change these):

      .. include:: upgrade/_templates.rst


#. 

   Watch the screen to be sure that the template downloads successfully
   and enters the READY state. Do not proceed until this is successful

#. 

   **WARNING**: If you use more than one type of hypervisor in your
   cloud, be sure you have repeated these steps to download the system
   VM template for each hypervisor type. Otherwise, the upgrade will
   fail.

#. 

   (KVM on RHEL 6.0/6.1 only) If your existing CloudStack deployment
   includes one or more clusters of KVM hosts running RHEL 6.0 or RHEL
   6.1, perform the following:

   #. 

      Ensure that you upgrade the operating system version on those
      hosts before upgrading CloudStack

      To do that, change the yum repository for each system with
      CloudStack packages, that implies that all the Management Servers
      and any hosts that have the KVM agent.

   #. 

      Open ``/etc/yum.repos.d/cloudstack.repo`` on any systems that have
      CloudStack packages installed.

   #. 

      Edit as follows:

      .. sourcecode:: bash

                      [upgrade]
                      name=rhel63
                      baseurl=url-of-your-rhel6.3-repo
                      enabled=1
                      gpgcheck=0
                      [apache CloudStack]
                      name= Apache CloudStack
                      baseurl= http://cloudstack.apt-get.eu/rhel/4.2/
                      enabled=1
                      gpgcheck=0

      If you are using the community provided package repository, change
      the baseurl to http:// cloudstack.apt-get.eu/rhel/4.2/

      If you are using your own package repository, change this line to
      read as appropriate for your 4.2 repository.

   #. 

      Now that you have the repository configured, upgrade the host
      operating system from RHEL 6.0 to 6.3:

      .. sourcecode:: bash

          # yum upgrade

#. 

   Stop all Usage Servers if running. Run this on all Usage Server
   hosts.

   .. sourcecode:: bash

       # service cloud-usage stop

#. 

   Stop the Management Servers. Run this on all Management Server hosts.

   .. sourcecode:: bash

       # service cloud-management stop

#. 

   On the MySQL master, take a backup of the MySQL databases. We
   recommend performing this step even in test upgrades. If there is an
   issue, this will assist with debugging.

   In the following commands, it is assumed that you have set the root
   password on the database, which is a CloudStack recommended best
   practice. Substitute your own MySQL root password.

   .. sourcecode:: bash

       # mysqldump -u root -pmysql_password cloud > cloud-backup.dmp
                               # mysqldump -u root -pmysql_password cloud_usage > cloud-usage-backup.dmp

#. 

   Either build RPM/DEB packages as detailed in the Installation Guide,
   or use one of the community provided yum/apt repositories to gain
   access to the CloudStack binaries.

#. 

   If you are using Ubuntu, follow this procedure to upgrade your
   packages. If not, skip to step `13 <#upgrade-rpm-packages-22>`__.

   .. note:: **Community Packages:** This section assumes you're using the community supplied packages for CloudStack. If you've created your own packages and APT repository, substitute your own URL for the ones used in these examples.

   #. 

      The first order of business will be to change the sources list for
      each system with CloudStack packages. This means all management
      servers, and any hosts that have the KVM agent. (No changes should
      be necessary for hosts that are running VMware or Xen.)

      Start by opening ``/etc/apt/sources.list.d/cloudstack.list`` on
      any systems that have CloudStack packages installed.

      This file should have one line, which contains:

      .. sourcecode:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.0

      We'll change it to point to the new package repository:

      .. sourcecode:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.3

      If you're using your own package repository, change this line to
      read as appropriate for your 4.2 repository.

   #. 

      Now update your apt package list:

      .. sourcecode:: bash

          $ sudo apt-get update

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package. This will pull in any other
      dependencies you need.

      .. sourcecode:: bash

          $ sudo apt-get install cloudstack-management

   #. 

      On KVM hosts, you will need to manually install the
      ``cloudstack-agent`` package:

      .. sourcecode:: bash

          $ sudo apt-get install cloudstack-agent

      During the installation of ``cloudstack-agent``, APT will copy
      your ``agent.properties``, ``log4j-cloud.xml``, and
      ``environment.properties`` from ``/etc/cloud/agent`` to
      ``/etc/cloudstack/agent``.

      When prompted whether you wish to keep your configuration, say
      Yes.

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. sourcecode:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. sourcecode:: bash

          service cloud-agent stop
          killall jsvc
          service cloudstack-agent start

   #. 

      During the upgrade, ``log4j-cloud.xml`` was simply copied over, so
      the logs will continue to be added to
      ``/var/log/cloud/agent/agent.log``. There's nothing *wrong* with
      this, but if you prefer to be consistent, you can change this by
      copying over the sample configuration file:

      .. sourcecode:: bash

          cd /etc/cloudstack/agent
          mv log4j-cloud.xml.dpkg-dist log4j-cloud.xml
          service cloudstack-agent restart

   #. 

      Once the agent is running, you can uninstall the old cloud-\*
      packages from your system:

      .. sourcecode:: bash

          sudo dpkg --purge cloud-agent

#. 

   If you are using CentOS or RHEL, follow this procedure to upgrade
   your packages. If not, skip to step
   `14 <#correct-components-xml-22>`__.

   .. note:: **Community Packages:** This section assumes you're using the community supplied packages for CloudStack. If you've created your own packages and yum repository, substitute your own URL for the ones used in these examples.

   #. 

      The first order of business will be to change the yum repository
      for each system with CloudStack packages. This means all
      management servers, and any hosts that have the KVM agent. (No
      changes should be necessary for hosts that are running VMware or
      Xen.)

      Start by opening ``/etc/yum.repos.d/cloudstack.repo`` on any
      systems that have CloudStack packages installed.

      This file should have content similar to the following:

      .. sourcecode:: bash

          [apache-cloudstack]
          name=Apache CloudStack
          baseurl=http://cloudstack.apt-get.eu/rhel/4.0/
          enabled=1
          gpgcheck=0

      If you are using the community provided package repository, change
      the baseurl to http://cloudstack.apt-get.eu/rhel/4.2/

      If you're using your own package repository, change this line to
      read as appropriate for your 4.3 repository.

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package by upgrading the older
      ``cloud-client`` package.

      .. sourcecode:: bash

          $ sudo yum upgrade cloud-client

   #. 

      For KVM hosts, you will need to upgrade the ``cloud-agent``
      package, similarly installing the new version as
      ``cloudstack-agent``.

      .. sourcecode:: bash

          $ sudo yum upgrade cloud-agent

      During the installation of ``cloudstack-agent``, the RPM will copy
      your ``agent.properties``, ``log4j-cloud.xml``, and
      ``environment.properties`` from ``/etc/cloud/agent`` to
      ``/etc/cloudstack/agent``.

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. sourcecode:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. sourcecode:: bash

          service cloud-agent stop
          killall jsvc
          service cloudstack-agent start

#. 

   If you have made changes to your existing copy of the file
   components.xml in your previous-version CloudStack installation, the
   changes will be preserved in the upgrade. However, you need to do the
   following steps to place these changes in a new version of the file
   which is compatible with version 4.0.0-incubating.

   .. note:: How will you know whether you need to do this? If the upgrade output in the previous step included a message like the following, then some custom content was found in your old components.xml, and you need to merge the two files:

   .. sourcecode:: bash

       warning: /etc/cloud/management/components.xml created as 
       /etc/cloud/management/components.xml.rpmnew

   #. 

      Make a backup copy of your
      ``/etc/cloud/management/components.xml`` file. For example:

      .. sourcecode:: bash

          # mv /etc/cloud/management/components.xml /etc/cloud/management/components.xml-backup

   #. 

      Copy ``/etc/cloud/management/components.xml.rpmnew`` to create a
      new ``/etc/cloud/management/components.xml``:

      .. sourcecode:: bash

          # cp -ap /etc/cloud/management/components.xml.rpmnew /etc/cloud/management/components.xml

   #. 

      Merge your changes from the backup file into the new
      components.xml file.

      .. sourcecode:: bash

          # vi /etc/cloudstack/management/components.xml

#. 

   After upgrading to 4.3, API clients are expected to send plain text
   passwords for login and user creation, instead of MD5 hash. If API
   client changes are not acceptable, following changes are to be made
   for backward compatibility:

   Modify componentContext.xml, and make PlainTextUserAuthenticator as
   the default authenticator (1st entry in the userAuthenticators
   adapter list is default)

   .. sourcecode:: xml

       <!-- Security adapters -->
       <bean id="userAuthenticators" 
                       class="com.cloud.utils.component.AdapterList">
         <property name="Adapters">
           <list>
             <ref bean="PlainTextUserAuthenticator"/>
             <ref bean="MD5UserAuthenticator"/>
             <ref bean="LDAPUserAuthenticator"/>
           </list>
         </property>
       </bean>

   PlainTextUserAuthenticator works the same way MD5UserAuthenticator
   worked prior to 4.2.

#. 

   If you have made changes to your existing copy of the
   ``/etc/cloud/management/db.properties`` file in your previous-version
   CloudStack installation, the changes will be preserved in the
   upgrade. However, you need to do the following steps to place these
   changes in a new version of the file which is compatible with this
   version.

   #. 

      Make a backup copy of your file
      ``/etc/cloud/management/db.properties``. For example:

      .. sourcecode:: bash

          # mv /etc/cloud/management/db.properties /etc/cloud/management/db.properties-backup

   #. 

      Copy ``/etc/cloud/management/db.properties.rpmnew`` to create a
      new ``/etc/cloud/management/db.properties``:

      .. sourcecode:: bash

          # cp -ap /etc/cloud/management/db.properties.rpmnew etc/cloud/management/db.properties

   #. 

      Merge your changes from the backup file into the new db.properties
      file.

      .. sourcecode:: bash

          # vi /etc/cloudstack/management/db.properties

#. 

   On the management server node, run the following command. It is
   recommended that you use the command-line flags to provide your own
   encryption keys. See Password and Key Encryption in the Installation
   Guide.

   .. sourcecode:: bash

       # cloudstack-setup-encryption -e encryption_type -m management_server_key -k database_key

   When used without arguments, as in the following example, the default
   encryption type and keys will be used:

   -  

      (Optional) For encryption\_type, use file or web to indicate the
      technique used to pass in the database encryption password.
      Default: file.

   -  

      (Optional) For management\_server\_key, substitute the default key
      that is used to encrypt confidential parameters in the properties
      file. Default: password. It is highly recommended that you replace
      this with a more secure value

   -  

      (Optional) For database\_key, substitute the default key that is
      used to encrypt confidential parameters in the CloudStack
      database. Default: password. It is highly recommended that you
      replace this with a more secure value.

#. 

   Repeat steps 10 - 14 on every management server node. If you provided
   your own encryption key in step 14, use the same key on all other
   management servers.

#. 

   Start the first Management Server. Do not start any other Management
   Server nodes yet.

   .. sourcecode:: bash

       # service cloudstack-management start

   Wait until the databases are upgraded. Ensure that the database
   upgrade is complete. You should see a message like "Complete! Done."
   After confirmation, start the other Management Servers one at a time
   by running the same command on each node.

#. 

   Start all Usage Servers (if they were running on your previous
   version). Perform this on each Usage Server host.

   .. sourcecode:: bash

       # service cloudstack-usage start

#. 

   (KVM only) Perform the following additional steps on each KVM host.

   These steps will not affect running guests in the cloud. These steps
   are required only for clouds using KVM as hosts and only on the KVM
   hosts.

   #. 

      Configure your CloudStack package repositories as outlined in the
      Installation Guide

   #. 

      Stop the running agent.

      .. sourcecode:: bash

          # service cloud-agent stop

   #. 

      Update the agent software with one of the following command sets
      as appropriate.

      .. sourcecode:: bash

          # yum update cloud-*

      .. sourcecode:: bash

           # apt-get update
           # apt-get upgrade cloud-*

   #. 

      Copy the contents of the ``agent.properties`` file to the new
      ``agent.properties`` file by using the following command

      .. sourcecode:: bash

          sed -i 's/com.cloud.agent.resource.computing.LibvirtComputingResource/com.cloud.hypervisor.kvm.resource.LibvirtComputingResource/g' /etc/cloudstack/agent/agent.properties

   #. 

      Upgrade all the existing bridge names to new bridge names by
      running this script:

      .. sourcecode:: bash

           # cloudstack-agent-upgrade

   #. 

      Install a libvirt hook with the following commands:

      .. sourcecode:: bash

           # mkdir /etc/libvirt/hooks
           # cp /usr/share/cloudstack-agent/lib/libvirtqemuhook /etc/libvirt/hooks/qemu
           # chmod +x /etc/libvirt/hooks/qemu

   #. 

      Restart libvirtd.

      .. sourcecode:: bash

          # service libvirtd restart

   #. 

      Start the agent.

      .. sourcecode:: bash

          # service cloudstack-agent start

   #. 

      When the Management Server is up and running, log in to the
      CloudStack UI and restart the virtual router for proper
      functioning of all the features.

#. 

   Log in to the CloudStack UI as admin, and check the status of the
   hosts. All hosts should come to Up state (except those that you know
   to be offline). You may need to wait 20 or 30 minutes, depending on
   the number of hosts.

   Do not proceed to the next step until the hosts show in the Up state.
   If the hosts do not come to the Up state, contact support.

#. 

   Run the following script to stop, then start, all Secondary Storage
   VMs, Console Proxy VMs, and virtual routers.

   #. 

      Run the command once on one management server. Substitute your own
      IP address of the MySQL instance, the MySQL user to connect as,
      and the password to use for that user. In addition to those
      parameters, provide the "-c" and "-r" arguments. For example:

      .. sourcecode:: bash

          # nohup cloudstack-sysvmadm -d 192.168.1.5 -u cloud -p password -c -r > sysvm.log 2>&1 &
          # tail -f sysvm.log

      This might take up to an hour or more to run, depending on the
      number of accounts in the system.

   #. 

      After the script terminates, check the log to verify correct
      execution:

      .. sourcecode:: bash

          # tail -f sysvm.log

      The content should be like the following:

      .. sourcecode:: bash

                                          Stopping and starting 1 secondary storage vm(s)...
                                          Done stopping and starting secondary storage vm(s)
                                          Stopping and starting 1 console proxy vm(s)...
                                          Done stopping and starting console proxy vm(s).
                                          Stopping and starting 4 running routing vm(s)...
                                          Done restarting router(s).

#. 

   If you would like additional confirmation that the new system VM
   templates were correctly applied when these system VMs were rebooted,
   SSH into the System VM and check the version.

   Use one of the following techniques, depending on the hypervisor.

   **XenServer or KVM:**

   SSH in by using the link local IP address of the system VM. For
   example, in the command below, substitute your own path to the
   private key used to log in to the system VM and your own link local
   IP.

   Run the following commands on the XenServer or KVM host on which the
   system VM is present:

   .. sourcecode:: bash

       # ssh -i private-key-path link-local-ip -p 3922
                               # cat /etc/cloudstack-release

   The output should be like the following:

   .. sourcecode:: bash

       Cloudstack Release 4.0.0-incubating Mon Oct 9 15:10:04 PST 2012

   **ESXi:**

   SSH in using the private IP address of the system VM. For example, in
   the command below, substitute your own path to the private key used
   to log in to the system VM and your own private IP.

   Run the following commands on the Management Server:

   .. sourcecode:: bash

       # ssh -i private-key-path private-ip -p 3922
                               # cat /etc/cloudstack-release

   The output should be like the following:

   .. sourcecode:: bash

       Cloudstack Release 4.0.0-incubating Mon Oct 9 15:10:04 PST 2012

#. 

   If needed, upgrade all Citrix XenServer hypervisor hosts in your
   cloud to a version supported by CloudStack 4.0.0-incubating. The
   supported versions are XenServer 5.6 SP2 and 6.0.2. Instructions for
   upgrade can be found in the CloudStack 4.0.0-incubating Installation
   Guide.

#. 

   Apply the XenServer hotfix XS602E003 (and any other needed hotfixes)
   to XenServer v6.0.2 hypervisor hosts.

   #. 

      Disconnect the XenServer cluster from CloudStack.

      In the left navigation bar of the CloudStack UI, select
      Infrastructure. Under Clusters, click View All. Select the
      XenServer cluster and click Actions - Unmanage.

      This may fail if there are hosts not in one of the states Up,
      Down, Disconnected, or Alert. You may need to fix that before
      unmanaging this cluster.

      Wait until the status of the cluster has reached Unmanaged. Use
      the CloudStack UI to check on the status. When the cluster is in
      the unmanaged state, there is no connection to the hosts in the
      cluster.

   #. 

      To clean up the VLAN, log in to one XenServer host and run:

      .. sourcecode:: bash

          /opt/xensource/bin/cloud-clean-vlan.sh

   #. 

      Prepare the upgrade by running the following on one XenServer
      host:

      .. sourcecode:: bash

          /opt/xensource/bin/cloud-prepare-upgrade.sh

      If you see a message like "can't eject CD", log in to the VM and
      umount the CD, then run this script again.

   #. 

      Upload the hotfix to the XenServer hosts. Always start with the
      Xen pool master, then the slaves. Using your favorite file copy
      utility (e.g. WinSCP), copy the hotfixes to the host. Place them
      in a temporary folder such as /root or /tmp.

      On the Xen pool master, upload the hotfix with this command:

      .. sourcecode:: bash

          xe patch-upload file-name=XS602E003.xsupdate

      Make a note of the output from this command, which is a UUID for
      the hotfix file. You'll need it in another step later.

      .. note:: (Optional) If you are applying other hotfixes as well, you can repeat the commands in this section with the appropriate hotfix number. For example, XS602E004.xsupdate.

   #. 

      Manually live migrate all VMs on this host to another host. First,
      get a list of the VMs on this host:

      .. sourcecode:: bash

          # xe vm-list

      Then use this command to migrate each VM. Replace the example host
      name and VM name with your own:

      .. sourcecode:: bash

          # xe vm-migrate live=true host=host-name vm=VM-name

      .. note:: **Troubleshooting:** If you see a message like "You attempted an operation on a VM which requires PV drivers to be installed but the drivers were not detected," run: ``/opt/xensource/bin/make_migratable.sh b6cf79c8-02ee-050b-922f-49583d9f1a14``.

   #. 

      Apply the hotfix. First, get the UUID of this host:

      ``# xe host-list``

      Then use the following command to apply the hotfix. Replace the
      example host UUID with the current host ID, and replace the hotfix
      UUID with the output from the patch-upload command you ran on this
      machine earlier. You can also get the hotfix UUID by running xe
      patch-list.

      ``xe patch-apply host-uuid=host-uuid`` uuid=\ *``hotfix-uuid``*

   #. 

      Copy the following files from the CloudStack Management Server to
      the host.

       +-------------------------+-------------------------------------------------+
       | Copy from here...       | ...to here                                      |
       +=========================+=================================================+
       | ``/usr/share/cloudstack | ``/opt/xensource/sm/NFSSR.py``                  |
       | -common/scripts/vm/hype |                                                 |
       | rvisor/xenserver/xenser |                                                 |
       | ver60/NFSSR.py``        |                                                 |
       +-------------------------+-------------------------------------------------+
       | ``/usr/share/cloudstack | ``/opt/xensource/bin/setupxenserver.sh``        |
       | -common/scripts/vm/hype |                                                 |
       | rvisor/xenserver/setupx |                                                 |
       | enserver.sh``           |                                                 |
       +-------------------------+-------------------------------------------------+
       | ``/usr/lib64/cloudstack | ``/opt/xensource/bin/make_migratable.sh``       |
       | -common/scripts/vm/hype |                                                 |
       | rvisor/xenserver/make_m |                                                 |
       | igratable.sh``          |                                                 |
       +-------------------------+-------------------------------------------------+

   #. 

      (Only for hotfixes XS602E005 and XS602E007) You need to apply a
      new Cloud Support Pack.

      -  

         Download the CSP software onto the XenServer host from one of
         the following links:

         For hotfix XS602E005:
         `http://coltrane.eng.hq.xensource.com/release/XenServer-6.x/XS-6.0.2/hotfixes/XS602E005/56710/xe-phase-2/xenserver-cloud-supp.tgz <http://coltrane.eng.hq.xensource.com/release/XenServer-6.x/XS-6.0.2/hotfixes/XS602E005/56710/xe-phase-2/xenserver-cloud-supp.tgz>`__

         For hotfix XS602E007:
         `http://coltrane.eng.hq.xensource.com/release/XenServer-6.x/XS-6.0.2/hotfixes/XS602E007/57824/xe-phase-2/xenserver-cloud-supp.tgz <http://coltrane.eng.hq.xensource.com/release/XenServer-6.x/XS-6.0.2/hotfixes/XS602E007/57824/xe-phase-2/xenserver-cloud-supp.tgz>`__

      -  

         Extract the file:

         ``# tar xf xenserver-cloud-supp.tgz``

      -  

         Run the following script:

         ``# xe-install-supplemental-pack xenserver-cloud-supp.iso``

      -  

         If the XenServer host is part of a zone that uses basic
         networking, disable Open vSwitch (OVS):

         ``# xe-switch-network-backend bridge``

   #. 

      Reboot this XenServer host.

   #. 

      Run the following:

      ``/opt/xensource/bin/setupxenserver.sh``

      .. note:: If the message "mv: cannot stat \`/etc/cron.daily/logrotate': No such file or directory" appears, you can safely ignore it.

   #. 

      Run the following:

      .. sourcecode:: bash

        ``for pbd in `xe pbd-list currently-attached=false| grep ^uuid | awk '{print $NF}'`; do xe pbd-plug uuid=$pbd ; ``

   #. 

      On each slave host in the Xen pool, repeat these steps, starting
      from "manually live migrate VMs."


.. include:: /global.rst