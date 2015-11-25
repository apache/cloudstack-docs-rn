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

Version |release| includes more than 240 bug fixes from previous release, the
following new features and improvements.


Redundant Routers for VPC
-------------------------

Create VPC using an High Available pair of Virtual Routers in active-pasive mode.
The main goal behind its implementation is to increase critical application's
uptime, offering a better Disaster Recovery strategy by quickly switching
network traffic to a backup virtual router, hence increasing business continuity. 

====================== ============================================================================
Supported hypervisors: Any
Link                   `Redundant VR spec`_
====================== ============================================================================


UI: SSH keys and User-Data
--------------------------

It is now possible to import, delete and get instances inventory for SSH keys
from the webui at the account level. Instance can now be created with ssh key
and user-data defined from the webui wizard.

====================== ============================================================================
Supported hypervisors: N/A
Link                   `CLOUDSTACK-7882`_
====================== ============================================================================



Send statistics collected by StatsCollector to Graphite
-------------------------------------------------------

Send StatsCollector from the management server to a Graphite server in addition
to the usage database. This allows ease of graphing for CPU, Network and
Disk I/O for instances and hosts.

====================== ============================================================================
Supported hypervisors: Any
Link                   `CLOUDSTACK-7583`_
====================== ============================================================================


Browser-based Template/Volume upload
------------------------------------

This feature enables the users to directly upload template or volume to
Cloudstack and eliminates the dependency on an external http server. This is a
complementary functionality and users can continue to register template/volume
with URL.

====================== ============================================================================
Supported hypervisors: N/A
Link                   `Browser Upload spec`_
====================== ============================================================================


Run CloudStack inside Docker
----------------------------

Provide Docker images collection of Apache CloudStack modules thru automated
build on docker hub. These containers are usable for Continous Integration
tests, demo, rapid deployment of CloudStack for test purposes.

====================== ============================================================================
Supported hypervisors: N/A
Link                   https://hub.docker.com/u/cloudstack/
====================== ============================================================================


Deprecation of awsapi
---------------------

The module awsapi has been removed from the source code and replaced by ec2stack
(https://github.com/apache/cloudstack-ec2stack). Removal of awsapi change the
upgrade process to 4.6 from previous release as the RPM cloudstack-awsapi must
be removed. This deprecation removed close to 1 million lines of code from the
source base.

====================== ============================================================================
Supported hypervisors: N/A
Link                   `CLOUDSTACK-8433`_
====================== ============================================================================


Improvements
------------

Here is the list of `new features and improvements <https://issues.apache.org/jira/issues/?filter=12332938>`_: 

.. cssclass:: table-striped table-bordered table-hover

==================  ===================================================================================
Jira ID             Description
==================  ===================================================================================
`CLOUDSTACK-8301`_  Enable configuring local storage use for system VMs at zone level...
`CLOUDSTACK-7924`_  Browser-based Template / Volume upload...
`CLOUDSTACK-7583`_  Send statistics collected by StatsCollector to optional Graphite host...
`CLOUDSTACK-5863`_  Restore volume snapshot...
`CLOUDSTACK-8489`_  Provide smbios vendor information via KVM/Libvirt to Guest...
`CLOUDSTACK-8324`_  DHCP/DNS offload and config drive support for adv shared network...
`CLOUDSTACK-8313`_  Local Storage overprovisioning should be possible...
`CLOUDSTACK-8744`_  Add missing localization (l10n) for several parts in the UI...
`CLOUDSTACK-8740`_  make UI style customisation easier...
`CLOUDSTACK-8840`_  Update systemd profile for usage server...
`CLOUDSTACK-8252`_  KVM vlan passthrough 4095...
`CLOUDSTACK-8016`_  return code of the call to cloudstack-setup-agent is not checked...
`CLOUDSTACK-8036`_  SAML plugin provides no way to save IDP metadata in DB or file...
`CLOUDSTACK-7983`_  Create Disk/Service Offering for Domain Admin...
`CLOUDSTACK-7882`_  SSH Keypair Creation/Selection in UI...
`CLOUDSTACK-7908`_  Addition of userid field to vm_instance table to identify user that created the ...
`CLOUDSTACK-7847`_  API: listDomains should display the domain resources, similar to listAccounts...
`CLOUDSTACK-7698`_  Don't (acquire IP/create NAT) by default while deploying VM if not necessary...
`CLOUDSTACK-6139`_  System.vm.use.local.storage global setting to zone setting...
`CLOUDSTACK-8486`_  Refactoring LibVirt (KVM) Hypervisor Plugin...
`CLOUDSTACK-8477`_  Refactoring XenServer Hypervisor Plugin...
`CLOUDSTACK-8506`_  Make ACS compliant with the RFC 3021...
`CLOUDSTACK-8502`_  Implement Annotions for XenServer and Libvirt resources...
`CLOUDSTACK-8647`_  LDAP Trust AD and Autoimport...
`CLOUDSTACK-8635`_  Ubuntu packages should depend on OpenJDK headless JRE...
`CLOUDSTACK-8625`_  Systemd profile for KVM Agent...
`CLOUDSTACK-8624`_  cloud-install-sys-tmplt: add support for mysql port and optimise the disk capaci...
`CLOUDSTACK-8607`_  As an Operator I want to be able to change the host password on the host itself ...
`CLOUDSTACK-8596`_  [LDAP] Nested groups, ability of recursively querying nested groups...
`CLOUDSTACK-8590`_  Refactoring NiciraNVP resource...
`CLOUDSTACK-8589`_  As an operator I want to be able to change the KVM hypervisor credentials...
`CLOUDSTACK-8580`_  Users should be able to expunge VMs...
`CLOUDSTACK-8581`_  Make S3 TCP KeepAlive and ConnectionTtl configureable...
`CLOUDSTACK-8426`_  Use a separate thread pool for VR reboot in case of out-of-band movement...
`CLOUDSTACK-8424`_  KVM: allow a way to add CPU flags/features specific to a host...
`CLOUDSTACK-8457`_  Make SAML plugin production grade...
`CLOUDSTACK-9034`_  Cloudstack-docs-admin has rst files bullet list incorrectly terminated...
`CLOUDSTACK-8272`_  Improve password serving script by making it non-blocking non-locking concurrent...
`CLOUDSTACK-8197`_  make minimal sysvm version configuratble...
`CLOUDSTACK-8151`_  An API to cleanup cloud_usage table...
`CLOUDSTACK-8133`_  Add instance count to listSecurityGroups API call....
`CLOUDSTACK-8169`_  Dynamic storage adaptor detection for KVM agent...
`CLOUDSTACK-8063`_  list secondary Ips information in VM response...
`CLOUDSTACK-4719`_  Document details parameter of registerTemplate...
`CLOUDSTACK-1667`_  improve explanation of extractable ISO...
`CLOUDSTACK-8989`_  component/test_ps_limits.py can also be run on a "basic" setup...
`CLOUDSTACK-8992`_  Allow more then 6 disks to be connected to a KVM VM....
`CLOUDSTACK-9044`_  RBD Primary Storage isn't shown in the Zone Wizard...
==================  ===================================================================================


.. _Redundant VR spec : https://cwiki.apache.org/confluence/display/CLOUDSTACK/Redundant+Virtual+Routers+for+Virtual+Private+Clouds
.. _Browser Upload spec : https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=39620237
.. _CLOUDSTACK-7583 : https://issues.apache.org/jira/browse/CLOUDSTACK-7583
.. _CLOUDSTACK-7882 : https://issues.apache.org/jira/browse/CLOUDSTACK-7882
.. _Community supported CoreOS templates for CloudStack : https://coreos.com/os/docs/latest/booting-on-cloudstack.html

.. _CLOUDSTACK-8301 : https://issues.apache.org/jira/browse/CLOUDSTACK-8301
.. _CLOUDSTACK-7924 : https://issues.apache.org/jira/browse/CLOUDSTACK-7924
.. _CLOUDSTACK-7583 : https://issues.apache.org/jira/browse/CLOUDSTACK-7583
.. _CLOUDSTACK-5863 : https://issues.apache.org/jira/browse/CLOUDSTACK-5863
.. _CLOUDSTACK-8489 : https://issues.apache.org/jira/browse/CLOUDSTACK-8489
.. _CLOUDSTACK-8324 : https://issues.apache.org/jira/browse/CLOUDSTACK-8324
.. _CLOUDSTACK-8313 : https://issues.apache.org/jira/browse/CLOUDSTACK-8313
.. _CLOUDSTACK-8744 : https://issues.apache.org/jira/browse/CLOUDSTACK-8744
.. _CLOUDSTACK-8740 : https://issues.apache.org/jira/browse/CLOUDSTACK-8740
.. _CLOUDSTACK-8840 : https://issues.apache.org/jira/browse/CLOUDSTACK-8840
.. _CLOUDSTACK-8252 : https://issues.apache.org/jira/browse/CLOUDSTACK-8252
.. _CLOUDSTACK-8016 : https://issues.apache.org/jira/browse/CLOUDSTACK-8016
.. _CLOUDSTACK-8036 : https://issues.apache.org/jira/browse/CLOUDSTACK-8036
.. _CLOUDSTACK-7983 : https://issues.apache.org/jira/browse/CLOUDSTACK-7983
.. _CLOUDSTACK-7882 : https://issues.apache.org/jira/browse/CLOUDSTACK-7882
.. _CLOUDSTACK-7908 : https://issues.apache.org/jira/browse/CLOUDSTACK-7908
.. _CLOUDSTACK-7847 : https://issues.apache.org/jira/browse/CLOUDSTACK-7847
.. _CLOUDSTACK-7698 : https://issues.apache.org/jira/browse/CLOUDSTACK-7698
.. _CLOUDSTACK-6139 : https://issues.apache.org/jira/browse/CLOUDSTACK-6139
.. _CLOUDSTACK-8486 : https://issues.apache.org/jira/browse/CLOUDSTACK-8486
.. _CLOUDSTACK-8477 : https://issues.apache.org/jira/browse/CLOUDSTACK-8477
.. _CLOUDSTACK-8506 : https://issues.apache.org/jira/browse/CLOUDSTACK-8506
.. _CLOUDSTACK-8502 : https://issues.apache.org/jira/browse/CLOUDSTACK-8502
.. _CLOUDSTACK-8647 : https://issues.apache.org/jira/browse/CLOUDSTACK-8647
.. _CLOUDSTACK-8635 : https://issues.apache.org/jira/browse/CLOUDSTACK-8635
.. _CLOUDSTACK-8625 : https://issues.apache.org/jira/browse/CLOUDSTACK-8625
.. _CLOUDSTACK-8624 : https://issues.apache.org/jira/browse/CLOUDSTACK-8624
.. _CLOUDSTACK-8607 : https://issues.apache.org/jira/browse/CLOUDSTACK-8607
.. _CLOUDSTACK-8596 : https://issues.apache.org/jira/browse/CLOUDSTACK-8596
.. _CLOUDSTACK-8590 : https://issues.apache.org/jira/browse/CLOUDSTACK-8590
.. _CLOUDSTACK-8589 : https://issues.apache.org/jira/browse/CLOUDSTACK-8589
.. _CLOUDSTACK-8580 : https://issues.apache.org/jira/browse/CLOUDSTACK-8580
.. _CLOUDSTACK-8581 : https://issues.apache.org/jira/browse/CLOUDSTACK-8581
.. _CLOUDSTACK-8426 : https://issues.apache.org/jira/browse/CLOUDSTACK-8426
.. _CLOUDSTACK-8424 : https://issues.apache.org/jira/browse/CLOUDSTACK-8424
.. _CLOUDSTACK-8457 : https://issues.apache.org/jira/browse/CLOUDSTACK-8457
.. _CLOUDSTACK-9034 : https://issues.apache.org/jira/browse/CLOUDSTACK-9034
.. _CLOUDSTACK-8272 : https://issues.apache.org/jira/browse/CLOUDSTACK-8272
.. _CLOUDSTACK-8197 : https://issues.apache.org/jira/browse/CLOUDSTACK-8197
.. _CLOUDSTACK-8151 : https://issues.apache.org/jira/browse/CLOUDSTACK-8151
.. _CLOUDSTACK-8133 : https://issues.apache.org/jira/browse/CLOUDSTACK-8133
.. _CLOUDSTACK-8169 : https://issues.apache.org/jira/browse/CLOUDSTACK-8169
.. _CLOUDSTACK-8063 : https://issues.apache.org/jira/browse/CLOUDSTACK-8063
.. _CLOUDSTACK-4719 : https://issues.apache.org/jira/browse/CLOUDSTACK-4719
.. _CLOUDSTACK-1667 : https://issues.apache.org/jira/browse/CLOUDSTACK-1667
.. _CLOUDSTACK-8989 : https://issues.apache.org/jira/browse/CLOUDSTACK-8989
.. _CLOUDSTACK-8992 : https://issues.apache.org/jira/browse/CLOUDSTACK-8992
.. _CLOUDSTACK-9044 : https://issues.apache.org/jira/browse/CLOUDSTACK-9044
.. _CLOUDSTACK-8433 : https://issues.apache.org/jira/browse/CLOUDSTACK-8433