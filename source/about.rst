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

Version |release| includes 180 pull requests and fixes more than 75 bugs from the previous releases.

Due to some changes in the community, we had an extended period of time
without a release manager.  Because of this the 4.9.0 release is much larger
than usual and had a duration of about 6 months.

Going forward we should have more consistent releases again.

A LOT changed in this release, so this is not a complete list, but here is a 
quick summary of some of the changes.


Networking
----------

* Fixes to ACLs, S2S VPN, Private Gateways, Redundant VRs and other optimizations
* Nuage VSP SDN Plugin got a lot of improvements and some new features


Database
--------

* MySQL connector changed
* DB optimizations and improvements


Storage
-------

* Enabled fast snapshots for managed storage using XenServer
* Fixes for some RBD issues
* Fixes multiple Swift object store issues
* Improved VMware disk implementation


Usability
---------

* Added user defined roles
* Added configurable root volume size for KVM
* Lots of localization improvements
* Added CentOS 6.x guest OS mappings for VMware


Operations
----------

* Added Out-of-band power management for hosts (EG: IPMI, iLO, DRAC, etc.)


Miscellaneous
-------------

* Use non-blocking SSL handshake in NioConnection/Link
* Added memory utilization to ``listVirtualMachines``
* Multiple fixes related to usage



Build dependency
----------------

When building Apache CloudStack with ``noredist``, it now require the file
``deps/vim25_60.jar`` available from vSphere SDK 6.0,
VMware-vSphere-SDK-6.0.0-3634981.zip.

