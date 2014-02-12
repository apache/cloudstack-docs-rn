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
