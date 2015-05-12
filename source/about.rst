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
   

What's New in |version|
=======================

Version |release| includes more than 200 bug fixes from previous release, the
following new features and improvements.


NuageVsp Network Plugin
-----------------------

   The Nuage NetworksTM Virtualized Services Platform (VSP) is a Software-Defined
   Networking (SDN) solution that virtualizes any datacenter (DC) network
   infrastructure and automatically establishes connectivity between compute
   resources upon their creation.

   NuageVsp networking plugin bring the Nuage VSP network virtualization technology
   to CloudStack. All the network isolation and routing is handled by the Nuage
   SDN solution. Routing of the packets happen at hypervisor itself. Virtual Router
   is not used for routing the packets and is spawned only for Password reset
   functionality. The Nuage solution also helps significantly improve the agility
   and scale of a CloudStack deployment as compared to a Virtual Router based
   deployment.


   ====================== ============================================================================
   Supported hypervisors: XenServer, VMware
   Link                   `NuageVsp Network Plugin spec`_
   ====================== ============================================================================


Bind integration with Globo DNSAPI
----------------------------------
   
   GloboDNS provide API to Bind DNS server used to centralized DNS server outside of CloudStack networks.
   When deploying Advanced Networks, Virtual Routers are used to isolate networks
   and provide DNS service for all machines inside each network. This approach
   imposes a challenge when instances need to translate names that belong to
   instances from another network.

   ====================== ============================================================================
   Supported hypervisors: Any
   Link                   `Globo DNSAPI spec`_
   ====================== ============================================================================


SAML 2.0 Plugin
---------------
   
   SAML 2.0 Plugin provide integration of CloudStack to existing authentication
   mechanism. This provide Single Sign On (SSO) and Single Log Out (SLO) to work
   on CloudStack UI and clients. SAML (Security Assertion Markup Language) 2.0
   is an old, stable and widely used XML based authentication and authorization
   protocol supported by Salesforce, Google Apps and other public and private
   companies and the aim is to integrate the SSO SAML support in CloudStack. The
   current implementation is experimental, will change in future and should be
   avoided in prouduction.

   ====================== ============================================================================
   Supported hypervisors: N/A
   Link                   `SAML spec`_
   ====================== ============================================================================


Managed storage for KVM
-----------------------

   This adapter provides one to one mapping between SAN volume to VM's disk.
   This is to guarantee quality of services for performance sensitive
   applications. This adapter is based on nfs protocol.

   ====================== ============================================================================
   Supported hypervisors: KVM
   Link                   `CLOUDSTACK-7576 <https://issues.apache.org/jira/browse/CLOUDSTACK-7576>`_
   ====================== ============================================================================


Improved CloudByte Storage Plugin
---------------------------------

   The new improved CloudByte plugin support the following features:

   - Managed storage, where each vm disk has the guaranteed QoS.
   - Account integration in cloudbyte with respect to domains in CloudStack.
   - Resize of the volume.
   - both iSCSI and nfs protocols in XenServer.
   - iSCSI protocol for KVM and VMware ESX.
   - Storage level snapshot capabilities as well as hypervisor level snapshot feature. 
   - Expose custom API's for ui integration.
   - Unlimited storage nodes across the sites.

   ====================== ============================================================================
   Supported hypervisors: KVM, VMware, XenServer
   Link                   `CLOUDSTACK-7098 <https://issues.apache.org/jira/browse/CLOUDSTACK-7098>`_
   ====================== ============================================================================


Use SSH for commands sent to Virtual-Router
-------------------------------------------

   For XenServer host, sending commands to Virtual-Routers now use SSH,
   previously using XAPI plugin, this change reduce XAPI workload and allow
   Virtual-Router update while XenServer pool master is down.

   ====================== ============================================================================
   Supported hypervisors: XenServer
   Link                   `CLOUDSTACK-6314 <https://issues.apache.org/jira/browse/CLOUDSTACK-6314>`_
   ====================== ============================================================================


Baremetal Advanced Networking Support
-------------------------------------

This feature is about CloudStack network plugin for baremetal advanced
networking. With this plugin, CloudStack can automatically program vlan on
physical switch to which baremetal instances connect when creating/destroying
baremetal instance. This feature cannot work standalone, it needs support
from physical switch itself either from vendor's SDK or from an in-switch
agent for whitebox switch. When using this feature, baremetal instances gain
Layer 2 isolation methods provided by CloudStack advanced networking which is
particularly useful in public cloud that wants to provide baremetal as a
service.  This feature currently requires a VMware virtual router, so is only
supported by that hypervisor.

   ====================== ============================================================================
   Supported hypervisors: N/A
   Link                   `Baremetal feature spec`_
   ====================== ============================================================================


Instance Password Generation length can now be changed
------------------------------------------------------

   For instance using random password generated by CloudStack, Password length and
   encoder can now be define with following Global Settings:
   ``vm.password.length``, ``user.password.encoders.exclude``, ``user.password.encoders.order``


Improvements
------------

-  [UI] keep advanced search parameters visible after search has been run
-  [UI] Add new vGPU types K160Q, K180Q, K280Q
-  [LXC] storage migration for LXC VMs fixed
-  Use of MariaDB as cloudstack management server database
-  System VM password reset now supported
-  Root volume detach support
-  System VM local storage setting ``system.vm.use.local.storage`` is configurable at zone level
-  Ability to set CPU features for user vms on KVM using ``guest.cpu.features`` property
-  A threaded Python based password server that consumes less RAM and CPU
-  VMFS support in VMWare
-  XenServer 6.5 support
-  Separate /var/log partition in SystemVM template
-  VMXNET3 nic adapter support for KVM
-  ``nicAdapter`` VM detail is configurable for VMWare to set custom nic adapter
-  New secure and default user authenticator: PBKDF2-SHA-256
-  Resize volume support on KVM

.. _Baremetal feature spec: https://cwiki.apache.org/confluence/display/CLOUDSTACK/Baremetal+Advanced+Networking+Support
.. _Globo DNSAPI spec: https://cwiki.apache.org/confluence/display/CLOUDSTACK/Bind+integration+by+Globo+DNSAPI
.. _NuageVsp Network Plugin spec : https://cwiki.apache.org/confluence/display/CLOUDSTACK/NuageVsp+Network+Plugin
.. _SAML spec: https://cwiki.apache.org/confluence/display/CLOUDSTACK/SAML+2.0+Plugin
