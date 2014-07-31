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


.. |version_to_upgrade| replace:: 3.0.x

Upgrade Instruction from |version_to_upgrade|
=============================================

This section will guide you from Citrix CloudStack |version_to_upgrade| to 
Apache CloudStack |version|.

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

.. include:: _sysvm_templates_pre43.rst


Upgrade Steps
-------------

#. (KVM on RHEL 6.0/6.1 only) If your existing CloudStack deployment
   includes one or more clusters of KVM hosts running RHEL 6.0 or RHEL
   6.1, perform the following:

   #. Ensure that you upgrade the operating system version on those
      hosts before upgrading CloudStack

      To do that, change the yum repository for each system with
      CloudStack packages, that implies that all the Management Servers
      and any hosts that have the KVM agent.

   #. Open ``/etc/yum.repos.d/cloudstack.repo`` on any systems that have
      CloudStack packages installed.

   #. Edit as follows:

      .. sourcecode:: bash

         [upgrade]
         name=rhel63
         baseurl=url-of-your-rhel6.3-repo
         enabled=1
         gpgcheck=0
         [apache CloudStack]
         name= Apache CloudStack
         baseurl= http://cloudstack.apt-get.eu/rhel/4.4/
         enabled=1
         gpgcheck=0

      If you are using the community provided package repository, change
      the baseurl to ``http://cloudstack.apt-get.eu/rhel/4.4/``

      If you are using your own package repository, change this line to
      read as appropriate for your |version| repository.

   #. Now that you have the repository configured, upgrade the host
      operating system from RHEL 6.0 to 6.3:

      .. sourcecode:: bash

         # yum upgrade

#. Stop all Usage Servers if running. Run this on all Usage Server
   hosts.

   .. sourcecode:: bash

      # service cloud-usage stop

#. Stop the Management Servers. Run this on all Management Server hosts.

   .. sourcecode:: bash

      # service cloud-management stop

#. On the MySQL master, take a backup of the MySQL databases. We
   recommend performing this step even in test upgrades. If there is an
   issue, this will assist with debugging.

   In the following commands, it is assumed that you have set the root
   password on the database, which is a CloudStack recommended best
   practice. Substitute your own MySQL root password.

   .. sourcecode:: bash

      # mysqldump -u root -pmysql_password cloud > cloud-backup.dmp
      # mysqldump -u root -pmysql_password cloud_usage > cloud-usage-backup.dmp

#. Either build RPM/DEB packages as detailed in the Installation Guide,
   or use one of the community provided yum/apt repositories to gain
   access to the CloudStack binaries.

#. If you are using Ubuntu, follow this procedure to upgrade your packages. If 
   not, skip to step `8 <#upgrade-rpm-packages-302>`__.

   .. note:: 
      **Community Packages:** This section assumes you're using the community 
      supplied packages for CloudStack. If you've created your own packages 
      and APT repository, substitute your own URL for the ones used in these 
      examples.

   #. The first order of business will be to change the sources list for
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

   #. Verify that the file ``/etc/cloudstack/agent/environment.properties`` 
      has a line that reads:

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

#. If you are using CentOS or RHEL, follow this procedure to upgrade your 
   packages. If not, skip to step `9 <#correct-components-xml-302>`__.

   .. note:: 
      **Community Packages:** This section assumes you're using the community
      supplied packages for CloudStack. If you've created your own packages 
      and yum repository, substitute your own URL for the ones used in these 
      examples.

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

      If you are using the community provided package repository, change
      the baseurl to ``http://cloudstack.apt-get.eu/rhel/4.4/``

      If you're using your own package repository, change this line to
      read as appropriate for your |version| repository.

   #. Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package by upgrading the older
      ``cloud-client`` package.

      .. sourcecode:: bash

         $ sudo yum upgrade cloud-client

   #. For KVM hosts, you will need to upgrade the ``cloud-agent``
      package, similarly installing the new version as
      ``cloudstack-agent``.

      .. sourcecode:: bash

         $ sudo yum upgrade cloud-agent

      During the installation of ``cloudstack-agent``, the RPM will copy
      your ``agent.properties``, ``log4j-cloud.xml``, and
      ``environment.properties`` from ``/etc/cloud/agent`` to
      ``/etc/cloudstack/agent``.

   #. Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. sourcecode:: bash

         paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. Restart the agent:

      .. sourcecode:: bash

         service cloud-agent stop
         killall jsvc
         service cloudstack-agent start

#. If you have made changes to your copy of
   ``/etc/cloud/management/components.xml`` the changes will be
   preserved in the upgrade. However, you need to do the following steps
   to place these changes in a new version of the file which is
   compatible with version 4.x.x.

   #. Make a backup copy of ``/etc/cloud/management/components.xml``.
      For example:

      .. sourcecode:: bash

         # mv /etc/cloud/management/components.xml /etc/cloud/management/components.xml-backup

   #. Copy ``/etc/cloud/management/components.xml.rpmnew`` to create a
      new ``/etc/cloud/management/components.xml``:

      .. sourcecode:: bash

         # cp -ap /etc/cloud/management/components.xml.rpmnew /etc/cloud/management/components.xml

   #. Merge your changes from the backup file into the new
      ``components.xml``.

      .. sourcecode:: bash

         # vi /etc/cloudstack/management/components.xml

   .. note::  
      If you have more than one management server node, repeat the upgrade 
      steps on each node.

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

   PlainTextUserAuthenticator works the same way MD5UserAuthenticator
   worked prior to |version|

#. Start the first Management Server. Do not start any other Management
   Server nodes yet.

   .. sourcecode:: bash

      # service cloudstack-management start

   Wait until the databases are upgraded. Ensure that the database
   upgrade is complete. After confirmation, start the other Management
   Servers one at a time by running the same command on each node.

   .. note:: 
      Failing to restart the Management Server indicates a problem in the 
      upgrade. Having the Management Server restarted without any issues 
      indicates that the upgrade is successfully completed.

#. Start all Usage Servers (if they were running on your previous
   version). Perform this on each Usage Server host.

   ``# service cloudstack-usage start``

#. Additional steps are required for each KVM host. These steps will not
   affect running guests in the cloud. These steps are required only for
   clouds using KVM as hosts and only on the KVM hosts.

   #. Configure a yum or apt repository containing the CloudStack
      packages as outlined in the Installation Guide.

   #. Stop the running agent.

      ``# service cloud-agent stop``

   #. Update the agent software with one of the following command sets
      as appropriate for your environment.

      ``# yum update cloud-*``

      ``# apt-get update``

      ``# apt-get upgrade cloud-*``

   #. Edit ``/etc/cloudstack/agent/agent.properties`` to change the
      resource parameter from
      "com.cloud.agent.resource.computing.LibvirtComputingResource" to
      "com.cloud.hypervisor.kvm.resource.LibvirtComputingResource".

   #. Upgrade all the existing bridge names to new bridge names by
      running this script:

      .. sourcecode:: bash

         # cloudstack-agent-upgrade

   #. Install a libvirt hook with the following commands:

      .. sourcecode:: bash

         # mkdir /etc/libvirt/hooks
         # cp /usr/share/cloudstack-agent/lib/libvirtqemuhook /etc/libvirt/hooks/qemu
         # chmod +x /etc/libvirt/hooks/qemu

   #. Restart libvirtd.

      .. sourcecode:: bash

         # service libvirtd restart

   #. Start the agent.

      .. sourcecode:: bash

         # service cloudstack-agent start

   #. When the Management Server is up and running, log in to the
      CloudStack UI and restart the virtual router for proper
      functioning of all the features.

#. Log in to the CloudStack UI as administrator, and check the status of
   the hosts. All hosts should come to Up state (except those that you
   know to be offline). You may need to wait 20 or 30 minutes, depending
   on the number of hosts.

   .. note:: 
      Troubleshooting: If login fails, clear your browser cache and reload the 
      page.

   Do not proceed to the next step until the hosts show in Up state.

#. If you are upgrading from 3.0.x, perform the following:

   #. Ensure that the admin port is set to 8096 by using the "integration.api.port" global parameter.

      This port is used by the cloud-sysvmadm script at the end of the
      upgrade procedure. For information about how to set this
      parameter, see "Setting Global Configuration Parameters" in the
      Installation Guide.

   #. Restart the Management Server.

      .. note:: 
         If you don't want the admin port to remain open, you can set it to 
         null after the upgrade is done and restart the management server.

#. Run the ``cloudstack-sysvmadm`` script to stop, then start, all
   Secondary Storage VMs, Console Proxy VMs, and virtual routers. Run
   the script once on each management server. Substitute your own IP
   address of the MySQL instance, the MySQL user to connect as, and the
   password to use for that user. In addition to those parameters,
   provide the ``-c`` and ``-r`` arguments. For example:

   ``# nohup cloudstack-sysvmadm -d 192.168.1.5 -u cloud -p password -c -r > sysvm.log 2>&1 &``

   ``# tail -f sysvm.log``

   This might take up to an hour or more to run, depending on the number
   of accounts in the system.

#. If needed, upgrade all Citrix XenServer hypervisor hosts in your
   cloud to a version supported by CloudStack |version|. The supported
   versions are XenServer 5.6 SP2 and 6.0.2. Instructions for upgrade
   can be found in the CloudStack |version| Installation Guide under
   "Upgrading XenServer Versions."

#. Now apply the XenServer hotfix XS602E003 (and any other needed
   hotfixes) to XenServer v6.0.2 hypervisor hosts.

   #. Disconnect the XenServer cluster from CloudStack.

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

   #. To clean up the VLAN, log in to one XenServer host and run:

      ``/opt/xensource/bin/cloud-clean-vlan.sh``

   #. Now prepare the upgrade by running the following on one XenServer
      host:

      ``/opt/xensource/bin/cloud-prepare-upgrade.sh``

      If you see a message like "can't eject CD", log in to the VM and
      unmount the CD, then run this script again.

   #. Upload the hotfix to the XenServer hosts. Always start with the
      Xen pool master, then the slaves. Using your favorite file copy
      utility (e.g. WinSCP), copy the hotfixes to the host. Place them
      in a temporary folder such as /tmp.

      On the Xen pool master, upload the hotfix with this command:

      ``xe patch-upload file-name=XS602E003.xsupdate``

      Make a note of the output from this command, which is a UUID for
      the hotfix file. You'll need it in another step later.

      .. note:: 
         (Optional) If you are applying other hotfixes as well, you can repeat 
         the commands in this section with the appropriate hotfix number. For 
         example, XS602E004.xsupdate.

   #. Manually live migrate all VMs on this host to another host. First,
      get a list of the VMs on this host:

      ``# xe vm-list``

      Then use this command to migrate each VM. Replace the example host
      name and VM name with your own:

      ``# xe vm-migrate live=true host=host-name`` vm=\ *``VM-name``*

      .. note:: 
         **Troubleshooting:** If you see a message like "You attempted an 
         operation on a VM which requires PV drivers to be installed but the 
         drivers were not detected," run: 
         ``/opt/xensource/bin/make_migratable.sh b6cf79c8-02ee-050b-922f-49583d9f1a14``.

   #. Apply the hotfix. First, get the UUID of this host:

      .. sourcecode:: bash

         # xe host-list

      Then use the following command to apply the hotfix. Replace the
      example host UUID with the current host ID, and replace the hotfix
      UUID with the output from the patch-upload command you ran on this
      machine earlier. You can also get the hotfix UUID by running xe
      patch-list.

      .. sourcecode:: bash

         xe patch-apply host-uuid=host-uuid uuid=hotfix-uuid

   #. Copy the following files from the CloudStack Management Server to
      the host.


      +-------------------------+------------------------------------------+
      | Copy from here...       | ...to here                               |
      +=========================+==========================================+
      | /usr/lib64/cloud/common | /opt/xensource/sm/NFSSR.py               |
      | /scripts/vm/hypervisor/ |                                          |
      | xenserver/xenserver60/N |                                          |
      | FSSR.py                 |                                          |
      +-------------------------+------------------------------------------+
      | /usr/lib64/cloud/common | /opt/xensource/bin/setupxenserver.sh     |
      | /scripts/vm/hypervisor/ |                                          |
      | xenserver/setupxenserve |                                          |
      | r.sh                    |                                          |
      +-------------------------+------------------------------------------+
      | /usr/lib64/cloud/common | /opt/xensource/bin/make\_migratable.sh   |
      | /scripts/vm/hypervisor/ |                                          |
      | xenserver/make\_migrata |                                          |
      | ble.sh                  |                                          |
      +-------------------------+------------------------------------------+


   #. (Only for hotfixes XS602E005 and XS602E007) You need to apply a
      new Cloud Support Pack.

      -  Download the CSP software onto the XenServer host from one of
         the following links:

         For hotfix XS602E005:
         `http://coltrane.eng.hq.xensource.com/release/XenServer-6.x/XS-6.0.2/hotfixes/XS602E005/56710/xe-phase-2/xenserver-cloud-supp.tgz <http://coltrane.eng.hq.xensource.com/release/XenServer-6.x/XS-6.0.2/hotfixes/XS602E005/56710/xe-phase-2/xenserver-cloud-supp.tgz>`_

         For hotfix XS602E007:
         `http://coltrane.eng.hq.xensource.com/release/XenServer-6.x/XS-6.0.2/hotfixes/XS602E007/57824/xe-phase-2/xenserver-cloud-supp.tgz <http://coltrane.eng.hq.xensource.com/release/XenServer-6.x/XS-6.0.2/hotfixes/XS602E007/57824/xe-phase-2/xenserver-cloud-supp.tgz>`_

      -  Extract the file:

         .. sourcecode:: bash

            # tar xf xenserver-cloud-supp.tgz

      -  Run the following script:

         .. sourcecode:: bash

            # xe-install-supplemental-pack xenserver-cloud-supp.iso

      -  If the XenServer host is part of a zone that uses basic
         networking, disable Open vSwitch (OVS):

         .. sourcecode:: bash

            # xe-switch-network-backend  bridge

   #. Reboot this XenServer host.

   #. Run the following:

      .. sourcecode:: bash

         /opt/xensource/bin/setupxenserver.sh

      .. note:: 
         If the message "mv: cannot stat \`/etc/cron.daily/logrotate': No such 
         file or directory" appears, you can safely ignore it.

   #. Run the following:

      .. sourcecode:: bash

         for pbd in `xe pbd-list currently-attached=false| grep ^uuid | awk '{print $NF}'`; do xe pbd-plug uuid=$pbd ;

   #. On each slave host in the Xen pool, repeat these steps, starting
      from "manually live migrate VMs."

.. note:: 
   **Troubleshooting Tip:** If passwords which you know to be valid appear not 
   to work after upgrade, or other UI issues are seen, try clearing your 
   browser cache and reloading the UI page.

.. include:: /global.rst
