Upgrade Instruction from 4.1.x
-------------------------------

This section contains upgrade instructions from prior versions of
CloudStack to Apache CloudStack |version|. We include instructions on
upgrading to Apache CloudStack from pre-Apache versions of Citrix
CloudStack (last version prior to Apache is 3.0.2) and from the releases
made while CloudStack was in the Apache Incubator.

If you run into any issues during upgrades, please feel free to ask
questions on users@cloudstack.apache.org or dev@cloudstack.apache.org.

.. warning::
   :name: Depreciation of realhostip.com DNS and SSL certificate
   
   The realhostip.com dynamic DNS resolution service is being retired this
   summer. In advance of that, CloudStack 4.3 and later no longer uses realhostip.com
   DNS domains or SSL certificates to encrypt Console Proxy or file copy
   communications.


This section will guide you from CloudStack 4.1.x versions to CloudStack |version|.

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

      .. include:: /systemvm_templates.rst


#. 

   Create RPM or Debian packages (as appropriate) and a repository from
   the 4.3.0 source, or check the Apache CloudStack downloads page at
   `http://cloudstack.apache.org/downloads.html <http://cloudstack.apache.org/downloads.html>`__
   for package repositories supplied by community members. You will need
   them for step `8 <#upgrade-deb-packages-41to42>`__ or step
   `11 <#upgrade-rpm-packages-41to43>`__.

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
      read as appropriate for your |version| repository.

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
          baseurl=http://cloudstack.apt-get.eu/rhel/4.0/
          enabled=1
          gpgcheck=0

      If you are using the community provided package repository, change
      the base url to http://cloudstack.apt-get.eu/rhel/4.3/

      If you're using your own package repository, change this line to
      read as appropriate for your |version| repository.

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

.. include:: /global.rst