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

Welcome to the 4.3 release of CloudStack. This version is the first
feature release of CloudStack in the 4.3.x line.

This document contains information specific to this release of
CloudStack, including upgrade instructions from prior releases, new
features added to CloudStack, API changes, and issues fixed in the
release. For installation instructions, please see the `Installation
Guide <http://cloudstack.apache.org/docs/en-US/Apache_CloudStack/4.3.0/html/Installation_Guide/index.html>`__.
For usage and administration instructions, please see the `CloudStack
Administrator's
Guide <http://cloudstack.apache.org/docs/en-US/Apache_CloudStack/4.3.0/html/Admin_Guide/index.html>`__.
Developers and users who wish to work with the API will find instruction
in the `CloudStack API Developer's
Guide <http://cloudstack.apache.org/docs/en-US/Apache_CloudStack/4.0.1-incubating/html/API_Developers_Guide/index.html>`__.

Welcome to Apache CloudStack 4.3
================================

This section describes the operating systems, browsers, and hypervisors
that have been newly tested and certified compatible with CloudStack
4.3. Most earlier OS and hypervisor versions are also still supported
for use with 4.3 It might work well on other platforms, but the
platforms listed below are the ones that are specifically tested against
and are more likely to be able to help troubleshoot if you run into any
issues.

Compatibility Matrix
====================

Supported OS Versions for Management Server
-------------------------------------------

This section lists the operating systems that are supported for running
CloudStack Management Server. Note that specific versions of the
operating systems are tested, so compatibility with CentOS 6.3 may not
indicate compatibility with CentOS 6.2, 6.1 and so on.

-  

   RHEL versions 5.5, 6.2, 6.3, and 6.4

-  

   CentOS versions 6.3, and 6.4

-  

   Ubuntu 12.04 LTS

Supported Hypervisor Versions
-----------------------------

CloudStack supports three hypervisor families, XenServer with XAPI, KVM,
and VMware with vSphere.

-  

   Windows Server 2012 R2 (with Hyper-V Role enabled)

-  

   Hyper-V 2012 R2

-  

   CentOS 6.2 with KVM

-  

   Red Hat Enterprise Linux 6.2 with KVM

-  

   XenServer 6.0.2 (with Hotfix)

-  

   XenServer versions 6.1 and 6.2 SPI with latest hotfixes

-  

   VMware versions 5.0, 5.1, and 5.5

-  

   Bare metal hosts are supported, which have no hypervisor. These hosts
   can run the following operating systems:

   -  

      RHEL or CentOS, v6.2 or 6.3

      .. note:: Use libvirt version 0.9.10 for CentOS 6.3

   -  

      Fedora 17

   -  

      Ubuntu 12.04

For more information, see the Hypervisor Compatibility Matrix in the
CloudStack Installation Guide.

Supported External Devices
--------------------------

-  

   Netscaler VPX and MPX versions 9.3 and 10.e

-  

   Netscaler SDX version 9.3

-  

   SRX (Model srx100b) versions 10.3 or higher

-  

   F5 10.1.0 (Build 3341.1084)

Supported Browsers
------------------

The CloudStack Web-based UI should be compatible with any modern
browser, but it's possible that some browsers will not render portions
of the UI reliably, depending on their support of Web standards. For
best results, one of the following browsers recommended:

-  

   Internet Explorer versions 10 and 11

-  

   Firefox version 26 or lower

-  

   Google Chrome version 31

-  

   Safari 5


About this new Release
======================

What's New in 4.3
-----------------

CloudStack 4.3 includes the following new features.

Optional 64-Bit System VM Template Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CloudStack now provides 64-bit templates for System VMs. With this
support, you will be able to upgrade virtual routers in a zone. The
following parameters have been introduced for the same purpose:

-  

   XenServer: *``router.template.xen``*

-  

   KVM: *``router.template.kvm``*

-  

   VMware:

-  

   Hyper-V:

Hyper-V Support
~~~~~~~~~~~~~~~

CloudStack 4.3 Beta rolls out support for Hyper-V hosts. For Hyper-V,
CloudStack supports SMB-based storage. If you want to run guest VMs on
Hyper-V hosts, install CloudStack Agents on each Hyper-V hosts. Before
you use Hyper-V, review the following list of supported and
non-supported features. For detailed instruction, see Hyper-V Quick
Start Guide. You can also see the chapter Installing Hyper-V for
CloudStack in the CloudStack 4.3 Beta Installation Guide.

Supported Functionalities
^^^^^^^^^^^^^^^^^^^^^^^^^

-  

   VM Compute

   -  

      All the VM operations, except VM Snapshots

   -  

      Live Migration

   -  

      Service Offerings (Scale up on stopped VMs)

   -  

      Console access

   -  

      SSH key and reseting SSH key

   -  

      Upload and download templates, volumes, and ISO

   -  

      Create VMs from template and ISO

   -  

      Create template from volume

   -  

      Attach and detach VMs from ISO and password-enabled template

   -  

      Copy template across zone

-  

   Storage

   -  

      Primary Storage (SMB and Local)

   -  

      Root and data volumes on Local and SMB

   -  

      Add, delete, attach, detach volumes (one or more volumes per VM)

   -  

      Single and multiple secondary storage (SMB)

-  

   Network

   -  

      VLANs (Isolated and Shared)

   -  

      All VR services: DNS, DHCP, SourceNAT, LB, PF, Firewall,
      StaticNAT, Userdata, and VPN

   -  

      External device support for both Isolated and Shared networks:
      Netscaler, SRX, F5

   -  

      Multiple physical networks

   -  

      Dedicated IP range, Public VLANs (to account)

   -  

      Network Offering upgrades and updates

   -  

      L4-L7 services in Shared network

   -  

      Multiple IP ranges and portable IPs

-  

   Host and Storage in maintenance mode

Unsupported Functionalities
^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  

   Affinity an Anti-Affinity Groups

-  

   Network throttling

-  

   Security groups (Advanced Zone)

-  

   IPv6

-  

   Snapshot: VM and disk

-  

   PVLAN

-  

   VPC

-  

   HA of guest VMs

-  

   Redundant VR

-  

   Object Store

-  

   Mixed hypervisor zone

-  

   Zone-wide Primary storage

-  

   NIC bonding

Enhanced Upgrade for Virtual Routers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upgrading VRs is made flexible. The CloudStack administrators will be
able to control the sequence of the VR upgrades. The sequencing is based
on Infrastructure hierarchy, such as by Cluster, Pod, or Zone, and
Administrative hierarchy, such as by Tenant or Domain. This implies, for
example, that you will have the flexibility to upgrade a VR in a
specified zone. As an administrator, you can also determine when a
particular VR can be upgraded within a specified upgrade interval.
Additionally, upgrade operation is enhanced to increase the upgrade
speed by allowing as many upgrade operations in parallel as possible.
During the entire duration of the upgrade, users cannot launch new
services or make changes to an existing service.

To support this feature, a new API, upgradeRouterTemplate, has been
introduced.

The detailed instruction is provided in the CloudStack 4.3 Beta
Administration Guide. See section 17.5.5. Enhanced Upgrade for Virtual
Routers.

Service Monitoring Tool for Virtual Router
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Various services running on the CloudStack virtual routers can be
monitored by using a Service Monitoring tool. The tool ensures that
services are successfully running until CloudStack deliberately disables
them. If a service goes down, the tool automatically performs a restart,
and if that does not help bringing up the service, an alert as well as
an event is generated indicating the failure.

The following services are monitored in a VR:

-  

   DNS

-  

   HA Proxy

-  

   SSH

-  

   Apache Web Server

Only the services with daemons are monitored.

The following networks are supported:

-  

   Isolated Networks

-  

   Shared Networks in both Advanced and Basic zone

This feature is supported on the following hypervisors: XenServer,
VMware, and KVM.

The detailed instruction is provided in the CloudStack 4.3 Beta
Administration Guide. See section 17.5.4. Service Monitoring Tool for
Virtual Router.

Custom Compute Offering
~~~~~~~~~~~~~~~~~~~~~~~

CloudStack provides you the flexibility to specify the desired values
for the number of CPU, CPU speed, and memory while deploying a VM. The
admin creates a Compute Offering by marking it as custom, and as an
user, you will be able to customize this dynamic Compute Offering by
specifying the memory, CPU and root disk at the time of VM creation or
upgrade.

Custom Compute Offering is same as the normal Compute Offering except
that the values of the dynamic parameters will be set to zeros in the
given set of templates. Use this offering to deploy VM by specifying
custom values for the dynamic parameters. Memory, CPU and number of CPUs
are considered as dynamic parameters. Dynamic Compute Offerings can be
used in following cases: deploying a VM, changing the compute offering
of a stopped VM and running VMs, which is nothing but scaling up. To
support this feature a new field, Custom, has been added to the Create
Compute Offering page. If the Custom field is checked, the end-user will
be able to create a custom Compute Offering by filling in the desired
values for number of CPU, CPU speed, and memory.

Remote Access VPN for VPC
~~~~~~~~~~~~~~~~~~~~~~~~~

Support for Remote access VPN in Isolated networks is now extended to
VPC networks. Remote users will now be able to initiate a VPN connection
to a VPC network. To enable this feature, enable VPN in the Source NAT
IP of the VPC.

Site to Site VPN Connection Between VPC Networks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CloudStack provides you with the ability to establish a site-to-site VPN
connection between CloudStack virtual routers. With this functionality,
users can deploy applications in multiple Availability Zones or VPCs,
which can communicate with each other by using a secure Site-to-Site VPN
Tunnel. Creating a typical Site to Site VPN connection between VPC
networks involves the following:

#. 

   Create two VPCs. For example, VPC A and VPC B.

#. 

   Create VPN gateways on both the VPCs you created.

#. 

   Create VPN customer gateway for both the VPCs.

#. 

   Enable a VPN connection on VPC A in passive mode.

   Ensure that the customer gateway is pointed to VPC B. The VPN
   connection is shown in the Disconnected state.

#. 

   Enable a VPN connection on VPC B.

   Ensure that the customer gateway is pointed to VPC A. Because virtual
   router of VPC A, in this case, is in passive mode and is waiting for
   the virtual router of VPC B to initiate the connection. The virtual
   router of VPC B should not be in passive mode.

   The VPN connection is shown in the Disconnected state.

   Creating VPN connection on both the VPCs initiates a VPN connection.
   Wait for few seconds. The default is 30 seconds for both the VPN
   connections to show the Connected state.

Reporting CPU Sockets
~~~~~~~~~~~~~~~~~~~~~

CloudStack now provides an additional infrastructure statistics for CPU
sockets managed by CloudStack, which in turn reflects the size of the
cloud. The Infrastructure tab has a new tab for sockets. The Socket page
will give you the number of hosts an sockets used for each hypervisor
type. This feature is not supported in versions prior to XenServer 6.2.

Database High Availability
~~~~~~~~~~~~~~~~~~~~~~~~~~

To help ensure high availability of the databases that store the
internal data for CloudStack, you can set up database replication. This
covers both the main CloudStack database and the Usage database.
Replication is achieved using the MySQL connector parameters and two-way
replication. Tested with MySQL 5.1 and 5.5. Database replication in
CloudStack is provided using the MySQL replication capabilities. The
steps to set up replication can be found in the MySQL documentation.

LDAP User Provisioning
~~~~~~~~~~~~~~~~~~~~~~

LDAP user provisioning has been enhanced by allowing user import from
the configured LDAP servers. You will be able to add multiple LDAP
servers and selectively import LDAP users. You can o filter by group
name and import all the users within a group. After they have been
imported to CloudStack, in contrast to manually adding them in previous
releases, users are allowed to directly log in to CloudStack by using
the LDAP credentials.

Migrating NFS Secondary Storage to Object Store
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In an existing zone that is using NFS for secondary storage, you can
upgrade the zone to use a region-wide object storage without causing
downtime. The existing NFS storage in the zone will be converted to an
NFS Staging Store. After migration, the data that was on the NFS storage
remains there. CloudStack does not provide a way to automatically
migrate all data to the new object storage. The data remaining on the
old NFS storage will remain accessible for read and delete operations
only. Newly created snapshots and templates will be placed in the newly
configured object storage.

VXLAN Plugin Support
~~~~~~~~~~~~~~~~~~~~

The VXLAN plugin adds VXLAN as one of the guest network isolation
methods in CloudStack. This plugin enables more than 4096 isolated guest
networks in a Zone, with almost the same usability as VLAN isolation.
This plugin provides no network services. Use virtual router for network
services. This plugin is supported on KVM hypervisors.

Contrail Network Plugin Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Contrail virtual network controller is an open source project that
provides an overlay implementation of network virtualization that is
interoperable with network devices that support existing network
virtualization standards. Support for the Contrail plugin has been added
to CloudStack to provide NAT services to the XenServer hosts. The plugin
supports isolated networks, Static NAT implemented by the VRouter
dataplane, and Source NAT implemented by using a virtual appliance with
full NAT functionality.

Publishing Alert Using the Web ROOT Admin API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In previous releases of CloudStack code alerts are generated for
CloudStack services (Usage service) only if they run on the same host as
the Management Server. A new API has been introduced in 4.3, which can
be used by the following services to generate and publish. The services
need not be running on the same host where the Management Server is
running.

-  

   Any new services added to CloudStack.

-  

   Usage service when run on a separate storage host.

-  

   Console Proxy and Secondary Storage VM services.

The main advantage of this feature is that the third party systems
integrating with CloudStack will be able to utilize the Alert
notification system publish alerts.

Support for Palo Alto Firewall Service
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CloudStack supports Palo Alto firewall services. Use the Create Network
Offering dialog to create an offering which has the Palo Alto firewall
services. What is not supported and not supported are given below:

Supported Functionalities
^^^^^^^^^^^^^^^^^^^^^^^^^

-  

   Advanced Network

-  

   Parallel deployment with hardware Load balancer

-  

   Virtual Palo Alto firewall.

-  

   Communication layer with Palo Alto APIs.

-  

   Mapping of CloudStack APIs to corresponding Palo Alto APIs.

-  

   Connectivity status of the firewall service on the CloudStack UI.

Unsupported Functionalities
^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  

   Inline deployment with hardware Load balancer

-  

   Firewall between VLANs within an advanced network

-  

   Firewall between VM instances

For more information, see `Palo Alto Firewall
Integration <https://cwiki.apache.org/confluence/display/CLOUDSTACK/Palo+Alto+Firewall+Integration>`__.

Root Volume Metering
~~~~~~~~~~~~~~~~~~~~

CloudStack supports recording usage events as per the dynamically
assigned resources. Usage events are registered when a VM is created
from dynamic service offering, and the values of parameters, such as
CPU, speed, RAM are recorded. If VM is deployed by using template and
dynamic root disk size is mentioned, the same value is recorded in the
usage event.

Support for SSL Termination
~~~~~~~~~~~~~~~~~~~~~~~~~~~

SSL Offloading allows load balancers to handle encryption and decryption
of HTTP(s) traffic giving plain text HTTP to the back end servers
freeing them from the resource intensive task of handling encryption and
decryption. Supported for Citrix NetScaler.

Support for Pluggable VM Snapshots
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CloudStack implements a plugin to integrate a third-party storage
provider. Third party storage providers can integrate with CloudStack to
provide either primary storage or secondary storage. The user enables a
storage plugin through the UI. A new dialog box choice is offered to
select the storage provider. Depending on which provider is selected,
additional input fields may appear so that the user can provide the
additional details required by that provider, such as a user name and
password for a third-party storage account.

Enhanced CloudStack UI
~~~~~~~~~~~~~~~~~~~~~~

A complete UI makeover is implemented to enhance the usability and user
experience in modern browsers. The visual look-and-feel has been changed
for the Header, Navigation, Buttons, text fields, drop-downs, tables and
so on. Consistent color themes has been introduced to match with the
Apache branding.

The current UI flow remains the same.

Issues Fixed in 4.3.0
---------------------

Apache CloudStack uses
`Jira <https://issues.apache.org/jira/browse/CLOUDSTACK>`__ to track its
issues. All new features and bugs for 4.3 have been tracked in Jira, and
have a standard naming convention of "CLOUDSTACK-NNNN" where "NNNN" is
the issue number.

For the list of issues fixed, see `Issues Fixed in
4.3 <https://issues.apache.org/jira/issues/?filter=12326161>`__.

Known Issues in 4.3.0
---------------------

Apache CloudStack uses
`Jira <https://issues.apache.org/jira/browse/CLOUDSTACK>`__ to track its
issues. All new features and bugs for 4.3 have been tracked in Jira, and
have a standard naming convention of "CLOUDSTACK-NNNN" where "NNNN" is
the issue number.

For the list of known issues, see `Known Issues in
4.3 <https://issues.apache.org/jira/issues/?filter=12326162>`__.


Upgrade Instructions for 4.3
============================

This section contains upgrade instructions from prior versions of
CloudStack to Apache CloudStack 4.3. We include instructions on
upgrading to Apache CloudStack from pre-Apache versions of Citrix
CloudStack (last version prior to Apache is 3.0.2) and from the releases
made while CloudStack was in the Apache Incubator.

If you run into any issues during upgrades, please feel free to ask
questions on users@cloudstack.apache.org or dev@cloudstack.apache.org.

Upgrade from 4.2.0 to 4.3
-------------------------

This section will guide you from CloudStack 4.2 to CloudStack 4.3.

Any steps that are hypervisor-specific will be called out with a note.

We recommend reading through this section once or twice before beginning
your upgrade procedure, and working through it on a test system before
working on a production system.

.. note:: The following upgrade instructions should be performed regardless of hypervisor type.

#. 

   #. 

      While running the existing 4.2.0 system, log in to the UI as root
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

      Hypervisor

      Description

      XenServer

      Name: systemvm-xenserver-4.2

      Description: systemvm-xenserver-4.2

      URL:http://download.cloud.com/templates/4.2/systemvmtemplate-2013-07-12-master-xen.vhd.bz2

      Zone: Choose the zone where this hypervisor is used

      Hypervisor: XenServer

      Format: VHD

      OS Type: Debian GNU/Linux 7.0 (32-bit) (or the highest Debian
      release number available in the dropdown)

      Extractable: no

      Password Enabled: no

      Public: no

      Featured: no

      KVM

      Name: systemvm-kvm-4.2

      Description: systemvm-kvm-4.2

      URL:
      http://download.cloud.com/templates/4.2/systemvmtemplate-2013-06-12-master-kvm.qcow2.bz2

      Zone: Choose the zone where this hypervisor is used

      Hypervisor: KVM

      Format: QCOW2

      OS Type: Debian GNU/Linux 7.0 (32-bit) (or the highest Debian
      release number available in the dropdown)

      Extractable: no

      Password Enabled: no

      Public: no

      Featured: no

      VMware

      Name: systemvm-vmware-4.2

      Description: systemvm-vmware-4.2

      URL:
      http://download.cloud.com/templates/4.2/systemvmtemplate-4.2-vh7.ova

      Zone: Choose the zone where this hypervisor is used

      Hypervisor: VMware

      Format: OVA

      OS Type: Debian GNU/Linux 7.0 (32-bit) (or the highest Debian
      release number available in the dropdown)

      Extractable: no

      Password Enabled: no

      Public: no

      Featured: no

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
   them for step `9 <#upgrade-deb-packages-4.3>`__ or step
   `12 <#upgrade-rpm-packages-4.3>`__.

   Instructions for creating packages from the CloudStack source are in
   the `Installation
   Guide <http://cloudstack.apache.org/docs/en-US/index.html>`__.

#. 

   Stop your management server or servers. Run this on all management
   server hosts:

   .. code:: bash

       # service cloudstack-management stop

#. 

   If you are running a usage server or usage servers, stop those as
   well:

   .. code:: bash

       # service cloudstack-usage stop

#. 

   Make a backup of your MySQL database. If you run into any issues or
   need to roll back the upgrade, this will assist in debugging or
   restoring your existing environment. You'll be prompted for your
   password.

   .. code:: bash

       # mysqldump -u root -p cloud > cloudstack-backup.sql

#. 

   Perform the following to verify the artifacts:

   #. 

      (optional) Install GPG keys if needed:

      .. code::
	  
          $sudo apt-get install gpg

   #. 

      Import the GPG keys stored in the source distribution's KEYS file

      .. code:: bash

          $gpg --import KEYS

      Alternatively, download the signing keys, the IDs found in the
      KEYS file, individually by using a keyserver.

      For example:

      .. code::

          $ gpg --recv-keys CC56CEA8

   #. 

      Verify signatures and hash files:

      .. code::

          #gpg --verify apache-cloudstack-4.3-src.tar.bz2.asc
          #gpg --print-md MD5 apache-cloudstack-4.3-src.tar.bz2 | diff - apache-cloudstack-4.3-src.tar.bz2.md5
          #gpg --print-md SHA512 apache-cloudstack-4.3-src.tar.bz2 | diff - apache-cloudstack-4.3-src.tar.bz2.sha

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

      .. code::

          #mkdir /tmp/cloudstack/git
          #mkdir /tmp/cloudstack/tree

   #. 

      Check out the 4.3 branch:

      .. code::

          #git clone https://git-wip-us.apache.org/repos/asf/cloudstack.git /tmp/cloudstack/git
          #cd /tmp/cloudstack/git
          #git archive --format=tar --prefix=/tmp/cloudstack/tree/ <commit-hash> | tar Pxf -

   #. 

      Unpack the release artifact:

      .. code::

          #cd /tmp/cloudstack
          #tar xvfj apache-cloudstack-4.3-src.tar.bz2

   #. 

      Compare the contents of the release artifact with the contents
      pulled from the repo:

      .. code::

          #diff -r /tmp/cloudstack/apache-cloudstack-4.3-src /tmp/cloudstack/tree

      Ensure that content is the same.

   #. 

      Verify the Code License Headers:

      .. code::

          #cd /tmp/cloudstack/apache-cloudstack-4.3-src
          #mvn --projects='org.apache.cloudstack:cloudstack' org.apache.rat:apache-rat-plugin:0.8:check

      The build fails if any non-compliant files are present that are
      not specifically excluded from the ASF license header requirement.
      You can optionally review the target/rat.txt file after the run
      completes. Passing the build implies that RAT certifies that the
      files are compliant and this test is passed.

#. 

   (KVM Only) If primary storage of type local storage is in use, the
   path for this storage needs to be verified to ensure it passes new
   validation. Check local storage by querying the cloud.storage\_pool
   table:

   .. code:: bash

       #mysql -u cloud -p -e "select id,name,path from cloud.storage_pool where pool_type='Filesystem'"

   If local storage paths are found to have a trailing forward slash,
   remove it:

   .. code:: bash

       #mysql -u cloud -p -e 'update cloud.storage_pool set path="/var/lib/libvirt/images" where path="/var/lib/libvirt/images/"';

#. 

   If you are using Ubuntu, follow this procedure to upgrade your
   packages. If not, skip to step `12 <#upgrade-rpm-packages-4.3>`__.

   .. note:: **Community Packages:** This section assumes you're using the community supplied packages for CloudStack. If you've created your own packages and APT repository, substitute your own URL for the ones used in these examples.

   #. 

      The first order of business will be to change the sources list for
      each system with CloudStack packages. This means all management
      servers, and any hosts that have the KVM agent. (No changes should
      be necessary for hosts that are running VMware or Xen.)

      Start by opening ``/etc/apt/sources.list.d/cloudstack.list`` on
      any systems that have CloudStack packages installed.

      This file should have one line, which contains:

      .. code::

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.0

      We'll change it to point to the new package repository:

      .. code::

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.2

      If you're using your own package repository, change this line to
      read as appropriate for your 4.3 repository.

   #. 

      Now update your apt package list:

      .. code::

          $ sudo apt-get update

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package. This will pull in any other
      dependencies you need.

      .. code::

          $ sudo apt-get install cloudstack-management

   #. 

      You will need to manually install the ``cloudstack-agent``
      package:

      .. code::

          $ sudo apt-get install cloudstack-agent

      During the installation of ``cloudstack-agent``, APT will copy your ``agent.properties``, ``log4j-cloud.xml``, and
      ``environment.properties`` from ``/etc/cloud/agent`` to ``/etc/cloudstack/agent``.

      When prompted whether you wish to keep your configuration, say
      Yes.

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. code:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. code:: bash

          #service cloudstack-agent stop
          #killall jsvc
          #service cloudstack-agent start

#. 

   (VMware only) Additional steps are required for each VMware cluster.
   These steps will not affect running guests in the cloud. These steps
   are required only for clouds using VMware clusters:

   #. 

      Stop the Management Server:

      .. code:: bash

          service cloudstack-management stop

   #. 

      Generate the encrypted equivalent of your vCenter password:

      .. code:: bash

          java -classpath /usr/share/cloudstack-common/lib/jasypt-1.9.0.jar org.jasypt.intf.cli.JasyptPBEStringEncryptionCLI encrypt.sh input="_your_vCenter_password_" password="`cat /etc/cloudstack/management/key`" verbose=false

      Store the output from this step, we need to add this in
      cluster\_details table and vmware\_data\_center tables in place of
      the plain text password

   #. 

      Find the ID of the row of cluster\_details table that you have to
      update:

      .. code:: bash

          mysql -u <username> -p<password>

      .. code:: bash

          select * from cloud.cluster_details;

   #. 

      Update the plain text password with the encrypted one

      .. code:: bash

          update cloud.cluster_details set value = '_ciphertext_from_step_1_' where id = _id_from_step_2_;

   #. 

      Confirm that the table is updated:

      .. code:: bash

          select * from cloud.cluster_details;

   #. 

      Find the ID of the correct row of vmware\_data\_center that you
      want to update

      .. code:: bash

          select * from cloud.vmware_data_center;

   #. 

      update the plain text password with the encrypted one:

      .. code:: bash

          update cloud.vmware_data_center set password = '_ciphertext_from_step_1_' where id = _id_from_step_5_;

   #. 

      Confirm that the table is updated:

      .. code:: bash

          select * from cloud.vmware_data_center;

   #. 

      Start the CloudStack Management server

      .. code:: bash

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

      .. code:: bash

          # service cloud-agent stop

   #. 

      Update the agent software.

      .. code:: bash

          # yum update cloudstack-agent

   #. 

      Start the agent.

      .. code:: bash

          # service cloudstack-agent start

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

      .. code:: bash

          [apache-cloudstack]
          name=Apache CloudStack
          baseurl=http://cloudstack.apt-get.eu/rhel/4.0/
          enabled=1
          gpgcheck=0

      If you are using the community provided package repository, change
      the base url to http://cloudstack.apt-get.eu/rhel/4.2/

      If you're using your own package repository, change this line to
      read as appropriate for your 4.3 repository.

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package by upgrading the older
      ``cloudstack-management`` package.

      .. code:: bash

          $ sudo yum upgrade cloudstack-management

   #. 

      For KVM hosts, you will need to upgrade the ``cloud-agent``
      package, similarly installing the new version as
      ``cloudstack-agent``.

      .. code:: bash

          $ sudo yum upgrade cloudstack-agent

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. code:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. code:: bash

          service cloudstack-agent stop
          killall jsvc
          service cloudstack-agent start

#. 

   Now it's time to restart the management server

   .. code:: bash

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

   .. code:: bash

       # nohup cloudstack-sysvmadm -d IP address -u cloud -p -a > sysvm.log 2>&1 &

   You can monitor the log for progress. The process of restarting the
   system VMs can take an hour or more.

   .. code:: bash

       # tail -f sysvm.log

   The output to ``sysvm.log`` will look something like this:

   .. code:: bash

       Stopping and starting 1 secondary storage vm(s)...
       Done stopping and starting secondary storage vm(s)
       Stopping and starting 1 console proxy vm(s)...
       Done stopping and starting console proxy vm(s).
       Stopping and starting 4 running routing vm(s)...
       Done restarting router(s).

#. .. note:: **For Xen Hosts: Copy vhd-utils:** This step is only for CloudStack installs that are using Xen hosts.

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

      Hypervisor

      Description

      XenServer

      Name: systemvm-xenserver-4.3

      Description: systemvm-xenserver-4.3

      URL:http://download.cloud.com/templates/4.3/systemvmtemplate-2014-07-12-master-xen.vhd.bz2

      Zone: Choose the zone where this hypervisor is used

      Hypervisor: XenServer

      Format: VHD

      OS Type: Debian GNU/Linux 7.0 (32-bit) (or the highest Debian
      release number available in the dropdown)

      Extractable: no

      Password Enabled: no

      Public: no

      Featured: no

      KVM

      Name: systemvm-kvm-4.3

      Description: systemvm-kvm-4.3

      URL:
      http://download.cloud.com/templates/4.3/systemvmtemplate-2014-06-12-master-kvm.qcow2.bz2

      Zone: Choose the zone where this hypervisor is used

      Hypervisor: KVM

      Format: QCOW2

      OS Type: Debian GNU/Linux 7.0 (32-bit) (or the highest Debian
      release number available in the dropdown)

      Extractable: no

      Password Enabled: no

      Public: no

      Featured: no

      VMware

      Name: systemvm-vmware-4.3

      Description: systemvm-vmware-4.3

      URL:
      http://download.cloud.com/templates/4.3/systemvmtemplate-4.3-vh7.ova

      Zone: Choose the zone where this hypervisor is used

      Hypervisor: VMware

      Format: OVA

      OS Type: Debian GNU/Linux 7.0 (32-bit) (or the highest Debian
      release number available in the dropdown)

      Extractable: no

      Password Enabled: no

      Public: no

      Featured: no

#. 

   Create RPM or Debian packages (as appropriate) and a repository from
   the 4.2.1 source, or check the Apache CloudStack downloads page at
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

   .. code:: bash

       # service cloudstack-management stop

#. 

   If you are running a usage server or usage servers, stop those as
   well:

   .. code:: bash

       # service cloudstack-usage stop

#. 

   Make a backup of your MySQL database. If you run into any issues or
   need to roll back the upgrade, this will assist in debugging or
   restoring your existing environment. You'll be prompted for your
   password.

   .. code:: bash

       # mysqldump -u root -p cloud > cloudstack-backup.sql

#. 

   (KVM Only) If primary storage of type local storage is in use, the
   path for this storage needs to be verified to ensure it passes new
   validation. Check local storage by querying the cloud.storage\_pool
   table:

   .. code:: bash

       #mysql -u cloud -p -e "select id,name,path from cloud.storage_pool where pool_type='Filesystem'"

   If local storage paths are found to have a trailing forward slash,
   remove it:

   .. code:: bash

       #mysql -u cloud -p -e 'update cloud.storage_pool set path="/var/lib/libvirt/images" where path="/var/lib/libvirt/images/"';

#. 

   If you are using Ubuntu, follow this procedure to upgrade your
   packages. If not, skip to step `11 <#upgrade-rpm-packages-41to42>`__.

   .. note:: **Community Packages:** This section assumes you're using the community supplied packages for CloudStack. If you've created your own packages and APT repository, substitute your own URL for the ones used in these examples.

   #. 

      The first order of business will be to change the sources list for
      each system with CloudStack packages. This means all management
      servers, and any hosts that have the KVM agent. (No changes should
      be necessary for hosts that are running VMware or Xen.)

      Start by opening ``/etc/apt/sources.list.d/cloudstack.list`` on
      any systems that have CloudStack packages installed.

      This file should have one line, which contains:

      .. code:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.0

      We'll change it to point to the new package repository:

      .. code:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.2

      If you're using your own package repository, change this line to
      read as appropriate for your 4.3 repository.

   #. 

      Now update your apt package list:

      .. code:: bash

          $ sudo apt-get update

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package. This will pull in any other
      dependencies you need.

      .. code:: bash

          $ sudo apt-get install cloudstack-management

   #. 

      You will need to manually install the ``cloudstack-agent``
      package:

      .. code:: bash

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

      .. code:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. code:: bash

          service cloudstack-agent stop
          killall jsvc
          service cloudstack-agent start

#. 

   (VMware only) Additional steps are required for each VMware cluster.
   These steps will not affect running guests in the cloud. These steps
   are required only for clouds using VMware clusters:

   #. 

      Stop the Management Server:

      .. code:: bash

          service cloudstack-management stop

   #. 

      Generate the encrypted equivalent of your vCenter password:

      .. code:: bash

          java -classpath /usr/share/cloudstack-common/lib/jasypt-1.9.0.jar org.jasypt.intf.cli.JasyptPBEStringEncryptionCLI encrypt.sh input="_your_vCenter_password_" password="`cat /etc/cloudstack/management/key`" verbose=false

      Store the output from this step, we need to add this in
      cluster\_details table and vmware\_data\_center tables in place of
      the plain text password

   #. 

      Find the ID of the row of cluster\_details table that you have to
      update:

      .. code:: bash

          mysql -u <username> -p<password>

      .. code:: bash

          select * from cloud.cluster_details;

   #. 

      Update the plain text password with the encrypted one

      .. code:: bash

          update cloud.cluster_details set value = '_ciphertext_from_step_1_' where id = _id_from_step_2_;

   #. 

      Confirm that the table is updated:

      .. code:: bash

          select * from cloud.cluster_details;

   #. 

      Find the ID of the correct row of vmware\_data\_center that you
      want to update

      .. code:: bash

          select * from cloud.vmware_data_center;

   #. 

      update the plain text password with the encrypted one:

      .. code:: bash

          update cloud.vmware_data_center set password = '_ciphertext_from_step_1_' where id = _id_from_step_5_;

   #. 

      Confirm that the table is updated:

      .. code:: bash

          select * from cloud.vmware_data_center;

   #. 

      Start the CloudStack Management server

      .. code:: bash

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

      .. code:: bash

          # service cloud-agent stop

   #. 

      Update the agent software.

      .. code:: bash

          # yum update cloudstack-agent

   #. 

      Start the agent.

      .. code:: bash

          # service cloudstack-agent start

#. 

   If you are using CentOS or RHEL, follow this procedure to upgrade
   your packages. If not, skip to step
   `13 <#restart-system-vms-41to42>`__.

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

      .. code:: bash

          [apache-cloudstack]
          name=Apache CloudStack
          baseurl=http://cloudstack.apt-get.eu/rhel/4.0/
          enabled=1
          gpgcheck=0

      If you are using the community provided package repository, change
      the base url to http://cloudstack.apt-get.eu/rhel/4.2/

      If you're using your own package repository, change this line to
      read as appropriate for your 4.3 repository.

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package by upgrading the older
      ``cloudstack-management`` package.

      .. code:: bash

          $ sudo yum upgrade cloudstack-management

   #. 

      For KVM hosts, you will need to upgrade the ``cloud-agent``
      package, similarly installing the new version as
      ``cloudstack-agent``.

      .. code:: bash

          $ sudo yum upgrade cloudstack-agent

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. code:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. code:: bash

          service cloudstack-agent stop
          killall jsvc
          service cloudstack-agent start

#. 

   Now it's time to restart the management server

   .. code:: bash

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

   .. code:: bash

       # nohup cloudstack-sysvmadm -d IP address -u cloud -p -a > sysvm.log 2>&1 &

   You can monitor the log for progress. The process of restarting the
   system VMs can take an hour or more.

   .. code:: bash

       # tail -f sysvm.log

   The output to ``sysvm.log`` will look something like this:

   .. code:: bash

       Stopping and starting 1 secondary storage vm(s)...
       Done stopping and starting secondary storage vm(s)
       Stopping and starting 1 console proxy vm(s)...
       Done stopping and starting console proxy vm(s).
       Stopping and starting 4 running routing vm(s)...
       Done restarting router(s).

#. .. note:: **For Xen Hosts: Copy vhd-utils:** This step is only for CloudStack installs that are using Xen hosts.

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
   the 4.1.0 source, or check the Apache CloudStack downloads page at
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

      Hypervisor

      Description

      XenServer

      Name: systemvm-xenserver-4.3

      Description: systemvm-xenserver-4.3

      URL:http://download.cloud.com/templates/4.3/systemvmtemplate-2013-07-12-master-xen.vhd.bz2

      Zone: Choose the zone where this hypervisor is used

      Hypervisor: XenServer

      Format: VHD

      OS Type: Debian GNU/Linux 7.0 (32-bit) (or the highest Debian
      release number available in the dropdown)

      Extractable: no

      Password Enabled: no

      Public: no

      Featured: no

      KVM

      Name: systemvm-kvm-4.3

      Description: systemvm-kvm-4.3

      URL:
      http://download.cloud.com/templates/4.3/systemvmtemplate-2013-06-12-master-kvm.qcow2.bz2

      Zone: Choose the zone where this hypervisor is used

      Hypervisor: KVM

      Format: QCOW2

      OS Type: Debian GNU/Linux 7.0 (32-bit) (or the highest Debian
      release number available in the dropdown)

      Extractable: no

      Password Enabled: no

      Public: no

      Featured: no

      VMware

      Name: systemvm-vmware-4.3

      Description: systemvm-vmware-4.3

      URL:
      http://download.cloud.com/templates/4.3/systemvmtemplate-4.2-vh7.ova

      Zone: Choose the zone where this hypervisor is used

      Hypervisor: VMware

      Format: OVA

      OS Type: Debian GNU/Linux 7.0 (32-bit) (or the highest Debian
      release number available in the dropdown)

      Extractable: no

      Password Enabled: no

      Public: no

      Featured: no

#. 

   Stop your management server or servers. Run this on all management
   server hosts:

   .. code:: bash

       # service cloud-management stop

#. 

   If you are running a usage server or usage servers, stop those as
   well:

   .. code:: bash

       # service cloud-usage stop

#. 

   Make a backup of your MySQL database. If you run into any issues or
   need to roll back the upgrade, this will assist in debugging or
   restoring your existing environment. You'll be prompted for your
   password.

   .. code:: bash

       # mysqldump -u root -p cloud > cloudstack-backup.sql

#. 

   Whether you're upgrading a Red Hat/CentOS based system or Ubuntu
   based system, you're going to need to stop the CloudStack management
   server before proceeding.

   .. code:: bash

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

   Modify componentsContext.xml, and make PlainTextUserAuthenticator as
   the default authenticator (1st entry in the userAuthenticators
   adapter list is default)

   .. code:: bash

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

      .. code:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.0

      We'll change it to point to the new package repository:

      .. code:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.1

      If you're using your own package repository, change this line to
      read as appropriate for your 4.1.0 repository.

   #. 

      Now update your apt package list:

      .. code:: bash

          $ sudo apt-get update

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package. This will pull in any other
      dependencies you need.

      .. code:: bash

          $ sudo apt-get install cloudstack-management

   #. 

      You will need to manually install the ``cloudstack-agent``
      package:

      .. code:: bash

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

      .. code:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. code:: bash

                                          service cloud-agent stop
                                          killall jsvc
                                          service cloudstack-agent start

   #. 

      During the upgrade, ``log4j-cloud.xml`` was simply copied over, so
      the logs will continue to be added to
      ``/var/log/cloud/agent/agent.log``. There's nothing *wrong* with
      this, but if you prefer to be consistent, you can change this by
      copying over the sample configuration file:

      .. code:: bash

                                          cd /etc/cloudstack/agent
                                          mv log4j-cloud.xml.dpkg-dist log4j-cloud.xml
                                          service cloudstack-agent restart

   #. 

      Once the agent is running, you can uninstall the old cloud-\*
      packages from your system:

      .. code:: bash

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

      .. code:: bash

                                          [apache-cloudstack]
                                          name=Apache CloudStack
                                          baseurl=http://cloudstack.apt-get.eu/rhel/4.0/
                                          enabled=1
                                          gpgcheck=0

      If you are using the community provided package repository, change
      the baseurl to http://cloudstack.apt-get.eu/rhel/4.1/

      If you're using your own package repository, change this line to
      read as appropriate for your 4.3 repository.

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package by upgrading the older
      ``cloud-client`` package.

      .. code:: bash

          $ sudo yum upgrade cloud-client

   #. 

      For KVM hosts, you will need to upgrade the ``cloud-agent``
      package, similarly installing the new version as
      ``cloudstack-agent``.

      .. code:: bash

          $ sudo yum upgrade cloud-agent

      During the installation of ``cloudstack-agent``, the RPM will copy
      your ``agent.properties``, ``log4j-cloud.xml``, and
      ``environment.properties`` from ``/etc/cloud/agent`` to
      ``/etc/cloudstack/agent``.

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. code:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. code:: bash

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

   .. code:: bash

       # nohup cloudstack-sysvmadm -d IP address -u cloud -p -a > sysvm.log 2>&1 &

   You can monitor the log for progress. The process of restarting the
   system VMs can take an hour or more.

   .. code:: bash

       # tail -f sysvm.log

   The output to ``sysvm.log`` will look something like this:

   .. code:: bash

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

      Hypervisor

      Description

      XenServer

      Name: systemvm-xenserver-4.2

      Description: systemvm-xenserver-4.2

      URL:http://download.cloud.com/templates/4.2/systemvmtemplate-2013-07-12-master-xen.vhd.bz2

      Zone: Choose the zone where this hypervisor is used

      Hypervisor: XenServer

      Format: VHD

      OS Type: Debian GNU/Linux 7.0 (32-bit) (or the highest Debian
      release number available in the dropdown)

      Extractable: no

      Password Enabled: no

      Public: no

      Featured: no

      KVM

      Name: systemvm-kvm-4.2

      Description: systemvm-kvm-4.2

      URL:
      http://download.cloud.com/templates/4.2/systemvmtemplate-2013-06-12-master-kvm.qcow2.bz2

      Zone: Choose the zone where this hypervisor is used

      Hypervisor: KVM

      Format: QCOW2

      OS Type: Debian GNU/Linux 7.0 (32-bit) (or the highest Debian
      release number available in the dropdown)

      Extractable: no

      Password Enabled: no

      Public: no

      Featured: no

      VMware

      Name: systemvm-vmware-4.2

      Description: systemvm-vmware-4.2

      URL:
      http://download.cloud.com/templates/4.2/systemvmtemplate-4.2-vh7.ova

      Zone: Choose the zone where this hypervisor is used

      Hypervisor: VMware

      Format: OVA

      OS Type: Debian GNU/Linux 7.0 (32-bit) (or the highest Debian
      release number available in the dropdown)

      Extractable: no

      Password Enabled: no

      Public: no

      Featured: no

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

      .. code:: bash

                      [upgrade]
                      name=rhel63
                      baseurl=url-of-your-rhel6.3-repo
                      enabled=1
                      gpgcheck=0
                      [apache CloudStack]
                      name= Apache CloudStack
                      baseurl= http://cloudstack.apt-get.eu/rhel/4.0/
                      enabled=1
                      gpgcheck=0

      If you are using the community provided package repository, change
      the baseurl to http:// cloudstack.apt-get.eu/rhel/4.2/

      If you are using your own package repository, change this line to
      read as appropriate for your 4.2.0 repository.

   #. 

      Now that you have the repository configured, upgrade the host
      operating system from RHEL 6.0 to 6.3:

      .. code:: bash

          # yum upgrade

#. 

   Stop all Usage Servers if running. Run this on all Usage Server
   hosts.

   .. code:: bash

       # service cloud-usage stop

#. 

   Stop the Management Servers. Run this on all Management Server hosts.

   .. code:: bash

       # service cloud-management stop

#. 

   On the MySQL master, take a backup of the MySQL databases. We
   recommend performing this step even in test upgrades. If there is an
   issue, this will assist with debugging.

   In the following commands, it is assumed that you have set the root
   password on the database, which is a CloudStack recommended best
   practice. Substitute your own MySQL root password.

   .. code:: bash

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

      .. code:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.0

      We'll change it to point to the new package repository:

      .. code:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.2

      If you're using your own package repository, change this line to
      read as appropriate for your 4.3 repository.

   #. 

      Now update your apt package list:

      .. code:: bash

          $ sudo apt-get update

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package. This will pull in any other
      dependencies you need.

      .. code:: bash

          $ sudo apt-get install cloudstack-management

   #. 

      You will need to manually install the ``cloudstack-agent``
      package:

      .. code:: bash

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

      .. code:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. code:: bash

          service cloud-agent stop
          killall jsvc
          service cloudstack-agent start

   #. 

      During the upgrade, ``log4j-cloud.xml`` was simply copied over, so
      the logs will continue to be added to
      ``/var/log/cloud/agent/agent.log``. There's nothing *wrong* with
      this, but if you prefer to be consistent, you can change this by
      copying over the sample configuration file:

      .. code:: bash

          cd /etc/cloudstack/agent
          mv log4j-cloud.xml.dpkg-dist log4j-cloud.xml
          service cloudstack-agent restart

   #. 

      Once the agent is running, you can uninstall the old cloud-\*
      packages from your system:

      .. code:: bash

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

      .. code:: bash

          [apache-cloudstack]
          name=Apache CloudStack
          baseurl=http://cloudstack.apt-get.eu/rhel/4.0/
          enabled=1
          gpgcheck=0

      If you are using the community provided package repository, change
      the baseurl to http://cloudstack.apt-get.eu/rhel/4.2/

      If you're using your own package repository, change this line to
      read as appropriate for your 4.2.0 repository.

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package by upgrading the older
      ``cloud-client`` package.

      .. code:: bash

          $ sudo yum upgrade cloud-client

   #. 

      For KVM hosts, you will need to upgrade the ``cloud-agent``
      package, similarly installing the new version as
      ``cloudstack-agent``.

      .. code:: bash

          $ sudo yum upgrade cloud-agent

      During the installation of ``cloudstack-agent``, the RPM will copy
      your ``agent.properties``, ``log4j-cloud.xml``, and
      ``environment.properties`` from ``/etc/cloud/agent`` to
      ``/etc/cloudstack/agent``.

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. code:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. code:: bash

          service cloud-agent stop
          killall jsvc
          service cloudstack-agent start

#. 

   If you have made changes to your copy of
   ``/etc/cloud/management/components.xml`` the changes will be
   preserved in the upgrade. However, you need to do the following steps
   to place these changes in a new version of the file which is
   compatible with version 4.2.0.

   #. 

      Make a backup copy of ``/etc/cloud/management/components.xml``.
      For example:

      .. code:: bash

          # mv /etc/cloud/management/components.xml /etc/cloud/management/components.xml-backup

   #. 

      Copy ``/etc/cloud/management/components.xml.rpmnew`` to create a
      new ``/etc/cloud/management/components.xml``:

      .. code:: bash

          # cp -ap /etc/cloud/management/components.xml.rpmnew /etc/cloud/management/components.xml

   #. 

      Merge your changes from the backup file into the new
      ``components.xml``.

      .. code:: bash

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

   .. code:: bash

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

   .. code:: bash

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

      .. code:: bash

           # cloudstack-agent-upgrade

   #. 

      Install a libvirt hook with the following commands:

      .. code:: bash

           # mkdir /etc/libvirt/hooks
           # cp /usr/share/cloudstack-agent/lib/libvirtqemuhook /etc/libvirt/hooks/qemu
           # chmod +x /etc/libvirt/hooks/qemu

   #. 

      Restart libvirtd.

      .. code:: bash

          # service libvirtd restart

   #. 

      Start the agent.

      .. code:: bash

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

      .. code:: bash

          # xe host-list

      Then use the following command to apply the hotfix. Replace the
      example host UUID with the current host ID, and replace the hotfix
      UUID with the output from the patch-upload command you ran on this
      machine earlier. You can also get the hotfix UUID by running xe
      patch-list.

      .. code:: bash

          xe patch-apply host-uuid=host-uuid uuid=hotfix-uuid

   #. 

      Copy the following files from the CloudStack Management Server to
      the host.

      Copy from here...

      ...to here

      /usr/lib64/cloud/common/scripts/vm/hypervisor/xenserver/xenserver60/NFSSR.py

      /opt/xensource/sm/NFSSR.py

      /usr/lib64/cloud/common/scripts/vm/hypervisor/xenserver/setupxenserver.sh

      /opt/xensource/bin/setupxenserver.sh

      /usr/lib64/cloud/common/scripts/vm/hypervisor/xenserver/make\_migratable.sh

      /opt/xensource/bin/make\_migratable.sh

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

         .. code:: bash

             # tar xf xenserver-cloud-supp.tgz

      -  

         Run the following script:

         .. code:: bash

             # xe-install-supplemental-pack xenserver-cloud-supp.iso

      -  

         If the XenServer host is part of a zone that uses basic
         networking, disable Open vSwitch (OVS):

         .. code:: bash

             # xe-switch-network-backend  bridge

   #. 

      Reboot this XenServer host.

   #. 

      Run the following:

      .. code:: bash

          /opt/xensource/bin/setupxenserver.sh

      .. note:: If the message "mv: cannot stat \`/etc/cron.daily/logrotate': No such file or directory" appears, you can safely ignore it.

   #. 

      Run the following:

      .. code:: bash

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

      Hypervisor

      Description

      XenServer

      Name: systemvm-xenserver-4.3

      Description: systemvm-xenserver-4.3

      URL:http://download.cloud.com/templates/4.3/systemvmtemplate-2013-07-12-master-xen.vhd.bz2

      Zone: Choose the zone where this hypervisor is used

      Hypervisor: XenServer

      Format: VHD

      OS Type: Debian GNU/Linux 7.0 (32-bit) (or the highest Debian
      release number available in the dropdown)

      Extractable: no

      Password Enabled: no

      Public: no

      Featured: no

      KVM

      Name: systemvm-kvm-4.3

      Description: systemvm-kvm-4.3

      URL:
      http://download.cloud.com/templates/4.3/systemvmtemplate-2013-06-12-master-kvm.qcow2.bz2

      Zone: Choose the zone where this hypervisor is used

      Hypervisor: KVM

      Format: QCOW2

      OS Type: Debian GNU/Linux 7.0 (32-bit) (or the highest Debian
      release number available in the dropdown)

      Extractable: no

      Password Enabled: no

      Public: no

      Featured: no

      VMware

      Name: systemvm-vmware-4.3

      Description: systemvm-vmware-4.3

      URL:
      http://download.cloud.com/templates/4.3/systemvmtemplate-4.2-vh7.ova

      Zone: Choose the zone where this hypervisor is used

      Hypervisor: VMware

      Format: OVA

      OS Type: Debian GNU/Linux 7.0 (32-bit) (or the highest Debian
      release number available in the dropdown)

      Extractable: no

      Password Enabled: no

      Public: no

      Featured: no

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

      .. code:: bash

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
      read as appropriate for your 4.2.0 repository.

   #. 

      Now that you have the repository configured, upgrade the host
      operating system from RHEL 6.0 to 6.3:

      .. code:: bash

          # yum upgrade

#. 

   Stop all Usage Servers if running. Run this on all Usage Server
   hosts.

   .. code:: bash

       # service cloud-usage stop

#. 

   Stop the Management Servers. Run this on all Management Server hosts.

   .. code:: bash

       # service cloud-management stop

#. 

   On the MySQL master, take a backup of the MySQL databases. We
   recommend performing this step even in test upgrades. If there is an
   issue, this will assist with debugging.

   In the following commands, it is assumed that you have set the root
   password on the database, which is a CloudStack recommended best
   practice. Substitute your own MySQL root password.

   .. code:: bash

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

      .. code:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.0

      We'll change it to point to the new package repository:

      .. code:: bash

          deb http://cloudstack.apt-get.eu/ubuntu precise 4.2

      If you're using your own package repository, change this line to
      read as appropriate for your 4.2.0 repository.

   #. 

      Now update your apt package list:

      .. code:: bash

          $ sudo apt-get update

   #. 

      Now that you have the repository configured, it's time to install
      the ``cloudstack-management`` package. This will pull in any other
      dependencies you need.

      .. code:: bash

          $ sudo apt-get install cloudstack-management

   #. 

      On KVM hosts, you will need to manually install the
      ``cloudstack-agent`` package:

      .. code:: bash

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

      .. code:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. code:: bash

          service cloud-agent stop
          killall jsvc
          service cloudstack-agent start

   #. 

      During the upgrade, ``log4j-cloud.xml`` was simply copied over, so
      the logs will continue to be added to
      ``/var/log/cloud/agent/agent.log``. There's nothing *wrong* with
      this, but if you prefer to be consistent, you can change this by
      copying over the sample configuration file:

      .. code:: bash

          cd /etc/cloudstack/agent
          mv log4j-cloud.xml.dpkg-dist log4j-cloud.xml
          service cloudstack-agent restart

   #. 

      Once the agent is running, you can uninstall the old cloud-\*
      packages from your system:

      .. code:: bash

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

      .. code:: bash

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

      .. code:: bash

          $ sudo yum upgrade cloud-client

   #. 

      For KVM hosts, you will need to upgrade the ``cloud-agent``
      package, similarly installing the new version as
      ``cloudstack-agent``.

      .. code:: bash

          $ sudo yum upgrade cloud-agent

      During the installation of ``cloudstack-agent``, the RPM will copy
      your ``agent.properties``, ``log4j-cloud.xml``, and
      ``environment.properties`` from ``/etc/cloud/agent`` to
      ``/etc/cloudstack/agent``.

   #. 

      Verify that the file
      ``/etc/cloudstack/agent/environment.properties`` has a line that
      reads:

      .. code:: bash

          paths.script=/usr/share/cloudstack-common

      If not, add the line.

   #. 

      Restart the agent:

      .. code:: bash

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

   .. code:: bash

       warning: /etc/cloud/management/components.xml created as /etc/cloud/management/components.xml.rpmnew

   #. 

      Make a backup copy of your
      ``/etc/cloud/management/components.xml`` file. For example:

      .. code:: bash

          # mv /etc/cloud/management/components.xml /etc/cloud/management/components.xml-backup

   #. 

      Copy ``/etc/cloud/management/components.xml.rpmnew`` to create a
      new ``/etc/cloud/management/components.xml``:

      .. code:: bash

          # cp -ap /etc/cloud/management/components.xml.rpmnew /etc/cloud/management/components.xml

   #. 

      Merge your changes from the backup file into the new
      components.xml file.

      .. code:: bash

          # vi /etc/cloudstack/management/components.xml

#. 

   After upgrading to 4.3, API clients are expected to send plain text
   passwords for login and user creation, instead of MD5 hash. If API
   client changes are not acceptable, following changes are to be made
   for backward compatibility:

   Modify componentContext.xml, and make PlainTextUserAuthenticator as
   the default authenticator (1st entry in the userAuthenticators
   adapter list is default)

   .. code:: xml

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

      .. code:: bash

          # mv /etc/cloud/management/db.properties /etc/cloud/management/db.properties-backup

   #. 

      Copy ``/etc/cloud/management/db.properties.rpmnew`` to create a
      new ``/etc/cloud/management/db.properties``:

      .. code:: bash

          # cp -ap /etc/cloud/management/db.properties.rpmnew etc/cloud/management/db.properties

   #. 

      Merge your changes from the backup file into the new db.properties
      file.

      .. code:: bash

          # vi /etc/cloudstack/management/db.properties

#. 

   On the management server node, run the following command. It is
   recommended that you use the command-line flags to provide your own
   encryption keys. See Password and Key Encryption in the Installation
   Guide.

   .. code:: bash

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

   .. code:: bash

       # service cloudstack-management start

   Wait until the databases are upgraded. Ensure that the database
   upgrade is complete. You should see a message like "Complete! Done."
   After confirmation, start the other Management Servers one at a time
   by running the same command on each node.

#. 

   Start all Usage Servers (if they were running on your previous
   version). Perform this on each Usage Server host.

   .. code:: bash

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

      .. code:: bash

          # service cloud-agent stop

   #. 

      Update the agent software with one of the following command sets
      as appropriate.

      .. code:: bash

          # yum update cloud-*

      .. code:: bash

           # apt-get update
           # apt-get upgrade cloud-*

   #. 

      Copy the contents of the ``agent.properties`` file to the new
      ``agent.properties`` file by using the following command

      .. code:: bash

          sed -i 's/com.cloud.agent.resource.computing.LibvirtComputingResource/com.cloud.hypervisor.kvm.resource.LibvirtComputingResource/g' /etc/cloudstack/agent/agent.properties

   #. 

      Upgrade all the existing bridge names to new bridge names by
      running this script:

      .. code:: bash

           # cloudstack-agent-upgrade

   #. 

      Install a libvirt hook with the following commands:

      .. code:: bash

           # mkdir /etc/libvirt/hooks
           # cp /usr/share/cloudstack-agent/lib/libvirtqemuhook /etc/libvirt/hooks/qemu
           # chmod +x /etc/libvirt/hooks/qemu

   #. 

      Restart libvirtd.

      .. code:: bash

          # service libvirtd restart

   #. 

      Start the agent.

      .. code:: bash

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

      .. code:: bash

          # nohup cloudstack-sysvmadm -d 192.168.1.5 -u cloud -p password -c -r > sysvm.log 2>&1 &
          # tail -f sysvm.log

      This might take up to an hour or more to run, depending on the
      number of accounts in the system.

   #. 

      After the script terminates, check the log to verify correct
      execution:

      .. code:: bash

          # tail -f sysvm.log

      The content should be like the following:

      .. code:: bash

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

   .. code:: bash

       # ssh -i private-key-path link-local-ip -p 3922
                               # cat /etc/cloudstack-release

   The output should be like the following:

   .. code:: bash

       Cloudstack Release 4.0.0-incubating Mon Oct 9 15:10:04 PST 2012

   **ESXi:**

   SSH in using the private IP address of the system VM. For example, in
   the command below, substitute your own path to the private key used
   to log in to the system VM and your own private IP.

   Run the following commands on the Management Server:

   .. code:: bash

       # ssh -i private-key-path private-ip -p 3922
                               # cat /etc/cloudstack-release

   The output should be like the following:

   .. code:: bash

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

      .. code:: bash

          /opt/xensource/bin/cloud-clean-vlan.sh

   #. 

      Prepare the upgrade by running the following on one XenServer
      host:

      .. code:: bash

          /opt/xensource/bin/cloud-prepare-upgrade.sh

      If you see a message like "can't eject CD", log in to the VM and
      umount the CD, then run this script again.

   #. 

      Upload the hotfix to the XenServer hosts. Always start with the
      Xen pool master, then the slaves. Using your favorite file copy
      utility (e.g. WinSCP), copy the hotfixes to the host. Place them
      in a temporary folder such as /root or /tmp.

      On the Xen pool master, upload the hotfix with this command:

      .. code:: bash

          xe patch-upload file-name=XS602E003.xsupdate

      Make a note of the output from this command, which is a UUID for
      the hotfix file. You'll need it in another step later.

      .. note:: (Optional) If you are applying other hotfixes as well, you can repeat the commands in this section with the appropriate hotfix number. For example, XS602E004.xsupdate.

   #. 

      Manually live migrate all VMs on this host to another host. First,
      get a list of the VMs on this host:

      .. code:: bash

          # xe vm-list

      Then use this command to migrate each VM. Replace the example host
      name and VM name with your own:

      .. code:: bash

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

      Copy from here...

      ...to here

      ``/usr/share/cloudstack-common/scripts/vm/hypervisor/xenserver/xenserver60/NFSSR.py``

      ``/opt/xensource/sm/NFSSR.py``

      ``/usr/share/cloudstack-common/scripts/vm/hypervisor/xenserver/setupxenserver.sh``

      ``/opt/xensource/bin/setupxenserver.sh``

      ``/usr/lib64/cloudstack-common/scripts/vm/hypervisor/xenserver/make_migratable.sh``

      ``/opt/xensource/bin/make_migratable.sh``

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

      .. code:: bash

        ``for pbd in `xe pbd-list currently-attached=false| grep ^uuid | awk '{print $NF}'`; do xe pbd-plug uuid=$pbd ; ``

   #. 

      On each slave host in the Xen pool, repeat these steps, starting
      from "manually live migrate VMs."

API Changes Introduced in 4.3
=============================

Hyper-V
------------

=================  =============================================================
API                Description
=================  =============================================================
addPrimaryStorage  To this existing API, the following field has been added: smb
addImageStore      To this existing API, the following field has been added: smb
=================  =============================================================

Reporting CPU Sockets
---------------------

========  ================================================================================
API       Description
========  ================================================================================
listhost  To this existing API, the following request parameter has been added: hypervisor. The new response parameter added is: cpusockets
========  ================================================================================

Publishing Alerts Using the Web ROOT Admin API
----------------------------------------------

=============  ===============================================================================================================
API            Description
=============  ===============================================================================================================
generateAlert  A new API has been added to generate and publish alerts for usage services. 
               The usage services can be installed on a different host or the same host where the Management Server is running.           This API is available only to the Root Admin.
listAlerts     To this existing API, a new response parameter has been added: name. An alert can be searched on the basis of alert name.
=============  ===============================================================================================================

Dynamic Compute Offering
------------------------

================  ==============================================================================
API               Description
================  ==============================================================================
DeployVM          To this existing API, the following request parameter has been added: details.
ScaleVM           To this existing API, the following request parameter has been added: details.
ScaleSystemVM     To this existing API, the following request parameter has been added: details.
UpgradeVM         To this existing API, the following request parameter has been added: details.
UpgradeSysytemVM  To this existing API, the following request parameter has been added: details.
================  ==============================================================================

Enhanced Upgrade for Virtual Routers
------------------------------------

=====================   ===========================================================================================================================API                     Description
=====================   ===========================================================================================================================upgradeRouterTemplate   This is a new API which has been added in this release.
                        The following are the request parameters:
                        -  
                            id: Upgrade the specified VR
						-  
   							zone\_id : Upgrade the VRs in the specified zone.
						-  
   							pod\_id : Upgrade the VRs in the specified pod.
						-  
   							cluster\_id : Upgrade the VRs in the specified cluster.
						-  
   							domain\_id : Upgrade the VRs belonging to the specified domain.
						-  
   							account\_id : Upgrade the VRs belonging to the specified account.

listRouters             For this existing API, the following request parameters has been added:
						-  
   							version: Lists routers by specified version.
						-  
   							zone\_id : lists routers in specified zone.
						-  
   							pod\_id : Lists routers in the specified pod.
						-  
   							cluster\_id : Lists routers in the specified cluster.
						-  
   							domain\_id : Lists routers owned by specified domain.
						- 
   							account: Lists routers owned by specified account.

						The following response parameters has been added:
						-  
   							version : (String) The router version. For example, 4.3.0.
						-  
   							requiresupgrade: (Boolean) The flag to indicate if the router template requires an upgrade.

=====================   ===========================================================================================================================
