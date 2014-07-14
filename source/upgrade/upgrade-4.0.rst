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


.. |version_to_upgrade| replace:: 4.0.x

Upgrade Instruction from |version_to_upgrade|
=============================================

This section will guide you from CloudStack |version_to_upgrade| versions to 
CloudStack |version|.

.. include:: _upgrade_header.rst

.. important:: 
   **Package Structure Changes:** The package structure for CloudStack has 
   changed significantly since the |version_to_upgrade| releases. If you've 
   compiled your own packages, you'll notice that the package names and the 
   number of packages has changed. This is *not* a bug. However, this *does* 
   mean that the procedure is not as simple as an ``apt-get upgrade`` or 
   ``yum update``, so please follow this section carefully.


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
them for :ref:`ubuntu40` or :ref:`rhel40` hosts upgrade. 

Instructions for creating packages from the CloudStack source are in the 
`CloudStack Installation Guide`_.

.. include:: _sysvm_templates.rst


Database Preparation
--------------------

#. Stop your management server or servers. Run this on all management
   server hosts:

   .. sourcecode:: bash

      # service cloud-management stop

#. If you are running a usage server or usage servers, stop those as well:

   .. sourcecode:: bash

      # service cloud-usage stop

#. Make a backup of your MySQL database. If you run into any issues or
   need to roll back the upgrade, this will assist in debugging or
   restoring your existing environment. You'll be prompted for your
   password.

   .. sourcecode:: bash

      # mysqldump -u root -p cloud > cloudstack-backup.sql

#. Whether you're upgrading a Red Hat/CentOS based system or Ubuntu
   based system, you're going to need to stop the CloudStack management
   server before proceeding.

   .. sourcecode:: bash

      # service cloud-management stop

#. If you have made changes to ``/etc/cloud/management/components.xml``,
   you'll need to carry these over manually to the new file,
   ``/etc/cloudstack/management/componentContext.xml``. This is not done
   automatically. (If you're unsure, we recommend making a backup of the
   original ``components.xml`` to be on the safe side.

#. After upgrading to |version|, API clients are expected to send plain text
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

   PlainTextUserAuthenticator works the same way MD5UserAuthenticator worked 
   prior to 4.1.


.. _ubuntu40:

Ubuntu
------

If you are using Ubuntu, follow this procedure to upgrade your packages. If 
not, skip to :ref:`rhel40`.

.. note:: 
   **Community Packages:** This section assumes you're using the community 
   supplied packages for CloudStack. If you've created your own packages and 
   APT repository, substitute your own URL for the ones used in these examples.

#. The first order of business will be to change the sources list for
   each system with CloudStack packages. This means all management
   servers, and any hosts that have the KVM agent. (No changes should
   be necessary for hosts that are running VMware or Xen.)

   Start by opening ``/etc/apt/sources.list.d/cloudstack.list`` on any systems 
   that have CloudStack packages installed.

   This file should have one line, which contains:

   .. sourcecode:: bash

      deb http://cloudstack.apt-get.eu/ubuntu precise 4.0

   We'll change it to point to the new package repository:

   .. sourcecode:: bash

      deb http://cloudstack.apt-get.eu/ubuntu precise 4.4

   If you're using your own package repository, change this line to
   read as appropriate for your |version| repository.

#. Now update your apt package list:

   .. sourcecode:: bash

      $ sudo apt-get update

#. Now that you have the repository configured, it's time to install
   the ``cloudstack-management`` package. This will pull in any other
   dependencies you need.

   .. sourcecode:: bash

      $ sudo apt-get install cloudstack-management

#. You will need to manually install the ``cloudstack-agent`` package:

   .. sourcecode:: bash

      $ sudo apt-get install cloudstack-agent

   During the installation of ``cloudstack-agent``, APT will copy
   your ``agent.properties``, ``log4j-cloud.xml``, and
   ``environment.properties`` from ``/etc/cloud/agent`` to
   ``/etc/cloudstack/agent``.

   When prompted whether you wish to keep your configuration, say
   Yes.

#. Verify that the file ``/etc/cloudstack/agent/environment.properties`` has a 
   line that reads:

   .. sourcecode:: bash

      paths.script=/usr/share/cloudstack-common

   If not, add the line.

#. Restart the agent:

   .. sourcecode:: bash

      service cloud-agent stop
      killall jsvc
      service cloudstack-agent start

#. During the upgrade, ``log4j-cloud.xml`` was simply copied over, so
   the logs will continue to be added to
   ``/var/log/cloud/agent/agent.log``. There's nothing *wrong* with
   this, but if you prefer to be consistent, you can change this by
   copying over the sample configuration file:

   .. sourcecode:: bash

      cd /etc/cloudstack/agent
      mv log4j-cloud.xml.dpkg-dist log4j-cloud.xml
      service cloudstack-agent restart

#. Once the agent is running, you can uninstall the old cloud-\*
   packages from your system:

   .. sourcecode:: bash

      sudo dpkg --purge cloud-agent


.. _rhel40:

CentOS/RHEL
-----------

If you are using CentOS or RHEL, follow this procedure to upgrade your 
packages. If not, skip to step :ref:`upg-sysvm40`.

.. note:: 
   **Community Packages:** This section assumes you're using the community 
   supplied packages for CloudStack. If you've created your own packages and 
   yum repository, substitute your own URL for the ones used in these examples.

#. The first order of business will be to change the yum repository
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

   If you are using the community provided package repository, change the 
   baseurl to ``http://cloudstack.apt-get.eu/rhel/4.4/``

   If you're using your own package repository, change this line to read as 
   appropriate for your |version| repository.

#. Now that you have the repository configured, it's time to install
   the ``cloudstack-management`` package by upgrading the older
   ``cloud-client`` package.

   .. sourcecode:: bash

      $ sudo yum upgrade cloud-client

#. **For KVM hosts**, you will need to upgrade the ``cloud-agent``
   package, similarly installing the new version as
   ``cloudstack-agent``.

   .. sourcecode:: bash

      $ sudo yum upgrade cloud-agent

   During the installation of ``cloudstack-agent``, the RPM will copy
   your ``agent.properties``, ``log4j-cloud.xml``, and
   ``environment.properties`` from ``/etc/cloud/agent`` to
   ``/etc/cloudstack/agent``.

#. Verify that the file ``/etc/cloudstack/agent/environment.properties`` has a 
   line that reads:

   .. sourcecode:: bash

      paths.script=/usr/share/cloudstack-common

   If not, add the line.

#. Restart the agent:

   .. sourcecode:: bash

      service cloud-agent stop
      killall jsvc
      service cloudstack-agent start


Hypervisor: XenServer
---------------------

   **(XenServer only)** Copy vhd-utils file on CloudStack management servers.
   
   Copy the file `vhd-utils <http://download.cloud.com.s3.amazonaws.com/tools/vhd-util>`_ 
   to ``/usr/share/cloudstack-common/scripts/vm/hypervisor/xenserver``.


.. _upg-sysvm40:

.. include:: _sysvm_restart.rst

.. include:: /global.rst
