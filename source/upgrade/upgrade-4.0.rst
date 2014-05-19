Upgrade Instruction from 4.0.x
------------------------------

.. warning::
   :name: Depreciation of realhostip.com DNS and SSL certificate
   
   The realhostip.com dynamic DNS resolution service is being retired this
   summer. In advance of that, CloudStack 4.3 and later no longer uses realhostip.com
   DNS domains or SSL certificates to encrypt Console Proxy or file copy
   communications.

This section will guide you from CloudStack 4.0.x versions to CloudStack |version|.

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
   the 4.3.0 source, or check the Apache CloudStack downloads page at
   `http://cloudstack.apache.org/downloads.html <http://cloudstack.apache.org/downloads.html>`__
   for package repositories supplied by community members. You will need
   them for step `9 <#upgrade-deb-packages-40to43>`__ or step
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

      .. include:: /systemvm_templates.rst


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

   After upgrading to |version|, API clients are expected to send plain text
   passwords for login and user creation, instead of MD5 hash. Incase,
   api client changes are not acceptable, following changes are to be
   made for backward compatibility:

   Modify componentsContext.xml, and make PlainTextUserAuthenticator as
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
   worked prior to |version|.

#. 

   If you are using Ubuntu, follow this procedure to upgrade your
   packages. If not, skip to step `10 <#upgrade-rpm-packages-40to43>`__.

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
      read as appropriate for your 4.3.0 repository.

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
      read as appropriate for your |version| repository.

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

.. include:: /global.rst