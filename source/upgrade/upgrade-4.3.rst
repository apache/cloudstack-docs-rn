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


.. |version_to_upgrade| replace:: 4.3.x

Upgrade Instruction from |version_to_upgrade|
=============================================

.. warning::
   A recently found systemvm upgrade require manual MySQL 
   commands in order to allow upgrade of SystemVMs and Virtual Routers.

   Dependency to Java 1.7 inside SystemVM require Upgrade of systemvm-template. 
   Templates version 4.4.0-6 must be use with CloudStack 4.4.0.

   Refer to: :ref:`manual_hofix`


This section will guide you from CloudStack |version_to_upgrade| to CloudStack 
|version|.

Any steps that are hypervisor-specific will be called out with a note.

We recommend reading through this section once or twice before beginning
your upgrade procedure, and working through it on a test system before
working on a production system.

.. note:: 
   The following upgrade instructions should be performed regardless of 
   hypervisor type.

Upgrade Steps:

#. Backup CloudStack database (MySQL)

#. Upgrade CloudStack management server(s)

#. Update hypervisors specific dependencies


Packages repository
-------------------

Most users of CloudStack manage the installation and upgrades of
CloudStack with one of Linux's predominant package systems, RPM or
APT. This guide assumes you'll be using RPM and Yum (for Red Hat
Enterprise Linux or CentOS), or APT and Debian packages (for Ubuntu).

Create RPM or Debian packages (as appropriate) and a repository from
the |version| source, or check the Apache CloudStack downloads page at
http://cloudstack.apache.org/downloads.html
for package repositories supplied by community members. You will need
them for :ref:`ubuntu43` or :ref:`rhel43` and :ref:`kvm43` hosts upgrade. 

Instructions for creating packages from the CloudStack source are in the 
`CloudStack Installation Guide`_.

.. include:: _sysvm_templates.rst


Database Preparation
--------------------

Backup current database

#. Stop your management server or servers. Run this on all management
   server hosts:

   .. sourcecode:: bash

      $ sudo service cloudstack-management stop

#. If you are running a usage server or usage servers, stop those as well:

   .. sourcecode:: bash

      $ sudo service cloudstack-usage stop

#. Make a backup of your MySQL database. If you run into any issues or
   need to roll back the upgrade, this will assist in debugging or
   restoring your existing environment. You'll be prompted for your
   password.

   .. sourcecode:: bash

      $ mysqldump -u root -p cloud > cloudstack-backup.sql
      $ mysqldump -u root -p cloud_usage > cloud_usage-backup.sql

#. **(KVM Only)** If primary storage of type local storage is in use, the
   path for this storage needs to be verified to ensure it passes new
   validation. Check local storage by querying the cloud.storage\_pool
   table:

   .. sourcecode:: bash

      $ mysql -u cloud -p -e "select id,name,path from cloud.storage_pool where pool_type='Filesystem'"

   If local storage paths are found to have a trailing forward slash,
   remove it:

   .. sourcecode:: bash

      $ mysql -u cloud -p -e 'update cloud.storage_pool set path="/var/lib/libvirt/images" where path="/var/lib/libvirt/images/"';


.. _ubuntu43:

Management Server on Ubuntu
---------------------------

If you are using Ubuntu, follow this procedure to upgrade your packages. If 
not, skip to step :ref:`rhel43`.

.. note:: 
   **Community Packages:** This section assumes you're using the community 
   supplied packages for CloudStack. If you've created your own packages and 
   APT repository, substitute your own URL for the ones used in these examples.

The first order of business will be to change the sources list for
each system with CloudStack packages. This means all management
servers, and any hosts that have the KVM agent. (No changes should
be necessary for hosts that are running VMware or Xen.)


.. _apt-repo43:

CloudStack apt repository
^^^^^^^^^^^^^^^^^^^^^^^^^

   Start by opening ``/etc/apt/sources.list.d/cloudstack.list`` on
   any systems that have CloudStack packages installed.
   
   This file should have one line, which contains:
   
   .. sourcecode:: bash
   
      deb http://cloudstack.apt-get.eu/ubuntu precise 4.3
   
   We'll change it to point to the new package repository:
   
   .. sourcecode:: bash
   
      deb http://cloudstack.apt-get.eu/ubuntu precise 4.4
   
   If you're using your own package repository, change this line to
   read as appropriate for your |version| repository.

#. Now update your apt package list:

   .. sourcecode:: bash

      $ sudo apt-get update

#. Now that you have the repository configured, it's time to upgrade
   the ``cloudstack-management`` package. 

   .. sourcecode:: bash

      $ sudo apt-get upgrade cloudstack-management

#. If you use CloudStack usage server

   .. sourcecode:: bash

      $ sudo apt-get upgrade cloudstack-usage


.. _rhel43:

Management Server on CentOS/RHEL
--------------------------------

If you are using CentOS or RHEL, follow this procedure to upgrade your 
packages. If not, skip to hypervisors section, then :ref:`upg-sysvm43`.

.. note:: 
   **Community Packages:** This section assumes you're using the community 
   supplied packages for CloudStack. If you've created your own packages and 
   yum repository, substitute your own URL for the ones used in these examples.


.. _rpm-repo43:

CloudStack RPM repository
^^^^^^^^^^^^^^^^^^^^^^^^^^

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
      baseurl=http://cloudstack.apt-get.eu/rhel/4.3/
      enabled=1
      gpgcheck=0

   If you are using the community provided package repository, change
   the base url to ``http://cloudstack.apt-get.eu/rhel/4.4/``

   If you're using your own package repository, change this line to
   read as appropriate for your |version| repository.


#. Now that you have the repository configured, it's time to upgrade the 
   ``cloudstack-management``.

   .. sourcecode:: bash

      $ sudo yum upgrade cloudstack-management

#. If you use CloudStack usage server

   .. sourcecode:: bash

      $ sudo yum upgrade cloudstack-usage


Hypervisor: XenServer
---------------------

   **(XenServer only)** Copy vhd-utils file on CloudStack management servers.
   Copy the file `vhd-utils <http://download.cloud.com.s3.amazonaws.com/tools/vhd-util>`_ 
   to ``/usr/share/cloudstack-common/scripts/vm/hypervisor/xenserver``.

   .. sourcecode:: bash

      wget -P /usr/share/cloudstack-common/scripts/vm/hypervisor/xenserver \
      http://download.cloud.com.s3.amazonaws.com/tools/vhd-util


Hypervisor: VMware
------------------

   .. warning::
      For VMware hypervisor CloudStack management server packages must be 
      build using "noredist". Refer to `Building from Source 
      <http://docs.cloudstack.apache.org/projects/cloudstack-installation/en/latest/building_from_source.html>`_.

   **(VMware only)** Additional steps are required for each VMware cluster.
   These steps will not affect running guests in the cloud. These steps
   are required only for clouds using VMware clusters:

#. Stop the Management Server:

   .. sourcecode:: bash

      $ sudo service cloudstack-management stop

#. Generate the encrypted equivalent of your vCenter password:

   .. sourcecode:: bash

      $ java -classpath /usr/share/cloudstack-common/lib/jasypt-1.9.0.jar org.jasypt.intf.cli.JasyptPBEStringEncryptionCLI encrypt.sh input="_your_vCenter_password_" password="`cat /etc/cloudstack/management/key`" verbose=false

   Store the output from this step, we need to add this in
   cluster\_details table and vmware\_data\_center tables in place of
   the plain text password

#. Find the ID of the row of cluster\_details table that you have to
   update:

   .. sourcecode:: bash

      $ mysql -u <username> -p<password>

   .. sourcecode:: bash

      select * from cloud.cluster_details;

#. Update the plain text password with the encrypted one

   .. sourcecode:: bash

      update cloud.cluster_details set value = '_ciphertext_from_step_1_' where id = _id_from_step_2_;

#. Confirm that the table is updated:

   .. sourcecode:: bash

      select * from cloud.cluster_details;

#. Find the ID of the correct row of vmware\_data\_center that you
   want to update

   .. sourcecode:: bash

      select * from cloud.vmware_data_center;

#. update the plain text password with the encrypted one:

   .. sourcecode:: bash

      update cloud.vmware_data_center set password = '_ciphertext_from_step_1_' where id = _id_from_step_5_;

#. Confirm that the table is updated:

   .. sourcecode:: bash

      select * from cloud.vmware_data_center;


.. _kvm43:

Hypervisor: KVM
---------------

KVM on Ubuntu
^^^^^^^^^^^^^

(KVM only) Additional steps are required for each KVM host. These
steps will not affect running guests in the cloud. These steps are
required only for clouds using KVM as hosts and only on the KVM
hosts.

#. Configure the :ref:`apt-repo43` as detailed above.

#. Stop the running agent.

   .. sourcecode:: bash

      $ sudo service cloudstack-agent stop

#. Update the agent software.

   .. sourcecode:: bash

      $ sudo apt-get upgrade cloudstack-agent

#. Verify that the file ``/etc/cloudstack/agent/environment.properties`` has a 
   line that reads:

   .. sourcecode:: bash

      paths.script=/usr/share/cloudstack-common

   If not, add the line.

#. Start the agent.

   .. sourcecode:: bash

      $ sudo service cloudstack-agent start


KVM on CentOS/RHEL
^^^^^^^^^^^^^^^^^^
For KVM hosts, upgrade the ``cloudstack-agent`` package

#. Configure the :ref:`rpm-repo43` as detailed above.

   .. sourcecode:: bash

      $ sudo yum upgrade cloudstack-agent

#. Verify that the file ``/etc/cloudstack/agent/environment.properties`` has a 
   line that reads:

   .. sourcecode:: bash

      paths.script=/usr/share/cloudstack-common

   If not, add the line.

#. Restart the agent:

   .. sourcecode:: bash

      $ sudo service cloudstack-agent stop
      $ sudo killall jsvc
      $ sudo service cloudstack-agent start


.. _manual_hofix:

Manual hotfix for systemvm upgrade
----------------------------------

Some manual steps are required to upgrade of SystemVMs and Virtual Routers.

Following MySQL commands will update the template ID used by Console Proxy VMs (CPVM)
and Secondary Storage VMs (SSVM). It will also change the default template for
Virtual Router to *systemvm-<hypervisor>-4.4* templates.


XenServer SystemVMs
^^^^^^^^^^^^^^^^^^^

   Execute following MySQL queries in MySQL. 
   Please note ``<ID FROM COMMAND #1>`` from the first command

   #. Connect to the database:

      .. code-block:: bash

         mysql -h localhost -u root -p cloud

   #. get the id of the new template:

      .. code-block:: mysql

         select id,name from vm_template where name = 'systemvm-xenserver-4.4';

   #. Replace ``<ID FROM COMMAND #1>`` by the id from the previous command and execute following:

      .. code-block:: mysql
 
         update vm_template set type='SYSTEM' where id='<ID FROM COMMAND #1>';
         update vm_instance set vm_template_id = '<ID FROM COMMAND #1>' where type='ConsoleProxy' and hypervisor_type = 'xenserver';
         update vm_instance set vm_template_id = '<ID FROM COMMAND #1>' where type='SecondaryStorageVm' and hypervisor_type = 'xenserver';
         update configuration set value = 'systemvm-xenserver-4.4' where name = 'router.template.xen';


KVM SystemVMs
^^^^^^^^^^^^^

   Execute following MySQL queries in MySQL. 
   Please note ``<ID FROM COMMAND #1>`` from the first command

   #. Connect to the database:

      .. code-block:: bash

         mysql -h localhost -u root -p cloud

   #. get the id of the new template:

      .. code-block:: mysql   

         select id,name from vm_template where name = 'systemvm-kvm-4.4';

   #. Replace ``<ID FROM COMMAND #1>`` by the id from the previous command and execute following:

      .. code-block:: mysql

         update vm_template set type='SYSTEM' where id='<ID FROM COMMAND #1>';
         update vm_instance set vm_template_id = '<ID FROM COMMAND #1>' where type='ConsoleProxy' and hypervisor_type = 'KVM';
         update vm_instance set vm_template_id = '<ID FROM COMMAND #1>' where type='SecondaryStorageVm' and hypervisor_type = 'KVM';
         update configuration set value = 'systemvm-kvm-4.4' where name = 'router.template.kvm';


VMware SystemVMs
^^^^^^^^^^^^^^^^

   Execute following MySQL queries in MySQL. 
   Please note ``<ID FROM COMMAND #1>`` from the first command

   #. Connect to the database:

      .. code-block:: bash

         mysql -h localhost -u root -p cloud

   #. get the id of the new template:

      .. code-block:: mysql   

         select id,name from vm_template where name = 'systemvm-vmware-4.4';

   #. Replace ``<ID FROM COMMAND #1>`` by the id from the previous command and execute following:

      .. code-block:: mysql

         update vm_template set type='SYSTEM' where id='<ID FROM COMMAND #1>';
         update vm_instance set vm_template_id = '<ID FROM COMMAND #1>' where type='ConsoleProxy' and hypervisor_type = 'vmware';
         update vm_instance set vm_template_id = '<ID FROM COMMAND #1>' where type='SecondaryStorageVm' and hypervisor_type = 'vmware';
         update configuration set value = 'systemvm-vmware-4.4' where name = 'router.template.vmware';


Restart management services
---------------------------

#. Now it's time to start the management server

   .. sourcecode:: bash

      $ sudo service cloudstack-management start

#. If you use it, start the usage server

   .. sourcecode:: bash

      $ sudo service cloudstack-usage start


.. _upg-sysvm43:

System-VMs and Virtual-Routers
------------------------------

.. include:: _sysvm_restart.rst


.. include:: /global.rst
