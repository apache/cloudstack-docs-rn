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


1) Improve Object Storage, CloudStack-8640, Wido
2) Snapshot Improvements, CloudStack-8663, Anshul
3) Deploy user Instance from VM Snapshot, CloudStack-8676, Sateesh
4) Netscaler Integration, CloudStack-8672, CloudStack-8673, Rajesh
5) Billing Quota, CloudStack-8592, Abhinandan, Rohit
6) Improve SAML plugin, CloudStack-8457, Rohit
7) LDAP Improvements - Trust AD and Auto Import, CloudStack-8647, Rajani, Sarath (even though this shows 4.7 - I know, the code has been merged to master).
8) Docker/Containers, No JIRA ticket, Pdion
9) iSCSI and HA support in Hyper-V, CloudStack-8444, Anshul
10) Support for non-US keyboards in Console Proxy, CloudStack-8665, Anshul


Redundant Routers for VPC
-------------------------

<TBD>

====================== ============================================================================
Supported hypervisors: N/A
Link                   `CLOUDSTACK-7583`_
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
Supported hypervisors: N/A
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





Improvements
------------

-  Enable configuring local storage use for system VMs at zone level.
-  Restore volume from volune-snapshot (KVM)
-  Addition of an empty custom.css for ease of UI customization.
-  Local Storage overprovisionning for KVM.
-  Provide smbios vendor information via KVM/Libvirt to Guest.
-  KVM vlan passthrough '4095', usable for nested hypervisor as instance.


.. _Browser Upload spec : https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=39620237
.. _CLOUDSTACK-7583 : https://issues.apache.org/jira/browse/CLOUDSTACK-7583
.. _CLOUDSTACK-7882 : https://issues.apache.org/jira/browse/CLOUDSTACK-7882