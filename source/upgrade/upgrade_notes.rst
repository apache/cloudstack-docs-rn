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


General Upgrade Notes
=====================

Java version upgraded to Java 1.7
---------------------------------

As of Apache CloudStack 4.4, Java version required is 1.7 for the 
management-server, cloudstack-usage, KVM agent and system-VMs.


Depreciation of realhostip.com 
------------------------------
   
The realhostip.com dynamic DNS resolution service is being retired on
September 30th, 2014. In advance of that, CloudStack 4.3 and later no longer uses 
realhostip.com DNS domains or SSL certificates to encrypt Console Proxy or 
file copy communications.

For latest update about realhostip.com follow `Apache CloudStack Blog <https://blogs.apache.org/cloudstack/>`_.


Settings Changes
----------------

After upgrading to 4.2 and later, Settings ``mem.overporvisioning.factor`` and 
``cpu.overporvisioning.factor`` are now at the cluster level and be set to 1 
which is the default.

If Global Settings ``mem.overporvisioning.factor`` and 
``cpu.overporvisioning.factor`` have been changed prior the upgrade to 4.2 and 
later, the upgrade process will be reset them to 1. Values can be changed by 
editing clusters settings.

All clusters created after the upgrade will get created with the Global Settings 
values for ``mem.overporvisioning.factor`` and ``cpu.overporvisioning.factor``.


OVS plug-in
-----------

OVS plug-in functionality is disrupted if ovsdaemon crashes

A critical functionality issue came out with `CLOUDSTACK-6779 <https://issues.apache.org/jira/browse/CLOUDSTACK-6779>`_. On XenServer it
is observed that on VIF unplug Ovs-Vswitchd is crashing resulting in loosing all
the openflow rules added to the bridge. Ovs daemon gets started and creates a
bridge but configure openflow rules are lost resulting in the disruption of
connectivity for the VM's on the host.


Active-Directory Authentication (LDAP)
--------------------------------------

If using Active-Directory (LDAP/LDAPs) as user authentication; Upgrading to 
4.3 and later require changes in Global Settings. After upgrading CloudStack
to 4.3 or latest, following Global Settings must be change:

======================= ============== ==============
Global Settings         Default        New
======================= ============== ==============
ldap.user.object        inetOrgPerson  user
ldap.username.attribute uid            sAMAccountName
======================= ============== ==============


SystemVM 32bit deprecated
-------------------------

32bit versions of systemvm templates are in the process of behing deprecated. Upgrade instructions from this Release Notes use 64bit templates. 32bit systemvm-templates are available for this version on `http://cloudstack.apt-get.eu/systemvm/4.4/ <http://cloudstack.apt-get.eu/systemvm/4.4/>`_. Follow the dev mailing list for further updates.


.. not confirmed 
   Build From Sources
   ------------------
   
   Since CloudStack 4.2.1 build packages from source using non opensource 
   modules param ``-nonoss`` changed to ``-   noredist``.


